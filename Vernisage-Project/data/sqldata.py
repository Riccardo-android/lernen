import os

import requests
import mysql.connector
import time

from mysql.connector import errorcode
from sympy.solvers.ode.single import SeparableReduced



def getlines(filename, results):
   line = filename.split(sep="\r\n")
   results.extend(line)
   return(results)

def getcells(results, array2):
    for i in results:
        #i = i.replace(" ","")
        cells = i.split(sep=";")
        array2.append(cells)
        #array2 = [item.replace(" .", "0.") for item in cells]
    return array2

def addZero(results, array4):
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
        exit(2)

def filldatabase(array4, array7, cnx, TABLE_NAME):
    array5 = array4
    del array5[0]
    del array5[len(array5) - 1]
    del array7[0]
    del array7[len(array7) - 1]
    print(array7)
    for i in range(len(array5)):
        for j in range(len(array7)):
            if array5[i][0] == array7[j][0]:
                array5[i].insert(1, array7[j][1])
                array5[i].insert(2, array7[j][5])
                break
        else:
            array5[i].insert(1, "unknown")
            array5[i].insert(2, "unknown")

    id = [int(k[0]) for k in array5]
    ort = [str(k[1]) for k in array5]
    bland = [str(k[2]) for k in array5]
    bzzeit = [str(k[3]) for k in array5]
    source = [int(k[4]) for k in array5]
    Jan = [float(k[5]) for k in array5]
    Feb = [float(k[6]) for k in array5]
    Mar = [float(k[7]) for k in array5]
    Apr = [float(k[8]) for k in array5]
    May = [float(k[9]) for k in array5]
    Jun = [float(k[10]) for k in array5]
    Jul = [float(k[11]) for k in array5]
    Aug = [float(k[12]) for k in array5]
    Sep = [float(k[13]) for k in array5]
    Oct = [float(k[14]) for k in array5]
    Nov = [float(k[15]) for k in array5]
    Dec = [float(k[16]) for k in array5]
    Jahr = [float(k[17]) for k in array5]
    array6 = list(zip(id, ort, bland, bzzeit,source, Jan, Feb, Mar, Apr, May, Jun, Jul, Aug,Sep, Oct, Nov, Dec, Jahr))

    with cnx.cursor() as cursor:
        cursor.executemany('INSERT INTO ' + TABLE_NAME + '  (Stations_id, Stationsname, Bundesland, Zeitraum, Datenquelle, Januar, Februar, Marz, April, Mai, Juni, Juli, August, September, Oktober, November, Dezember, avg_Jahr) '
                    'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE Stations_id = Stations_id',array6)


def getdata(url, urlsname, DB_NAME, TABLE_NAME):
    response = requests.get(url)
    file = response.text
    array = []
    array2 = []
    array4 = []
    array7 = []

    getlines(file, array)
    getcells(array, array2)
    addZero(array2, array4)
    array.clear()
    array2.clear()

    response = requests.get(urlsname)
    file = response.text
    getlines(file, array)
    getcells(array, array2)
    addZero(array2, array7)

    try:
        cnx = mysql.connector.connect(user='root', password='Pr!m4bAl13rina', host="db", port=3306)
        cursor = cnx.cursor()
        try:
            cursor.execute("USE {}".format(DB_NAME))
        except mysql.connector.Error as err:
            print("Failed to use database: {}".format(err))
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                create_database(cursor)
                print("Database {} created successfully".format(DB_NAME))
                cnx.database = DB_NAME
            else:
                print(err)
                exit(1)
    except mysql.connector.Error as err:
        print("Failed to create database: {}".format(err))
        exit(3)

    TABLES = {}
    avgtemp = """CREATE TABLE IF NOT EXISTS """ + TABLE_NAME + """ (
                                       `Stations_ID` int NOT NULL AUTO_INCREMENT,
                                       `Stationsname` varchar(255) NOT NULL,
                                       `Bundesland` varchar(255) NOT NULL, 
                                       `Zeitraum` varchar(255) NOT NULL, 
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
                                       PRIMARY KEY (`Stations_ID`,`Stationsname`,`Zeitraum`)
                                       ) ENGINE=InnoDB
                                       """

    with cnx.cursor() as cursor:
        cursor.execute(avgtemp)
        cnx.commit()
        filldatabase(array4, array7, cnx, TABLE_NAME)
        cnx.commit()
        cnx.close()
        array4.clear()
        array7.clear()

#connect with DWD API
DB_NAME = "hist_climate_ger"
TABLE_NAME = "avg_temp_ger_6120"
url = "https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/multi_annual/mean_91-20/Temperatur_1991-2020.txt"
urlsname = "https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/multi_annual/mean_91-20/Temperatur_1991-2020_Stationsliste.txt"
getdata(url, urlsname, DB_NAME, TABLE_NAME)

url = "https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/multi_annual/mean_61-90/Temperatur_1961-1990.txt"
urlsname = "https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/multi_annual/mean_61-90/Temperatur_1961-1990_Stationsliste.txt"
getdata(url, urlsname, DB_NAME, TABLE_NAME)

TABLE_NAME = "Eistage_ger_6120"
url = "https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/multi_annual/mean_91-20/Eistage_1991-2020.txt"
urlsname = "https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/multi_annual/mean_91-20/Eistage_1991-2020_Stationsliste.txt"
getdata(url, urlsname, DB_NAME, TABLE_NAME)

url = "https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/multi_annual/mean_61-90/Eistage_1961-1990.txt"
urlsname = "https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/multi_annual/mean_61-90/Eistage_1961-1990_Stationsliste.txt"
getdata(url, urlsname, DB_NAME, TABLE_NAME)

TABLE_NAME = "Frosttage_ger_6120"
url = "https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/multi_annual/mean_91-20/Frosttage_1991-2020.txt"
urlsname = "https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/multi_annual/mean_91-20/Frosttage_1991-2020_Stationsliste.txt"
getdata(url, urlsname, DB_NAME, TABLE_NAME)

url = "https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/multi_annual/mean_61-90/Frosttage_1961-1990.txt"
urlsname = "https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/multi_annual/mean_61-90/Frosttage_1961-1990_Stationsliste.txt"
getdata(url, urlsname, DB_NAME, TABLE_NAME)

TABLE_NAME = "Heissetage_ger_6120"
url = "https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/multi_annual/mean_91-20/Heissetage_1991-2020.txt"
urlsname = "https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/multi_annual/mean_91-20/Heissetage_1991-2020_Stationsliste.txt"
getdata(url, urlsname, DB_NAME, TABLE_NAME)

url = "https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/multi_annual/mean_61-90/Heissetage_1961-1990.txt"
urlsname = "https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/multi_annual/mean_61-90/Heissetage_1961-1990_Stationsliste.txt"
getdata(url, urlsname, DB_NAME, TABLE_NAME)

TABLE_NAME = "Niederschlag_ger_6120"
url = "https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/multi_annual/mean_91-20/Niederschlag_1991-2020.txt"
urlsname = "https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/multi_annual/mean_91-20/Niederschlag_1991-2020_Stationsliste.txt"
getdata(url, urlsname, DB_NAME, TABLE_NAME)

url = "https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/multi_annual/mean_61-90/Niederschlag_1961-1990.txt"
urlsname = "https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/multi_annual/mean_61-90/Niederschlag_1961-1990_Stationsliste.txt"
getdata(url, urlsname, DB_NAME, TABLE_NAME)

TABLE_NAME = "Sommertage_ger_6120"
url = "https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/multi_annual/mean_91-20/Sommertage_1991-2020.txt"
urlsname = "https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/multi_annual/mean_91-20/Sommertage_1991-2020_Stationsliste.txt"
getdata(url, urlsname, DB_NAME, TABLE_NAME)

url = "https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/multi_annual/mean_61-90/Sommertage_1961-1990.txt"
urlsname = "https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/multi_annual/mean_61-90/Sommertage_1961-1990_Stationsliste.txt"
getdata(url, urlsname, DB_NAME, TABLE_NAME)

TABLE_NAME = "Sonnenscheindauer_ger_6120"
url = "https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/multi_annual/mean_91-20/Sonnenscheindauer_1991-2020.txt"
urlsname = "https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/multi_annual/mean_91-20/Sonnenscheindauer_1991-2020_Stationsliste.txt"
getdata(url, urlsname, DB_NAME, TABLE_NAME)

url = "https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/multi_annual/mean_61-90/Sonnenscheindauer_1961-1990.txt"
urlsname = "https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/multi_annual/mean_61-90/Sonnenscheindauer_1961-1990_Stationsliste.txt"
getdata(url, urlsname, DB_NAME, TABLE_NAME)