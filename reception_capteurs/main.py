import socket
import time
import pycom
from network import LoRa

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

    #Reception du message
    message_recu = s.recv(128)
    message_recu = str(message_recu, 'utf-8')
    #Affichage du message
    if len(message_recu) > 0:
        print(message_recu)
    time.sleep(10)
