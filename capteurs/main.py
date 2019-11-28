import socket
import time
import pycom

#Importer libraires dans lib
from pysense import Pysense #Librairie de la carte pysense
from LIS2HH12 import LIS2HH12 #librairie de l'Accelerometre
from SI7006A20 import SI7006A20 #libraire du capteur d'humidité et de température
from LTR329ALS01 import LTR329ALS01 #librairie du capteur de lumière
from MPL3115A2 import MPL3115A2, ALTITUDE, PRESSURE #librairie du capteur d'altitude et de pression


#Création des objets associés aux capteurs
py = Pysense()
si = SI7006A20(py)  #contient les attributs : .humiditiy() et .temperature()
lt = LTR329ALS01(py) #contient l'attribut : .light()
li = LIS2HH12(py) #contient les attributs : .acceleration(), .roll() et .pitch()

# Désactiver le clignotement de la LED
pycom.heartbeat(False)


print('Initialisation de la carte')

#Changement de couleur de la LED 00 14 00 étant pour 0 Rouge, 14 Vert et 0 Bleu
pycom.rgbled(0x001400)

#Boucle principale
while True:

    #Led Rouge
    pycom.rgbled(0x000014)

    #Afficher les données d'accélérometre
    print('Données accélérometre : ')
    print('Acceleration', li.acceleration())
    print('Roll', li.roll())
    print('Pitch', li.pitch())

    #A faire : afficher les données de luminosité, d'humidité et de Température des capteurs SI7006A20 et LTR329ALS01
    #...
    #...


    #Passage du capteur de pression en mode pression
    mpPress = MPL3115A2(py,mode=PRESSURE)
    print('Données Baromètre')
    print('Pressure (hPa)', mpPress.pressure()/100)

    #Passage du capteur de pression en mode Altitude + Température
    mpAlt = MPL3115A2(py,mode=ALTITUDE)
    print('Altitude', mpAlt.altitude())
    print('Temperature', mpAlt.temperature())

    #LED Verte
    pycom.rgbled(0x001400)

    #attendre 30 secondes avant prochaine lecture
    time.sleep(30)
