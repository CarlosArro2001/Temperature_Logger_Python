class DayTemp():
    temp_Dic = {
        "date" : ["01/01/2021","02/01/2021","03/01/2021"],
        "temp" : [17,18,19]
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