from datetime import datetime
import psycopg2

tijd = str(datetime.now())
tijd = tijd[0:19]

modmail = "JORN.BOS@STUDENT.HU.NL"
modnaam = "JORN BOS"


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
r = open("resultaat.csv", "r")
berichten = r.readlines()
r.close

modnaam = input("Wat is uw naam?: ")
if modnaam.lower() != "jorn bos":
      print(exit("Dit is geen geldige naam."))
modmail = input("Wat is uw mail?: ")
if  modmail.lower() != "jorn.bos@student.hu.nl":
    print(exit("Dit is geen geldige mailadres"))   

for x in berichten:
    bericht = x.strip("\n").split(";")
    print(f"\nNaam: {bericht[0]} \nBericht: {bericht[1]}\n")
    
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
    
con.commit()

leeg = open("resultaat.csv", "w")
leeg.truncate(0)
leeg.close()


