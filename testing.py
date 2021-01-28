import csv 
with open("DayTemp.csv","r") as csvfile:
    reader = csv.reader(csvfile)
    lines = len(list(reader))
    print(lines-1)