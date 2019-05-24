# ######################
# 
# ######################
'''
Exercici 4
Representar en matplotlib una grafica de barres vertical de 10 minuts
'''

# Imports
from random import randint
from time import sleep
import matplotlib.pyplot as plt

# Definicio variables globals


# Definicio procediments auxiliars
def valor_fake():
    valor = randint(0,1)

def nom_arxiu():
    '''
    Genera un nom pseudoaleatori basat en el temps o no ....
    '''
    return nom_nou
    
def grafic1(llista1):
    minuts=[0,1,2,3,4,5,6,7,8,9]
    fig = plt.figure()
    plt.plot(llista1,minuts)
    plt.savefig('prova1.png', bbox_inches='tight')
    plt.close(fig)


# Bucle principal
llistapersones = []
minuts = 0

while minuts <10:
    persones = 0
    for segons in range(60):
        valor_actual = valor_fake()
        if valor_actual ==1:
            persones +=1
        sleep(1)
    llistapersones.append(persones)

grafic1(llistapersones)

        
