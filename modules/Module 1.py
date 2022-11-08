#importeert random en datetime zodat we de random.choice funcite kunnen gebruiken en zodat we de tijd kunnen oproepen met datetime.now()
from datetime import datetime
import random
#lijn is omdat ik lui ben n ook
lijn = "------------------------------------"
#datetime.now laat de tijd zien.
tijd = str(datetime.now())
n = "\n"
komma = ";"

#deze input vraagt of de gebruiker hem anoniem wilt invullen en gaat daarna naar de if statements
anoniem = input(str(lijn + n  + "Wilt u deze vragen anoniem beantworden of niet? (ja/nee): "))
#de volgende 3 lijnen laten lezen het stations.txt bestand en kiest een random station uit en zet het daarna in de variable locatie
s = open("stations.txt", "r").readlines()
locatie = str(random.choice(s))



#dit is de if statement als het anoniem word ingevuld
if anoniem.upper() == "JA":
#naam word automatisch "Anoniem ingevuld"
    naam = "anoniem"
    #dit vraagt het bericht van de gebruiker
    bericht = input(str(lijn + n + "Wat is het bericht wat u achter wilt laten?: "))
    #mocht het bericht langer zijn dan 140 karakters dan krijgt de gebruiker een error 
    if len(bericht) > 140:
        print(exit("Dit bericht heeft meer dan 140 karakters"))
    

#hier word het antwoord van anoniem automatisch hoofdletter gemaakt
elif anoniem.upper() == 'NEE':
    #hier word de naam als input gevraagd omdat de gebruiker niet anoniem wilt invullen
    naam = input(str(lijn + n + "Wat is uw naam?: "))
    #hier word het bericht als input gevraagd van de gebruiker
    bericht = input(str(lijn + n + "Wat is het bericht wat u achter wilt laten?: "))
    #mocht het bericht langer zijn dan 140 karakters dan krijgt de gebruiker een error 
    if len(bericht) > 140:
        print(exit("Dit bericht heeft meer dan 140 karakters"))

#als het antwoord niet ja of nee is dan krijgt de gebruiker een error
else:
    print("Dat is geen geldig antwoord, kies uit ja of nee.")

#hier word de opmaak van het tekst bestand gedaan

#de [0:19] is zodat de milliseconds er niet bij komen.
tijda = tijd[0:19]
nnaam = str(naam)
antwoord = f"{nnaam};{bericht};{tijda};{locatie}"
r = open('bericht.csv', "a")
r.write(antwoord)
r.close
