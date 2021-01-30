import csv 
class DayTemp():
    #creating a global variable for the filename to allow access to all functions 
    global file
    #csv file which will be accessed to all functions 
    file = "DayTemp.csv" 

    #getter function that gets all the of the csvfile 
    def getTemperatures(self):
        with open(file,'r') as csvfile:
            reader = csv.reader(csvfile,delimiter=',')
            for row in reader:
                #checking if the row had a value or not because when you enter a new value it always makes a new line 
                if(not row):
                    continue
                else:
                    print(row) 

    #setter function for inputting into the DayTemp.csv file (file variable)         
    def setTemperatures(self,n):
        #two lists , whereby the new_values will consist of the date and the temperature 
        # and the new_records will consists of elements in the form of values from new_values as a list 
        new_records = [] # new_records = [[Date,Temp],[Date,Temp]]
        new_values = [] # new_values = [Date,Temp]
        i = 0
        while(i != n): #while loop to input 'n' amount of values
            Date = "" 
            Temp = ""
            #input of date and temp 
            print("Enter Date:")
            Date = str(input())
            print("Enter Temperature:")
            Temp = str(input())
            #storing date & temp into new_values list
            new_values.append(Date)
            new_values.append(Temp)
            #storing the newly appended values from new_values into new_records
            new_records.append(new_values)
            i = i+1
            #inputting the new_records elements into the file (DayTemp.csv)
            with open(file,'a') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerows(new_records)
                #output stating that the values are fully inputted into the csv file
                print("DayTemp file updated")
            #clearing for the next time the person wants to input new values in the csvfile
            new_records.clear()
            new_values.clear()
                
    def getHighTemp(self):
        rows = []
        with open(file,'r') as csvfile:
            reader = csv.reader(csvfile,delimiter =',')
            for row in reader:
                if(not row):
                    continue
                else:
                    rows.append(row)
            rows.remove(rows[0]) #removing the first element which is ['Date','Temperature']
            n = len(rows)
            for i in range(n):
                for j in range(0,n-i-1):
                    if(int(rows[j][1]) > int(rows[j+1][1])):
                        rows[j] , rows[j+1] = rows[j+1] , rows[j]
        print(rows)
        print("Highest Day Temp : {0} on {1}".format(rows[len(rows)-1][1],rows[len(rows)-1][0]))
    
    def getLowTemp(self):
        rows = []
        with open(file,'r') as csvfile:
            reader = csv.reader(csvfile,delimiter =',')
            for row in reader:
                if(not row):
                    continue
                else:
                    rows.append(row)
            rows.remove(rows[0]) #removing the first element which is ['Date','Temperature']
            n = len(rows)
            for i in range(n):
                for j in range(0,n-i-1):
                    if(int(rows[j][1]) > int(rows[j+1][1])):
                        rows[j] , rows[j+1] = rows[j+1] , rows[j]
        print("Lowest Day Temp : {0} on {1}".format(rows[0][1],rows[0][0]))
    def getAvgTemp(self):
        rows = []
        temperatures = []
        with open(file,'r') as csvfile:
            reader = csv.reader(csvfile,delimiter =',')
            for row in reader:
                if(not row):
                    continue
                else:
                    rows.append(row)
            rows.remove(rows[0]) #removing the first element which is ['Date','Temperature']
            i = 0
            while(i != len(rows)):
                temperatures.append(int(rows[i][1]))
                i = i + 1
            print(temperatures)
            avg = sum(temperatures)/len(temperatures)
            print("Average Day temperature :{0}".format(avg))