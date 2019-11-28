#!/usr/bin/env python
#
# Copyright (c) 2019, Pycom Limited.
#
# This software is licensed under the GNU GPL version 3 or any
# later version, with permitted additional terms. For more information
# see the Pycom Licence v1.0 document supplied with this file, or
# available at https://www.pycom.io/opensource/licensing
#

#Importer les librairies
from network import LoRa
import socket
import time


#Construire l'objet Lora
lora = LoRa(mode=LoRa.LORA, frequency=863000000, region=LoRa.EU868)

#Definir la socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False)

#Boucle principale
while True:
    #Envoyer "Hello" à travers la socket
    s.send('Hello')

    #Lire les messages reçus par la socket
    message_recu = s.recv(64)

    #Transformer le message en string
    msg = str(message_recu, 'utf-8')

    #Si message non null
    if len(msg)>0:

        #Afficher le message
        print(msg)

    #Attendre 5 secondes avant de réitérer la boucle
    time.sleep(5)
