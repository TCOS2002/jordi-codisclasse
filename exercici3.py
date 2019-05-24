# #################################################################################################
#
#
# #################################################################################################

# Importacions
from random import randint
from time import sleep
# import cayenne.client

# Variables globals
# Cayenne authentication info. This should be obtained from the Cayenne Dashboard.
'''
fALTA ALTA A CAYENNE I CANVIAR ELS CODIS ....
MQTT_USERNAME = ""
MQTT_PASSWORD = ""
MQTT_CLIENT_ID = ""
client = cayenne.client.CayenneMQTTClient()
client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID)
'''

# Procediments auxiliars
def cayenne(valors):
    # Aquesta funcio retorna 0 o 1 segons si passa o no una persona.
    # Donem per suposat que en 1 sg SOLS pot passar una persona
    ''' 
    Procediment per enviar les dades a Cayenne 
    '''
    print(valors)

def distancia():
    # Aquesta funcio retorna de manera aleatoria un valor 0 o 1

    # definim:  random.randrange(start, stop[, step])
    # Definim per INTEGERS: random.randint(start,stop)
    dist1= randint(0,1) # de manera que ens retorni un valor que sigui 0 o 1
    return dist1


# Bucle principal

while True:
    #client.loop()
    persones = 0
    for segons in range(60):           # contarem fins a 60
        sleep(1)                               # esperem 1 segon
        persona = distancia()          # recuperem valor del sensor
        if persona == 1:                  # mirem si hi pasa algu i sumem en aquest cas
            persona +=1
            
    cayenne(persones)                  # Envia les dades a Cayenne, cada 60 segons
          
