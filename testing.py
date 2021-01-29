import csv
first_list = []
second_list = []
second_list.append("1/4/2021")
second_list.append("23")
print(second_list)
first_list.append(second_list)
print(first_list)
global file
file = "DayTemp.csv"
with open(file,'a') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(first_list)
    print("CSV UDPATED")