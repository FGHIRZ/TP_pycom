import socket
import time
import pycom

#Importer libraires dans lib
from pysense import Pysense #Librairie de la carte pysense
from LIS2HH12 import LIS2HH12 #librairie de l'Accelerometre
from SI7006A20 import SI7006A20 #libraire du capteur d'humidité et de température
from LTR329ALS01 import LTR329ALS01 #librairie du capteur de lumière
from MPL3115A2 import MPL3115A2, ALTITUDE, PRESSURE #librairie du capteur d'altitude et de pression
from network import LoRa

#Création des objets associés aux capteurs
py = Pysense()
si = SI7006A20(py)  #contient les attributs : .humiditiy() et .temperature()
lt = LTR329ALS01(py) #contient l'attribut : .light()
li = LIS2HH12(py) #contient les attributs : .acceleration(), .roll() et .pitch()

# Désactiver le clignotement de la LED
pycom.heartbeat(False)

lora = LoRa(mode=LoRa.LORA, frequency=863000000, region=LoRa.EU868)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False)

print('Initialisation de la carte')

#Changement de couleur de la LED 00 14 00 étant pour 0 Rouge, 14 Vert et 0 Bleu
pycom.rgbled(0x001400)

#Boucle principale
while True:

    #Led Rouge
    pycom.rgbled(0x140000)

    message_envoye = ""
    #Envoyer les données de l'accélérometre
    print('Envoi des données de l"accélérometre : ')

    #On construit le message a envoyer
    message_envoye = 'Acc : ' + str(li.acceleration())

    #On envoie le message
    s.send(message_envoye)

    #On laisse du temps a l'antenne pour envoyer le message ( débit lent )
    time.sleep(10)

    #Envoyer les données de Roll
    print('Envoi des données de Roll : ')
    message_envoye = 'Roll : ' + str(li.roll())
    s.send(message_envoye)
    time.sleep(10)

    #Envoyer les données de Pitch
    print('Envoi des données de pitch : ')
    message_envoye = 'Pitch : ' + str(li.pitch())
    s.send(message_envoye)
    time.sleep(10)

    #A faire : Envoyer les données de luminosité, d'humidité et de Température des capteurs SI7006A20 et LTR329ALS01
    #...
    #..
