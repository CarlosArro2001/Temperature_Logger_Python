import csv
class NightTemp():
    global file 
    file = "NightTemp.csv"
    def getTemperatures(self):
        rows = []
        with open(file,'r') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                rows.append(row)
            print(" Date\t   Temperature(celsius)")
            l=len(rows)
            i=0
            while(i != l):
                print("{0} : {1}".format(rows[i][0],rows[i][1]))
                i = i + 1

    def setTemperatures(self):
        print("Setting Temperatures")
    def getHighTemp(self):
        print("Getting High Temp")
    def getLowTemp(self):
        print("Getting Low Temp")
    def getAvgTemp(self):
        print("Getting Average Temp")