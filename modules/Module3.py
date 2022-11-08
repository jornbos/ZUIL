#####IMPORTS
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from cProfile import label
from email.mime import image
from inspect import FullArgSpec
from tkinter import *
from xml.dom.xmlbuilder import DOMBuilderFilter
from xmlrpc.client import boolean
import psycopg2
import random
from urllib.request import *
import requests


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
####VARIABELEN ETC
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#kleuren:
nsgeel = "#FFC917"
nsblauw = "#003072"
nsknop = "#0063D23"

#font
nsfont= "NS sans regular"




#STATIONS (RANDOM)
s = open("stations.txt", "r").readlines()
station = str(random.choice(s)).strip("\n")

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
###TKINTER
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#main
zuil = Tk()
#De naam van het document wat linksbovenstaan
zuil.title("Stationscherm")
#logo van applicatie
zuil.iconbitmap("ns-logo.ico")
#achtergrondkleur
zuil.configure(background=nsgeel)
#Afbeelding NS LOGO
IMGNS = PhotoImage(file='NSLOGO.png')





#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
###DATABASE
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#verbinden met DB
con = psycopg2.connect( 
#inloggegevens:
           host = "localhost",
           database = "ZUIL",
           user = "postgres",
           password = "Jorn2003",
           port = 5432          )


#cursor
cur = con.cursor()

#Berichten ophalen op aflopende volgorde (dus nieuwste)
DBinfo = "SELECT bericht FROM bericht ORDER BY goedgekeurd_tijd DESC"
cur.execute(DBinfo)
DBinfo = cur.fetchmany(10)

#de berichten in een simpeler variabel
bericht1 = DBinfo[0][0]
bericht2 = DBinfo[1][0]
bericht3 = DBinfo[2][0]
bericht4 = DBinfo[3][0]
bericht5 = DBinfo[4][0]

def ov_fiets(station):
        DBFiets = f"SELECT ovfietsinfo FROM station where stationnaam = '{station}'"
        cur.execute(DBFiets)
        fiets = cur.fetchall()
        fiets = fiets[0][0]
        if fiets == "ja":
               IMGFIETS = PhotoImage(file='img_ovfiets.png')
               return IMGFIETS
        elif fiets == "nee":
                IMGFIETS = PhotoImage(file='img_ovfietsnee.png') 
                return IMGFIETS

fotofiets = ov_fiets(station)

def lift(station):
        DBlift = f"SELECT liftinfo FROM station where stationnaam = '{station}'"
        cur.execute(DBlift)
        fiets = cur.fetchall()
        fiets = fiets[0][0]
        if fiets == "ja":
               IMGLIFT = PhotoImage(file='img_lift.png')
               return IMGLIFT
        elif fiets == "nee":
                IMGLIFT = PhotoImage(file='img_liftnee.png') 
                return IMGLIFT

fotolift = lift(station)


def toilet(station):
        DBtoilet = f"SELECT toiletinfo FROM station where stationnaam = '{station}'"
        cur.execute(DBtoilet)
        toilet = cur.fetchmany(1)
        toilet = toilet[0][0]
        if toilet == "ja":
                IMGTOILET = PhotoImage(file='img_toilet.png')
                return IMGTOILET
        elif toilet == "nee":
                IMGTOILET = PhotoImage(file='img_toiletnee.png') 
                return IMGTOILET

fototoilet = toilet(station)

def PR(stad):
        sqlcode = f"SELECT prinfo FROM station where stationnaam = '{stad}'"
        cur.execute(sqlcode)
        pr = cur.fetchmany(1)
        pr = pr[0][0]
        if pr == "ja":
             IMGPR = PhotoImage(file='img_pr.png')
             return IMGPR
        elif pr == "nee":
                IMGPR = PhotoImage(file='img_prnee.png')    
                return IMGPR

fotopr = PR(station)

con.commit


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#####API
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#api url
url_request = "https://api.openweathermap.org/data/2.5/weather?q={}&lang=nl&appid={}&lang={}"
#api key
api_key = "e802453a337a8aef378c3480e2fc4757"
#taal
lang = "NL"

def get_weather(city):
        #zet de stad (station.txt resultaat), apikey en taal in de url_request
    result = requests.get(url_request.format(city, api_key,lang))
    if result:
        json = result.json()
        #(stad, land, temp_celcius, temp_fahrenheit, icoon, weer)
        city = json['name']
        country = json['sys']['country']
        temp_kelvin = json['main']['temp']
        temp_celsius = temp_kelvin - 273.15
        icon = json['weather'][0]['icon']
        weather = json['weather'][0]['description']
        final = (city, country, temp_celsius, icon, weather)
        return final
    else:
        return None







#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#######Labels
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#blauwe balk:

kleur = Label(master=zuil,
        background=nsblauw,
        width=300,
        height=15

)
##Station en station naam van stations.txt (random)
stations = Label(master=zuil,
        text=f"Station {station}",
        background=nsblauw,
        foreground=nsgeel,
        font=(nsfont, 48, "bold"),
        #width=5,
        height=3)


#Logo NS
nslogo = Label(master=zuil, 
        image=IMGNS, 
        foreground=nsblauw,
        background=nsgeel,
        height=227)


#de tekst die boven de berichten staat ( apart zodat tekst dikgedrukt kan zijn)        
berichttitel = Label(master=zuil,
        text="    Laatste 5 berichten",
        font=(nsfont, 24, "bold"),
        background="white" ,
        foreground=nsblauw,
        borderwidth=2,
        relief="solid",
        width=101,
        height=5
)
#de 5 berichten van gebruikers (goedgekeurd door moderator in module2)
bericht = Label(master=zuil,
        text=f"1. {bericht1}\n\n2. {bericht2}\n\n3. {bericht3}\n\n4. {bericht4}\n\n5. {bericht5}",
        font=(nsfont, 16),
        background="white" ,
        foreground=nsblauw,
        borderwidth=2,
        relief="solid",
        #width=103,
        width=160,
        height=10
)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
### FOTOS OV FIETS, LIFT, PR, TOILET
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

fotoovfiets = Label(master=zuil,  
        image=fotofiets, 
        foreground=nsblauw,
        background=nsgeel,)
        #height=227)
fotoelevator = Label(master=zuil,  
        image=fotolift, 
        foreground=nsblauw,
        background=nsgeel,)
        #height=227)
fotowc = Label(master=zuil,  
        image=fototoilet, 
        foreground=nsblauw,
        background=nsgeel,)
        #height=227)
fotoparkride = Label(master=zuil,  
        image=fotopr, 
        foreground=nsblauw,
        background=nsgeel,)
        #height=227)






fotoovfiets.place(x=1460,y=690)
fotoelevator.place(x=1600,y=690)
fotowc.place(x=1460,y=830)
fotoparkride.place(x=1600,y=830)






#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
####WEERLABELS EN FORMAAT
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Locatie:
locatielabel = Label(master=zuil,
                text='',
                font=(nsfont, 32, "bold"),
                foreground=nsblauw,
                background=nsgeel
)
#Tempratuur:
tempratuurlabel = Label(master=zuil,
                text='',
                font=(nsfont, 32),
                foreground=nsblauw,
                background=nsgeel
)
#Het daadwerkelijke weer, bijv; bewolkt:
weerlabel = Label(master=zuil,
                text='',
                font=(nsfont, 32),
                foreground=nsblauw,
                background=nsgeel
                
              
)
print(station)
#weerformaat
if station == "Den Bosch":
        weer = get_weather("Den Bosch")
if station == "Almere":
        weer = get_weather("Almere")
else:
        weer = get_weather(station)

if weer:
#locatielabel = city, country (dus bijvoorbeeld: Amsterdam, NL)
    locatielabel['text'] = '{}, {}'.format(weer[0], weer[1])
#tempratuurlabel = temp_celcius zonder getallen achter de komma (dus bijvoorbeeld: 13C)
    tempratuurlabel['text'] = '{:.0f}°C'.format(weer[2])
#weerlabel = weather (bijvoorbeeld: bewolkt)
    weerlabel['text'] = weer[4]



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
####PLAATSTEN VAN ALLE WIDGETS/LABELS
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
kleur.place(x=0,y=0)
nslogo.place(x=800, y=700)
stations.place(x=750, y=10)
berichttitel.place(x=0,y=190)
bericht.place(x=0,y=356)
locatielabel.place(x=210,y=730)
tempratuurlabel.place(x=210,y=790)
weerlabel.place(x=210,y=850)



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
####GROOTTE SCHERM EN MAINLOOP
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#grootte scherm
zuil.geometry("1920x1080")
#zuil.attributes("-fullscreen", True)
#mainloop
zuil.mainloop()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
