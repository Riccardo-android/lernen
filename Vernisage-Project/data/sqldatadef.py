import os
import requests
import mysql.connector
import time

from mysql.connector import errorcode
from polars.testing.parametric import column
from sympy.solvers.ode.single import SeparableReduced

#teilen der textdatei in Zeilen. Jedes Element ist eine Zeile der txt datei
def getlines(filename, results, sign="\r\n"):
   line = filename.split(sep=sign)
   results.extend(line)
   return(results)

#Aufteilen der jeweiligen Zeilen in die einzelnen Daten
def getcells(results, array2):
    for i in results:
        cells = i.split(sep=";")
        array2.append(cells)
    return array2

#Anpassen der Daten um mögliche Probleme zu umgehen
def addZero(results, array4):
    for i in range(len(results)):
        array3 = []
        for j in range(len(results[i])):
           new_i = str(results[i][j])
           new_i = new_i.replace(" .", "0.")
           new_i = new_i.replace("-.", "-0.")
           new_i = new_i.replace("ä", "ae")
           new_i = new_i.replace("ö", "oe")
           new_i = new_i.replace("ü", "ue")
           new_i = new_i.replace("ß", "ss")
           new_i = new_i.replace(" ", "")
           array3.append(new_i)
        if array3 and array3[-1].strip() == '':
            array3.pop()
        array4.append(array3)
    return array4

#wird nur aufgerufen falls die Datenbank noch nicht existiert. Zur Sicherheit wird es aber auch hier nochmal überprüft
#Falls die Verbindung zur MYSQL Datenbank fehlschlägt bekommen wir einen Error. mit Errorcode 2 um besser zu wo der Verbindungserror passiert ist
def create_database(cursor, db_name):
    try:
         cursor.execute("CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(db_name))
    except mysql.connector.Error as err:
        print("Failed to create database: {}".format(err))
        exit(2)

#Zusammenstellen der 2 arrays in der passenden Reihgenfolge für die Datenbank. array4 hat Daten, array7 hat die Informationen zur Station
#Bei fehlenden Daten fügen wir default Werte ein die klar erkennbar sind
def adjhistdata(array4, array7):
    global array5
    array5 = array4[:]
    if len(array5) > 1:
        del array5[0]
        del array5[-1]
    if len(array7) > 1:
       del array7[0]
       del array7[-1]
    for i in range(len(array5)):
        for j in range(len(array7)):
            if array5[i][0] == array7[j][0]:
                array5[i].insert(1, array7[j][1])
                array5[i].insert(2, array7[j][5])
                array5[i].append(array7[j][2])
                array5[i].append(array7[j][3])
                array5[i].append(array7[j][4])
                break
        else:
            array5[i].insert(1, "unknown")
            array5[i].insert(2, "unknown")
            array5[i].append(0)
            array5[i].append(0)
            array5[i].append(100000)


# Die Daten werden nun von text auf das Format gebracht was für die jeweilige Spalte notwendig ist und in die Datenbank eingefügt.

def filldatabase(array5, cnx, table_name):
    id = [int(float(k[0])) for k in array5]
    ort = [str(k[1]) for k in array5]
    bland = [str(k[2]) for k in array5]
    bzzeit = [str(k[3]) for k in array5]
    source = [int(float(k[4])) for k in array5]
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
    slati = [float(k[18]) for k in array5]
    slongi = [float(k[19]) for k in array5]
    sheight = [float(k[20]) for k in array5]
    array6 = list(zip(id, ort, bland, bzzeit,source, Jan, Feb, Mar, Apr, May, Jun, Jul, Aug,Sep, Oct, Nov, Dec, Jahr, slati, slongi, sheight))

    with cnx.cursor() as cursor:
        cursor.executemany('INSERT INTO ' + table_name + '  (Stations_id, Stationsname, Land, Zeitraum, Datenquelle, Januar, Februar, Marz, April, Mai, Juni, Juli, August, September, Oktober, November, Dezember, avg_Jahr, latitude, longitude, Stationshoehe) '
                    'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE Stations_id = Stations_id',array6)

#Versucht mit MYSQL zu verbinden. und erkennt ob die Datenbank schon existiert oder noch erstellt werden muss.
def database(db_name):
    global cnx, cursor
    try:
        cnx = mysql.connector.connect(user='root', password='Pr!m4bAl13rina', host="db", port=3306)
        cursor = cnx.cursor()
        try:
            cursor.execute("USE {}".format(db_name))
        except mysql.connector.Error as err:
            print("Failed to use database: {}".format(err))
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                create_database(cursor, db_name)
                print("Database {} created successfully".format(db_name))
                cnx.database = db_name
            else:
                print(err)
                exit(1)
    except mysql.connector.Error as err:
        print("Failed to create database: {}".format(err))
        exit(3)


#Erstellung der Tables für die jeweilige Datenbank. Aktuell kann keine Spalte nachträglich eingefügt werden sondern muss bei der intiaisierung schon dabei sein.
#Primary Key besteht aus 3 Komponenten um sicherzustellen das benötigten Daten in die Datenbank eingefügt werden
def tables(table_name):
    global createtable
    createtable = """CREATE TABLE IF NOT EXISTS """ + table_name + """ (
                                       `Stations_ID` int NOT NULL AUTO_INCREMENT,
                                       `Stationsname` varchar(255) NOT NULL,
                                       `Land` varchar(255) NOT NULL, 
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
                                       `latitude` float NOT NULL, 
                                       `longitude` float NOT NULL, 
                                       `Stationshoehe` float NOT NULL, 
                                       PRIMARY KEY (`Stations_ID`,`Stationsname`,`Zeitraum`)
                                       ) ENGINE=InnoDB
                                       """


#wird nicht benutzt, ist aber vorhanden falls man eine Float Erkennung später braucht
def is_number(s):
    try:
        float(s) # für Float- und Int-Werte
        return True
    except ValueError:
        return False



#Durchführung aller nötigen Funktionen
def getdata(url, urlsname, db_name, table_name):
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

    database(db_name)
    tables(table_name)

    with cnx.cursor() as cursor:
        cursor.execute(createtable)
        cnx.commit()

    adjhistdata(array4, array7)

    with cnx.cursor() as cursor:
        filldatabase(array5, cnx, table_name)
        cnx.commit()
        cnx.close()
    array4.clear()
    array7.clear()
