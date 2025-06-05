import requests
import sqldatadef
from bs4 import BeautifulSoup
from fontTools.misc.cython import returns
import time

# Umrechnung der Längen und Breitengrade falls diese nicht im Dezimalformat angegeben wurden
def grad_to_dezimal(long, lat):
    splong = long.replace('°', ' ').replace("'", ' ').replace('"', ' ').split()
    splat = lat.replace('°', ' ').replace("'", ' ').replace('"', ' ').split()
    #print(splong, splat)
    long = int(splong[0]) + int(splong[1]) / 60 + int(splong[2]) / 3600  if len(splong) > 3 else int(splong[0]) + int(splong[1]) / 60
    lat = int(splat[0]) + int(splat[1]) / 60 + int(splat[2]) / 3600 if len(splat) > 3 else int(splat[0]) + int(splat[1]) / 60
    if splong[-1] == 'W':
        long = -long
    if splat[-1] == 'S':
        lat = -lat
    return round(long,6), round(lat,6)

#Wir nehmen die Längen- und Breitengrade und stellen im richtigen Formaat woeder in die Datenbank
def BreitGradinDez(array8):
    for i in range(1, len(array8)):
        longgrad = array8[i][2]
        latgrad = array8[i][3]
        new_long, new_lat = grad_to_dezimal(longgrad, latgrad)
        array8[i][2] = new_long
        array8[i][3] = new_lat

#entfernung von leeren Zeilen um nur die Daten anzeigen zu lassen die tatsächlich existieren
def no_empty_elements(array8):
    array9 = []
    for row in array8:
        row_clean = [elem for elem in row if elem != '']
        array9.append(row_clean)
    return array9

# Abrufen der Stationsübersicht. Da diese in html sind werden die hier umgewandelt. und passend formatiert.
# Default Text beeinhaltet die Städte die spziell für dieses Projekt ausgewählt wurden um auf jeden Fall die passenden Daten für diese Stationen zu bekommen.
def gettxtfromhtml(url):

    Jeju = "Jeju;47184;126°32'E;33°31'N;22;KOR;Republik Korea / Republic of Korea;Asien / Asia;\n;"
    Goiania = "Goiania;83423;49°16'W;16°40'S;741;BRA;Brasilien / Brazil;Südamerika / South America;\n;"
    Troll = "Troll;89504;2°32'E;72°01'S;1284;NOR;Norwegen / Norway;Antarktis / Antarctica;\n;"
    München = "München-Stadt;10865;11°32'E;48°10'N;526;DEU;Deutschland / Germany;Europa / Europe;\n;"
    Brocken = "Brocken;10453;10°37'E;51°48'N;1153;DEU;Deutschland / Germany;Europa / Europe;\n;"
    Itzehoe = "Itzehoe;10142;9°34'E;53°59'N;26;DEU;Deutschland / Germany;Europa / Europe;\n;"
    fallback = "Stationsname;Station_id;longitude;latitude;hoehe;Landkurz;land;kontinent;\n;"+ Jeju + Goiania + Troll + München + Brocken + Itzehoe

    #Versucht die Daten aus der HTML Website zu bekommen
    html_content = fetch_with_retries(url)

    #keine erflogreiche ABfrage der HTML Daten? Default Text wird hergenommen
    if not html_content:
        text_output = fallback
        #print(f"gettxtfromhtml liefert zurück:\n{result[:500]}")  # max 500 Zeichen Ausgabe
        return text_output

    #Herausfiltern der Tabellen auf der Website
    soup = BeautifulSoup(html_content, "html.parser")
    tables = soup.find_all("table")

    #existieren kein Tabellen wird der Default Text hergenommen um Fehler bei unserer Präsentation zu vermeiden
    if not tables:
        #print(f"gettxtfromhtml liefert zurücko:\n{result[:500]}")  # max 500 Zeichen Ausgabe
        return fallback

    # Tabelle 1 wird hergenommen. Da auf der DWD Seite für die Stationen nur 1 existiert gibt das für dieses Projekt sicher keine Probleme
    station_table = tables[0]
    result = ""

    #Wir holen uns den Text aus der gerade angegebenen Tabelle und formatieren ihn passend für die anderen Funktionen die diesen Text dann bearbeiten
    for row in station_table.find_all("tr"):
        cells = row.find_all(["th", "td"])
        line = ";".join(cell.get_text(strip = True)+";" for cell in cells)
        result += line + "\n"
    #print(f"gettxtfromhtml liefert zurückk:\n{result[:500]}")  # max 500 Zeichen Ausgabe
    return result
#print(text_output)

#Versuch an die HTML Website zu kommen. 5 Versuche im Abstand von 1 Sekunde.  Falls unerfolgreich wird eine Fehlertext zurückgegeben der uns im Logfile des Containers dann angezeigt wird
def fetch_with_retries(url, max_retries=5, wait_seconds=1, fallback_text="Fehler beim Laden der Seite."):
    attempt = 0
    while attempt < max_retries:
        try:
            response = requests.get(url, timeout=10) # Versucht an den Inhalt zu kommen und hat 10 Sekunden Zeit eine Antwort vom Client zu bekommen
            response.raise_for_status()  # wirft einen Fehler bei HTTP-Status 4xx/5xx
            return response.text
        except requests.exceptions.RequestException as e:
            #print(f"Fehler beim Abrufen (Versuch {attempt + 1}/{max_retries}): {e}")
            time.sleep(wait_seconds)
            attempt += 1
    return fallback_text


#da wir 2 Webseiten mit Daten haben und eine mit den Daten für die Stationen. werden erst die 2 datenarrays zusammengeführt.
#die Arrays werden passend formatiert und bekommen bei fehlenden Werten, Fülldaten die die Auswertung nicht groß beeinflussen und auch bei Grafischen Darstellungen nicht direkt auffallen dürften

def filltable(array4, array7, array8, city_name):
    global array5
    #print(array4)
    array5 = array4[:]

    if len(array5) > 1:
        del array5[-1]

    if len(array7) > 1:
        del array7[0]
        del array7[-1]

    array5.extend(array7)



    for i, row in enumerate(array5):
        if len(row) < len(array5[0]):
            array5[i].extend(['0.0'] * (len(array5[0]) - len(row)))

    for i, row in enumerate (array5):
        for j,value in enumerate(row):
            if value == '':
                array5[i][j]= '0.0'     #default wert, falls was Besseres einfällt bitte ändern. Könnte grafiken verhunzen

    #print(array5)
    if len(array5) > 1:
        del array5[0] #Überschriften werden gelöscht da sonst Fehler beim Einfüllen in die Datenbank.

    #berechnung der Jahresdurchschnittstemperaturen
    #0.0 wird nicht eingerechnet da dies aktuell ein Defaultwert für nicht vorhandene Werte ist
    for i, row in enumerate(array5):

        if len(row) == 13:
            try:
                values = [float(val) for val in row[1:]]  # skip Jahr
                jahr = sum(values) / len(values)
            except ValueError:
                jahr = 0.0
            array5[i].append(round(jahr, 1))
        else:
            array5[i].append('0.0')

    #Angabe des Zeitraums für die Durchschnittsberechnung und berechnung der Monatsdurchschnittswerte. 0.0 wird mit eingerechnet - muss noch angepasst werden
    zeitraum = array5[0][0] + "-" + array5[-1][0]
    array10 = [zeitraum, jahr]
    for i in range(1, len(array5[0])-1):
        summ = 0.0
        k = 0
        for j in range(1, len(array5)):
            try:
                summ = float(array5[j][i]) + summ
                k += 1
            except ValueError:
                continue
        array10.insert(i, summ / k if k > 0 else 0.0)
    array5.append(array10)
    #Einfügen und sortierung der Daten zu den Stationen
    for i in range(len(array5)):
        for j in range(len(array8)):
            if array8[j][0] == city_name:
                array5[i].insert(0, array8[j][1])
                array5[i].insert(1, array8[j][0])
                array5[i].insert(2, array8[j][6])
                array5[i].insert(4, 0)
                array5[i].append(array8[j][2])
                array5[i].append(array8[j][3])
                array5[i].append(array8[j][4])
                break
    # falls array8 nicht richtig formatiert ist (weil z.B. werte fehlen) werden defaultwerte eingefügt. Ist jedoch noch hardcoded auf 14 Elemente da dieses Probleme mit der DWD Stationsliste genauso auftritt (Stand: 02.06.25)
    for i in range(len(array5)):
        if len(array5[i]) == 14:
            array5[i].insert(0, 00000)
            array5[i].insert(1, city_name)
            array5[i].insert(2, "unknown")
            array5[i].insert(4, 0)
            array5[i].append(0.000)
            array5[i].append(0.000)
            array5[i].append(0)

#Durchführung aller nötigen Funktionen
def getdata(urlhist, urlrec, urlstation, db_name, table_name, city_name):
    response = requests.get(urlhist)
    file = response.text
    array = []
    array2 = []
    array4 = []
    array7 = []
    array8 = []

    sqldatadef.getlines(file, array)
    sqldatadef.getcells(array, array2)
    sqldatadef.addZero(array2, array4)
    array.clear()
    array2.clear()

    response = requests.get(urlrec)
    file = response.text
    sqldatadef.getlines(file, array, "\n")
    sqldatadef.getcells(array, array2)
    sqldatadef.addZero(array2, array7)
    array.clear()
    array2.clear()

    file = gettxtfromhtml(urlstation)
    sqldatadef.getlines(file, array, "\n")
    sqldatadef.getcells(array, array2)
    array2 = [row for row in array2 if any(cell.strip() for cell in row)]
    sqldatadef.addZero(array2, array8)
    array8 = no_empty_elements(array8)
    #print(array8)
    #print(f"array8 Länge: {len(array8)}")
    #print(f"array8 Inhalt (erste 3 Zeilen): {array8[:3]}")
    BreitGradinDez(array8)
    #print(array8)

    array.clear()
    array2.clear()

    sqldatadef.database(db_name)
    sqldatadef.tables(table_name)
    filltable(array4, array7, array8, city_name)

    with sqldatadef.cnx.cursor() as cursor:
        cursor.execute(sqldatadef.createtable)
        sqldatadef.cnx.commit()
        sqldatadef.filldatabase(array5, sqldatadef.cnx, table_name)
        sqldatadef.cnx.commit()
        sqldatadef.cnx.close()

    array4.clear()
    array7.clear()
    array8.clear()
