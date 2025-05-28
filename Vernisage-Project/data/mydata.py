#from getpass import getpass
#from mysql.connector import connect, Error

import requests
import pymysql

url = "https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/multi_annual/mean_91-20/Temperatur_1991-2020.txt"

print(url)









"""
try:
    with connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
    ) as connection:
        create_db_query = "CREATE DATABASE IF NOT EXISTS mydb"
        with connection.cursor() as cursor:
         cursor.execute(create_db_query)

        show_db_query = "SHOW DATABASES LIKE 'mydb'"
        with connection.cursor() as cursor:
            cursor.execute(show_db_query)
            for db in cursor:
                print(db)

except Error as e:
    print(e)
"""



