import sys 
from DayTemp import DayTemp
from NightTemp import NightTemp

class TempLog(DayTemp,NightTemp):    
    #main menu method , this will be what the user will see first when they first start up the program
    def mainmenu():
        print("\t Temperature Logger - version 1.0 \t ")
        print("\t Main Menu")
        print("\t Please choose one of the following : \n ")
        print("\t Get day temperatures , enter :  1  ")
        print("\t Get night temperatures , enter :  2  ")
        print("\t Set day temperatures , enter :  3  ")
        print("\t Set night temperatures , enter :  4  ")
        print("\t Get highest day temperature , enter :  5  ")
        print("\t Get highest night temperature , enter :  6  ")
        print("\t Get lowest day temperature , enter :  7  ")
        print("\t Get lowest night temperature , enter :  8  ")
        print("\t Get average day temperature , enter :  9  ")
        print("\t Get average night temperature , enter :  10  ")
        print("\t To exit program , enter : 11")
    #below refers to the input of the user , as long as the user doesn't input the value of 11 (which closes the program via sys.exit() function)
    #need to work on error handling for the the input of invalid values , as when the input is a non-integer value 
    #the program will just stop 
        choice = 0
        n = NightTemp()
        d = DayTemp()        
        while(choice != 11):
            print("Enter here : ")
            choice = int(input())
            if(choice == 1):
                d.getTemperatures()
            elif(choice == 2):
                n.getTemperatures()
            elif(choice == 3):
                print("Enter amount of temperatures recorded")
                n = int(input())
                d.setTemperatures(n)
            elif(choice == 4):
                n.getTemperatures()
            elif(choice == 5):
                d.getHighTemp()
            elif(choice == 6):
                n.getHighTemp()
            elif(choice == 7):
                d.getLowTemp()
            elif(choice == 8):
                n.getLowTemp()
            elif(choice == 9):
                d.getAvgTemp()
            elif(choice == 10):
                n.getAvgTemp()
            elif(choice == 11):
                print("Exiting Program")
                sys.exit()
            else:
                print("Invalid Input")
    mainmenu()
    