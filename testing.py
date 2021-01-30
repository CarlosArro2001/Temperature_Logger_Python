import csv
global file 
file = "DayTemp.csv"
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
    print(avg)
csvfile.close()
