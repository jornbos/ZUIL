from datetime import datetime
import psycopg2
import os

tijd = str(datetime.now())
tijd = tijd[0:19]

aantal = 0

#verbinden met DB
con = psycopg2.connect( 
           host = "localhost",
           database = "ZUIL",
           user = "postgres",
           password = "Jorn2003",
           port = 5432          )


#cursor
cur = con.cursor()

berichten = []
bericht = []
lijst_moderator = []

#opent het bestand met alle resultaten
r = open("bericht.csv", "r")
berichten = r.readlines()
r.close

#vraagt naar naam moderator
modnaam = input("Wat is uw naam?: ")

#als de naam niet gelijk is aan "jorn bos" stopt het programma
if modnaam.lower() != "jorn bos":
      print(exit("Dit is geen geldige naam."))

#vraagt naar naam moderator
modmail = input("Wat is uw mail?: ")

#als de naam niet gelijk is aan "jorn bos" stopt het programma
if  modmail.lower() != "jorn.bos@student.hu.nl":
    print(exit("Dit is geen geldige mailadres")) 

#hiermee kijkt python of het bestand waar het om gaat leeg is of niet, als het leeg is word het programma met het onderstaande bericht afgesloten
if os.path.getsize("bericht.csv") == 0:
    print(exit("Er zijn geen berichten.\nProgramma word afgesloten"))  

for x in berichten:
    bericht = x.strip("\n").split(";")
    print(f"\nNaam: {bericht[0]} \nBericht: {bericht[1]}\n")
    
    #vraagt of het bericht is goedgekeurd
    goedkeuring = input("Keurt u dit bericht goed?(ja/nee): ")
    
    if goedkeuring.upper() == "JA":
        goedgekeurd = 1
        
    if goedkeuring.upper() == "NEE":
        goedgekeurd = 0
    
    tijd = str(datetime.now())
    tijd = tijd[0:19]
    lijst_moderator = modnaam,modmail,tijd
    bericht.extend(lijst_moderator)
    sqlcode = "INSERT INTO bericht (naam, bericht, datum_tijd, stationnaam, goedgekeurd_door, Mailadres, goedgekeurd_tijd) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    if goedgekeurd == 1:
        cur.execute(sqlcode, bericht)
        aantal = aantal + 1
        print(f"Er zijn {aantal} goedgekeurde berichten toegevoegd aan de database.\nHet bericht.csv word nu geleegd!")
    
con.commit()


leeg = open("bericht.csv", "w")
leeg.truncate(0)
leeg.close()
