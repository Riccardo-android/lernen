import histflivefunc
import sqldatadef

# Hier werden nur die Funktionen, in die wir brauchen um die Datenbank zu füllen aufgerufen. Damit es einfacher ist, wurde der gesamte Ablauf in getdata gepackt
#Funktionsdefinition da wir über einen Container 2 Scripte ausführen müssen. wird in sqldata.py aufgerufen
def usehistflive():

    urlstation = "https://www.dwd.de/DE/leistungen/klimadatenweltweit/stationsverzeichnis.html?lsbId=374532"
    db_name = "hist_climate_global"
    table_name = "temp"


    urlhist =  "https://opendata.dwd.de/climate_environment/CDC/observations_global/CLIMAT/monthly/qc/air_temperature_mean/historical/47184_198901_202212.txt"
    urlrec =  "https://opendata.dwd.de/climate_environment/CDC/observations_global/CLIMAT/monthly/qc/air_temperature_mean/recent/47184.txt"
    city_name = "Jeju"
    histflivefunc.getdata(urlhist, urlrec, urlstation, db_name, table_name, city_name)

    urlhist =  "https://opendata.dwd.de/climate_environment/CDC/observations_global/CLIMAT/monthly/qc/air_temperature_mean/historical/83423_196901_202212.txt"
    urlrec =  "https://opendata.dwd.de/climate_environment/CDC/observations_global/CLIMAT/monthly/qc/air_temperature_mean/recent/83423.txt"
    city_name = "Goiania"
    histflivefunc.getdata(urlhist, urlrec, urlstation, db_name, table_name, city_name)

    urlhist = "https://opendata.dwd.de/climate_environment/CDC/observations_global/CLIMAT/monthly/qc/air_temperature_mean/historical/89054_199304_201412.txt"
    urlrec = "https://opendata.dwd.de/climate_environment/CDC/observations_global/CLIMAT/monthly/qc/air_temperature_mean/recent/89504.txt"
    city_name = "Troll"
    histflivefunc.getdata(urlhist, urlrec, urlstation, db_name, table_name, city_name)

    urlhist =  "https://opendata.dwd.de/climate_environment/CDC/observations_global/CLIMAT/monthly/qc/air_temperature_mean/historical/10865_200201_202212.txt"
    urlrec =  "https://opendata.dwd.de/climate_environment/CDC/observations_global/CLIMAT/monthly/qc/air_temperature_mean/recent/10865.txt"
    city_name = "München"
    histflivefunc.getdata(urlhist, urlrec, urlstation, db_name, table_name, city_name)

    urlhist = "https://opendata.dwd.de/climate_environment/CDC/observations_global/CLIMAT/monthly/qc/air_temperature_mean/historical/10453_199101_202212.txt"
    urlrec = "https://opendata.dwd.de/climate_environment/CDC/observations_global/CLIMAT/monthly/qc/air_temperature_mean/recent/10453.txt"
    city_name = "Brocken"
    histflivefunc.getdata(urlhist, urlrec, urlstation, db_name, table_name, city_name)


    urlhist = "https://opendata.dwd.de/climate_environment/CDC/observations_global/CLIMAT/monthly/qc/air_temperature_mean/historical/10142_200309_202212.txt"
    urlrec = "https://opendata.dwd.de/climate_environment/CDC/observations_global/CLIMAT/monthly/qc/air_temperature_mean/recent/10142.txt"
    city_name = "Itzehoe"
    histflivefunc.getdata(urlhist, urlrec, urlstation, db_name, table_name, city_name)

#---------------------------------------------------------------------------------------------------------------------------------------------------------#

    table_name = "sunshineduration"

    urlhist =  "https://opendata.dwd.de/climate_environment/CDC/observations_global/CLIMAT/monthly/qc/sunshine_duration/historical/47184_198901_202212.txt"
    urlrec =  "https://opendata.dwd.de/climate_environment/CDC/observations_global/CLIMAT/monthly/qc/sunshine_duration/recent/47184.txt"
    city_name = "Jeju"
    histflivefunc.getdata(urlhist, urlrec, urlstation, db_name, table_name, city_name)

    urlhist =  "https://opendata.dwd.de/climate_environment/CDC/observations_global/CLIMAT/monthly/qc/sunshine_duration/historical/83423_200404_202212.txt"
    urlrec =  "https://opendata.dwd.de/climate_environment/CDC/observations_global/CLIMAT/monthly/qc/sunshine_duration/recent/83423.txt"
    city_name = "Goiania"
    histflivefunc.getdata(urlhist, urlrec, urlstation, db_name, table_name, city_name)
    """
    urlhist = "https://opendata.dwd.de/climate_environment/CDC/observations_global/CLIMAT/monthly/qc/air_temperature_mean/historical/89054_199304_201412.txt"
    urlrec = "https://opendata.dwd.de/climate_environment/CDC/observations_global/CLIMAT/monthly/qc/air_temperature_mean/recent/89504.txt"
    city_name = "Troll"
    histflivefunc.getdata(urlhist, urlrec, urlstation, db_name, table_name, city_name)
    """
    urlhist =  "https://opendata.dwd.de/climate_environment/CDC/observations_global/CLIMAT/monthly/qc/sunshine_duration/historical/10865_200201_202212.txt"
    urlrec =  "https://opendata.dwd.de/climate_environment/CDC/observations_global/CLIMAT/monthly/qc/sunshine_duration/recent/10865.txt"
    city_name = "München"
    histflivefunc.getdata(urlhist, urlrec, urlstation, db_name, table_name, city_name)

    urlhist = "https://opendata.dwd.de/climate_environment/CDC/observations_global/CLIMAT/monthly/qc/sunshine_duration/historical/10453_199101_202212.txt"
    urlrec = "https://opendata.dwd.de/climate_environment/CDC/observations_global/CLIMAT/monthly/qc/sunshine_duration/recent/10453.txt"
    city_name = "Brocken"
    histflivefunc.getdata(urlhist, urlrec, urlstation, db_name, table_name, city_name)


    urlhist = "https://opendata.dwd.de/climate_environment/CDC/observations_global/CLIMAT/monthly/qc/sunshine_duration/historical/10142_200309_201912.txt"
    urlrec = "https://opendata.dwd.de/climate_environment/CDC/observations_global/CLIMAT/monthly/qc/sunshine_duration/recent/10142.txt"
    city_name = "Itzehoe"
    histflivefunc.getdata(urlhist, urlrec, urlstation, db_name, table_name, city_name)

#---------------------------------------------------------------------------------------------------------------------------------------------------------#

    table_name = "Niederschlag"

    urlhist =  "https://opendata.dwd.de/climate_environment/CDC/observations_global/CLIMAT/monthly/qc/precipitation_total/historical/47184_198901_202212.txt"
    urlrec =  "https://opendata.dwd.de/climate_environment/CDC/observations_global/CLIMAT/monthly/qc/precipitation_total/recent/47184.txt"
    city_name = "Jeju"
    histflivefunc.getdata(urlhist, urlrec, urlstation, db_name, table_name, city_name)

    urlhist =  "https://opendata.dwd.de/climate_environment/CDC/observations_global/CLIMAT/monthly/qc/precipitation_total/historical/83423_196901_202212.txt"
    urlrec =  "https://opendata.dwd.de/climate_environment/CDC/observations_global/CLIMAT/monthly/qc/precipitation_total/recent/83423.txt"
    city_name = "Goiania"
    histflivefunc.getdata(urlhist, urlrec, urlstation, db_name, table_name, city_name)
    """
    urlhist = "https://opendata.dwd.de/climate_environment/CDC/observations_global/CLIMAT/monthly/qc/precipitation_total/historical/89054_199304_201506.txt"
    urlrec = "https://opendata.dwd.de/climate_environment/CDC/observations_global/CLIMAT/monthly/qc/precipitation_total/recent/89054.txt"
    city_name = "Troll"
    histflivefunc.getdata(urlhist, urlrec, urlstation, db_name, table_name, city_name)
    """
    urlhist =  "https://opendata.dwd.de/climate_environment/CDC/observations_global/CLIMAT/monthly/qc/precipitation_total/historical/10865_200201_202212.txt"
    urlrec =  "https://opendata.dwd.de/climate_environment/CDC/observations_global/CLIMAT/monthly/qc/precipitation_total/recent/10865.txt"
    city_name = "München"
    histflivefunc.getdata(urlhist, urlrec, urlstation, db_name, table_name, city_name)

    urlhist = "https://opendata.dwd.de/climate_environment/CDC/observations_global/CLIMAT/monthly/qc/precipitation_total/historical/10453_199101_202212.txt"
    urlrec = "https://opendata.dwd.de/climate_environment/CDC/observations_global/CLIMAT/monthly/qc/precipitation_total/recent/10453.txt"
    city_name = "Brocken"
    histflivefunc.getdata(urlhist, urlrec, urlstation, db_name, table_name, city_name)


    urlhist = "https://opendata.dwd.de/climate_environment/CDC/observations_global/CLIMAT/monthly/qc/precipitation_total/historical/10142_200309_202212.txt"
    urlrec = "https://opendata.dwd.de/climate_environment/CDC/observations_global/CLIMAT/monthly/qc/precipitation_total/recent/10142.txt"
    city_name = "Itzehoe"
    histflivefunc.getdata(urlhist, urlrec, urlstation, db_name, table_name, city_name)
#---------------------------------------------------------------------------------------------------------------------------------------------------------#

    table_name = "temp_abs_max"

    urlhist =  "https://opendata.dwd.de/climate_environment/CDC/observations_global/CLIMAT/monthly/qc/air_temperature_absolute_max/historical/47184_199901_202212.txt"
    urlrec =  "https://opendata.dwd.de/climate_environment/CDC/observations_global/CLIMAT/monthly/qc/air_temperature_absolute_max/recent/47184.txt"
    city_name = "Jeju"
    histflivefunc.getdata(urlhist, urlrec, urlstation, db_name, table_name, city_name)

    urlhist =  "https://opendata.dwd.de/climate_environment/CDC/observations_global/CLIMAT/monthly/qc/air_temperature_absolute_max/historical/83423_201207_202212.txt"
    urlrec =  "https://opendata.dwd.de/climate_environment/CDC/observations_global/CLIMAT/monthly/qc/air_temperature_absolute_max/recent/83423.txt"
    city_name = "Goiania"
    histflivefunc.getdata(urlhist, urlrec, urlstation, db_name, table_name, city_name)
    """
    urlhist = "https://opendata.dwd.de/climate_environment/CDC/observations_global/CLIMAT/monthly/qc/air_temperature_absolute_max/historical/89054_199905_201503.txt"
    urlrec = "https://opendata.dwd.de/climate_environment/CDC/observations_global/CLIMAT/monthly/qc/air_temperature_absolute_max/recent/89054.txt"
    city_name = "Troll"
    histflivefunc.getdata(urlhist, urlrec, urlstation, db_name, table_name, city_name)
    """
    urlhist =  "https://opendata.dwd.de/climate_environment/CDC/observations_global/CLIMAT/monthly/qc/air_temperature_absolute_max/historical/10865_200201_202212.txt"
    urlrec =  "https://opendata.dwd.de/climate_environment/CDC/observations_global/CLIMAT/monthly/qc/air_temperature_absolute_max/recent/10865.txt"
    city_name = "München"
    histflivefunc.getdata(urlhist, urlrec, urlstation, db_name, table_name, city_name)

    urlhist = "https://opendata.dwd.de/climate_environment/CDC/observations_global/CLIMAT/monthly/qc/air_temperature_absolute_max/historical/10453_199901_202212.txt"
    urlrec = "https://opendata.dwd.de/climate_environment/CDC/observations_global/CLIMAT/monthly/qc/air_temperature_absolute_max/recent/10453.txt"
    city_name = "Brocken"
    histflivefunc.getdata(urlhist, urlrec, urlstation, db_name, table_name, city_name)

    urlhist = "https://opendata.dwd.de/climate_environment/CDC/observations_global/CLIMAT/monthly/qc/air_temperature_absolute_max/historical/10142_200309_202212.txt"
    urlrec = "https://opendata.dwd.de/climate_environment/CDC/observations_global/CLIMAT/monthly/qc/air_temperature_absolute_max/recent/10142.txt"
    city_name = "Itzehoe"
    histflivefunc.getdata(urlhist, urlrec, urlstation, db_name, table_name, city_name)

#---------------------------------------------------------------------------------------------------------------------------------------------------------#
"""
    table_name = "Lufttemp_abs_min"
    #47184
    urlhist =  "https://opendata.dwd.de/climate_environment/CDC/observations_global/CLIMAT/monthly/qc/air_temperature_absolute_min/historical/47184_199901_202212.txt"
    urlrec =  ""
    city_name = "Jeju"
    histflivefunc.getdata(urlhist, urlrec, urlstation, db_name, table_name, city_name)
    #83423
    urlhist =  "https://opendata.dwd.de/climate_environment/CDC/observations_global/CLIMAT/monthly/qc/air_temperature_absolute_min/historical/83423_201207_202212.txt"
    urlrec =  ""
    city_name = "Goiania"
    histflivefunc.getdata(urlhist, urlrec, urlstation, db_name, table_name, city_name)

    #89054
    urlhist = "https://opendata.dwd.de/climate_environment/CDC/observations_global/CLIMAT/monthly/qc/air_temperature_absolute_min/historical/89054_199905_201503.txt"
    urlrec = ""
    city_name = "Troll"
    histflivefunc.getdata(urlhist, urlrec, urlstation, db_name, table_name, city_name)

    #10865
    urlhist =  "https://opendata.dwd.de/climate_environment/CDC/observations_global/CLIMAT/monthly/qc/air_temperature_absolute_min/historical/10865_200201_202212.txt"
    urlrec =  ""
    city_name = "München"
    histflivefunc.getdata(urlhist, urlrec, urlstation, db_name, table_name, city_name)
    #10453
    urlhist = "https://opendata.dwd.de/climate_environment/CDC/observations_global/CLIMAT/monthly/qc/air_temperature_absolute_min/historical/10453_199901_202212.txt"
    urlrec = ""
    city_name = "Brocken"
    histflivefunc.getdata(urlhist, urlrec, urlstation, db_name, table_name, city_name)

    #10142
    urlhist = "https://opendata.dwd.de/climate_environment/CDC/observations_global/CLIMAT/monthly/qc/air_temperature_absolute_min/historical/10142_200309_202212.txt"
    urlrec = ""
    city_name = "Itzehoe"
    histflivefunc.getdata(urlhist, urlrec, urlstation, db_name, table_name, city_name)

#---------------------------------------------------------------------------------------------------------------------------------------------------------#

    table_name = "Lufttemp_daily_mean_max"

    # 47184
    urlhist = ""
    urlrec = ""
    city_name = "Jeju"
    histflivefunc.getdata(urlhist, urlrec, urlstation, db_name, table_name, city_name)
    # 83423
    urlhist = ""
    urlrec = ""
    city_name = "Goiania"
    histflivefunc.getdata(urlhist, urlrec, urlstation, db_name, table_name, city_name)

    #89054
    urlhist = ""
    urlrec = ""
    city_name = "Troll"
    histflivefunc.getdata(urlhist, urlrec, urlstation, db_name, table_name, city_name)
    # 10865
    urlhist = ""
    urlrec = ""
    city_name = "München"
    histflivefunc.getdata(urlhist, urlrec, urlstation, db_name, table_name, city_name)
    # 10453
    urlhist = ""
    urlrec = ""
    city_name = "Brocken"
    histflivefunc.getdata(urlhist, urlrec, urlstation, db_name, table_name, city_name)

    # 10142
    urlhist = ""
    urlrec = "lobal/CLIMAT/monthly/qc/sunshine_duration/recent/10142.txt"
    city_name = "Itzehoe"
    histflivefunc.getdata(urlhist, urlrec, urlstation, db_name, table_name, city_name)

    #---------------------------------------------------------------------------------------------------------------------------------------------------------#

    table_name = "Lufttemp_daily_mean_min"

    # 47184
    urlhist = ""
    urlrec = ""
    city_name = "Jeju"
    histflivefunc.getdata(urlhist, urlrec, urlstation, db_name, table_name, city_name)
    # 83423
    urlhist = ""
    urlrec = ""
    city_name = "Goiania"
    histflivefunc.getdata(urlhist, urlrec, urlstation, db_name, table_name, city_name)

    #89054
    urlhist = ""
    urlrec = ""
    city_name = "Troll"
    histflivefunc.getdata(urlhist, urlrec, urlstation, db_name, table_name, city_name)

    # 10865
    urlhist = ""
    urlrec = ""
    city_name = "München"
    histflivefunc.getdata(urlhist, urlrec, urlstation, db_name, table_name, city_name)
    # 10453
    urlhist = ""
    urlrec = ""
    city_name = "Brocken"
    histflivefunc.getdata(urlhist, urlrec, urlstation, db_name, table_name, city_name)

    # 10142
    urlhist = ""
    urlrec = ""
    city_name = "Itzehoe"
    histflivefunc.getdata(urlhist, urlrec, urlstation, db_name, table_name, city_name)

"""