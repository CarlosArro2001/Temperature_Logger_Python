import csv 
class DayTemp():
    global file 
    file = "DayTemp.csv"
    global temp_Dic 
    temp_Dic = {
        "Date":["01/02/2021","01/03/2021","01/04/2021"],
        "Temp":[20,21,23]
    }
    def getTemperatures(self):
        fields = []
        rows = []
        with open(file,'r') as csvfile:
            csvreader=csv.reader(csvfile)
            fields = next(csvreader)
            for row in csvreader:
                rows.append(row)
            print("Total no. of rows: %d"%(csvreader.line_num))
            print('Field Names are :' + ",".join(field for field in fields))
            print("\n First 5 rows are : \n")
            reader = csv.reader(csvfile)
            lines = len(rows)
            '''
            for row in rows[:lines]:
                for col in row:
                    print("%10s"%col),
                print('\n')
            '''
    def setTemperatures(self):
        print("Setting 'n' amount of temperatures")
    def getHighTemp(self):
        print("Getting High Temp")
    def getLowTemp(self):
        print("Getting Low Temp")
    def getAvgTemp(self):
        print("Getting Average Temp")