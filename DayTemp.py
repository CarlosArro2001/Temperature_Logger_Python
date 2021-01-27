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
        print(temp_Dic["temp"]) #NameError : name 'temp_Dic' is not defined 
    def setTemperatures(self):
        print("Setting 'n' amount of temperatures")
    def getHighTemp(self):
        print("Getting High Temp")
    def getLowTemp(self):
        print("Getting Low Temp")
    def getAvgTemp(self):
        print("Getting Average Temp")