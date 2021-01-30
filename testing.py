import csv
global file 
file = "DayTemp.csv"

rows = []
with open(file,'r') as csvfile:
    reader = csv.reader(csvfile,delimiter =',')
    for row in reader:
        if(not row):
            continue
        else:
            print(row)
csvfile.close()