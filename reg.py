import csv
import datetime

def taxiFare(plon,plat,dlon,dlat,dist):
    dateNow = datetime.datetime.now()
    hour = dateNow.hour
    day = dateNow.weekday()
    index = 23*day+hour+1

    LM=[]
    with open("LM.csv") as csvfile:
        read = csv.reader(csvfile)
        for row in read:
            LM.append(row)
    Coef = LM[index]
    fare = float(Coef[0])+float(Coef[1])*dist+plon*float(Coef[2])+plat*float(Coef[3])+dlon*float(Coef[4])+dlat*float(Coef[5])
    return round(fare,2)
