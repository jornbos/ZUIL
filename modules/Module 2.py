from datetime import datetime #importeert de tijd

import psycopg2  #importeert de postgres integratie tool

tijd = str(datetime.now())
tijd = tijd[0:19] #verwijderd de miliseconden van de tijd


#Inloggegevens:
modmail = "JORN.BOS@STUDENT.HU.NL"
modnaam = "JORN BOS"

#Opent resultaat.csv met schrijf rechten
r = open("resultaat.csv", "r")
bericht = r.readline()
r.close

#inloggegevenves database
connection_string = "host='localhost' dbname='ZUIL' user='postgres' password='Jorn2003'"



vraagmail = input(str("Wat is uw mail adres?: "))
if vraagmail.upper() != modmail:
    print("Dit is geen geldig moderator mail adres.")

else:
    vraagnaam = input(str("Wat is uw naam?: "))
    if vraagnaam.upper() != modnaam:
        print("Dit is geen geldige moderator naam.")
    
    else: 
        print("\n" + str(bericht) + "\n")
        keuring = input(str("Keurt u dit bericht goed? (ja/nee): "))
        while True:
            if keuring.upper() == "NEE":
                bericht = next(r)
                print("\n" + bericht + "\n")
                keuring = input(str("Keurt u dit bericht goed? (ja/nee): "))

            elif keuring.upper() == "JA":
                r = open("goedgekeurd.csv", "a")
                r.write(f"{bericht};{modnaam};{modmail}{tijd}")
                r.close
                break
               

        


            


