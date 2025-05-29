import requests
import pymysql
import mysql.connector
from mysql.connector import errorcode
from sympy.solvers.ode.single import SeparableReduced

def getlines(filename, results):
   line = filename.split(sep="\r\n")
   results.extend(line)
   return(results)

def getcells(results):
    for i in results:
        #i = i.replace(" ","")
        cells = i.split(sep=";")
        array2.append(cells)
        #array2 = [item.replace(" .", "0.") for item in cells]
    return array2

def addZero(results):
    for i in range(len(results)):
        array3 = []
        for j in range(len(results[i])):
           new_i = str(results[i][j])
           new_i = new_i.replace(" .", "0.")
           new_i = new_i.replace("-.", "-0.")
           new_i = new_i.replace(" ", "")
           array3.append(new_i)
        array3.pop()
        array4.append(array3)
    return array4

def create_database(cursor):
    try:
         cursor.execute("CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed to create database: {}".format(err))
        exit(1)

def filldatabase():
    array5 = array4
    del array5[0]
    del array5[len(array5) - 1]
    id = [int(k[0]) for k in array5]
    Bzeit = [str(k[1]) for k in array5]
    source = [int(k[2]) for k in array5]
    Jan = [float(k[3]) for k in array5]
    Feb = [float(k[4]) for k in array5]
    Mar = [float(k[5]) for k in array5]
    Apr = [float(k[6]) for k in array5]
    May = [float(k[7]) for k in array5]
    Jun = [float(k[8]) for k in array5]
    Jul = [float(k[9]) for k in array5]
    Aug = [float(k[10]) for k in array5]
    Sep = [float(k[11]) for k in array5]
    Oct = [float(k[12]) for k in array5]
    Nov = [float(k[13]) for k in array5]
    Dec = [float(k[14]) for k in array5]
    Jahr = [float(k[15]) for k in array5]
    array6 = list(zip(id, Bzeit,source, Jan, Feb, Mar, Apr, May, Jun, Jul, Aug,Sep, Oct, Nov, Dec, Jahr))

    with cnx.cursor() as cursor:
        cursor.executemany('INSERT INTO  avg_temp_ger_9020 (Stations_id, Zeitraum, Datenquelle, Januar, Februar, Marz, April, Mai, Juni, Juli, August, September, Oktober, November, Dezember, avg_Jahr) '
                    'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE Stations_id = Stations_id',array6)


#connect with DWD API
url = "https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/multi_annual/mean_91-20/Temperatur_1991-2020.txt"
response = requests.get(url)
file = response.text

array = []
array2 = []
array4 = []




#query = "INSERT INTO table VALUES (%s)"
#cur.execute(query, file_content,)



getlines(file, array)
getcells(array)
addZero(array2)
#print(array4)
DB_NAME = 'hist_temp_ger'
try:
    cnx = mysql.connector.connect(user='root', password='Pr!m4bAl13rina', host='127.0.0.1', port= 3307)
    cursor = cnx.cursor()
    try:
        cursor.execute("USE {}".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed to create database: {}".format(err))
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            create_database(cursor)
            print("Database {} created successfully".format(DB_NAME))
            cnx.database = DB_NAME
        else:
            print(err)
            exit(1)
except mysql.connector.Error as err:
    print("Failed to create database: {}".format(err))
    exit(1)

TABLES = {}
avgtemp = """CREATE TABLE IF NOT EXISTS avg_temp_ger_9020 (
                                       `Stations_ID` int NOT NULL AUTO_INCREMENT, 
                                       `Zeitraum` char(9) NOT NULL, 
                                       `Datenquelle` int NOT NULL, 
                                       `Januar` float NOT NULL, 
                                       `Februar` float NOT NULL, 
                                       `Marz` float NOT NULL, 
                                       `April` float NOT NULL, 
                                       `Mai` float NOT NULL, 
                                       `Juni` float NOT NULL, 
                                       `Juli` float NOT NULL, 
                                       `August` float NOT NULL, 
                                       `September` float NOT NULL, 
                                       `Oktober` float NOT NULL, 
                                       `November` float NOT NULL, 
                                       `Dezember` float NOT NULL, 
                                       `avg_Jahr` float NOT NULL,
                                       PRIMARY KEY (`Stations_ID`)
                                       ) ENGINE=InnoDB
                                       """

with cnx.cursor() as cursor:
    cursor.execute(avgtemp)
    cnx.commit()
    filldatabase()
    cnx.commit()
    cnx.close()



"""

print(array2)
#for x in array:
 #print(x)
"""

