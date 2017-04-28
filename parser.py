import csv
def writeFile(filename,aList):
    with open(filename, 'w', newline='') as huh:
        spamwriter = csv.writer(huh, delimiter=',')
        spamwriter.writerow(["tripDistance","pickupLong","pickupLat","dropoffLong","dropoffLat","Fare"])
        for row in aList:
            spamwriter.writerow(row)

Sunday = [3,10,17,24,31]
Monday = [4,11,18,25]
Tuesday = [5,12,19,26]
Wednesday = [6,13,20,27]
Thursday = [7,14,21,28]
Friday = [1,8,15,22,29]
Saturday = [2,9,16,23,30]

Days=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

numToDay ={}
for i in Sunday:
    numToDay[i]="Sunday"
for i in Monday:
    numToDay[i]="Monday"
for i in Tuesday:
    numToDay[i]="Tuesday"
for i in Wednesday:
    numToDay[i]="Wednesday"
for i in Thursday:
    numToDay[i]="Thursday"
for i in Friday:
    numToDay[i]="Friday"
for i in Saturday:
    numToDay[i]="Saturday"
wholeDict={}
for day in Days:
    wholeDict[day] = {}
    for j in range(0,24):
        wholeDict[day][j]=[]

aList=[]
with open("subset.csv",'r', newline="") as csvfile:
    well = csv.reader(csvfile)
    for read in well:
        try:
            day = numToDay[int(read[2][8:10])]
            time = int(read[2][11:13])
            theList = [read[5],read[6],read[7],read[10],read[11],read[13]]
            wholeDict[day][time].append(theList)
        except:
            print("error")
for day in Days:
    for i in range(0,24):
        writeFile(day+str(i)+".csv", wholeDict[day][i])
