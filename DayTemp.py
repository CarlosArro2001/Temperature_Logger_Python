import csv 
class DayTemp():
    #creating a global variable for the filename to allow access to all functions 
    global file
    #csv file which will be accessed to all functions 
    file = "DayTemp.csv" 

    #getter function that gets all the of the csvfile 
    def getTemperatures(self):
        rows = [] #this is where the values will be stored such that : [[<Date>,<Temperature]]
        with open(file,'r') as csvfile: 
            #using csv reader to append to the "rows" list 
            csvreader=csv.reader(csvfile)
            for row in csvreader:
                rows.append(row)
            #print statement to allow a better view of the data (kinda like a table)
            print(" Date\t   Temperature(celsius)")
            #variables for the loop 
            l = len(rows)
            i = 0 
            #using while loop to output the values
            while(i != l):
                print("{0} : {1}".format(rows[i][0],rows[i][1]))
                i = i + 1
            

    def setTemperatures(self):
        print("Setting 'n' amount of temperatures")
    def getHighTemp(self):
        print("Getting High Temp")
    def getLowTemp(self):
        print("Getting Low Temp")
    def getAvgTemp(self):
        print("Getting Average Temp")