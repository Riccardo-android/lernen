import requests
import pymysql
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

def filldatabase():
    array5 = array4
    del array5[0]
    del array5[len(array5) - 1]
    #print(array5)
    id = [(int(k[0]),) for k in array5]
    Bzeit = [(str(k[1]),) for k in array5]
    source = [(int(k[2]),) for k in array5]
    Jan = [(float(k[3]),) for k in array5]
    Feb = [(float(k[4]),) for k in array5]
    Mar = [(float(k[5]),) for k in array5]
    Apr = [(float(k[6]),) for k in array5]
    May = [(float(k[7]),) for k in array5]
    Jun = [(float(k[8]),) for k in array5]
    Jul = [(float(k[9]),) for k in array5]
    Aug = [(float(k[10]),) for k in array5]
    Sep = [(float(k[11]),) for k in array5]
    Oct = [(float(k[12]),) for k in array5]
    Nov = [(float(k[13]),) for k in array5]
    Dec = [(float(k[14]),) for k in array5]
    Jahr = [(float(k[15]),) for k in array5]
    array6 = list(zip(id, Bzeit,source, Jan, Feb, Mar, Apr, May, Jun, Jul, Aug,Sep, Oct, Nov, Dec, Jahr))

    cur.executemany('INSERT INTO  avg_temp_ger_all_stations (Stations_id, Bezugszeitraum, Datenquelle, Januar, Februar, März, April, Mai, Juni, Juli, August, September, Oktober, November, Dezember, avg_Jahr) '
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


#connecte mit existierender Datenbank
con = pymysql.connect(host = '127.0.0.1', user = 'root', passwd = 'Pr!m4bAl13rina', db = 'hist_ger_9020', port = 3307)

#
cur = con.cursor()
filldatabase()
con.commit()
con.close()



"""

print(array2)
#for x in array:
 #print(x)
"""

