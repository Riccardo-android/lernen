import histflivefunc
import sqldatadef


urlstation = "https://www.dwd.de/DE/leistungen/klimadatenweltweit/stationsverzeichnis.html?lsbId=374532"
db_name = "hist_climate_global"
table_name = "temp"


urlhist =  "https://opendata.dwd.de/climate_environment/CDC/observations_global/CLIMAT/monthly/qc/air_temperature_mean/historical/47184_198901_202212.txt"
urlrec =  "https://opendata.dwd.de/climate_environment/CDC/observations_global/CLIMAT/monthly/qc/air_temperature_mean/recent/47184.txt"
city_name = "Jeju"
histflivefunc.getdata(urlhist, urlrec, urlstation, db_name, table_name, city_name)

#89504 nicht - Troll, Norwegen
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

