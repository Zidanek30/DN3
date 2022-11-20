from datetime import datetime, timedelta

def emso_leta_preracun():
    emso = input("Vnesi svoj EMSO: ")

    emso = emso.strip()   
    
    if emso.isnumeric():    
       pass                 
    else:
        print("Error\nYou enetered a character")
        exit()            

    
    BirthYear = emso[4:7]         
    if BirthYear[0] == '9':      
        BirthYear = '1' + BirthYear    
    else:
        BirthYear = '2' + BirthYear     

    BirthMonth = emso[2:4]              
    BirthDay = emso[0:2]               
    date = datetime(year=int(BirthYear), month=int(BirthMonth), day=int(BirthDay))  

    Birthdate = datetime(year=int(BirthYear), month=int(BirthMonth), day=int(BirthDay))

    today = date.today()            
    year = today.strftime("%Y")     

    
    if today > datetime(year=int(year), month=int(BirthMonth), day=int(BirthDay)):  
        hadBD = 1    
    else:
        hadBD = 0

    
    if hadBD == 1:
        print("Stari ste " + str(int(year) - int(BirthYear)) + " let")
    else:
        print("Stari ste " + str(int(year) - int(BirthYear) - 1) + " let")


emso_leta_preracun()