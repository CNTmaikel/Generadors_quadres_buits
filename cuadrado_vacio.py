import time
import os
from tqdm.auto import tqdm

os.system("clear")

print("")
print("------------------------Generador de quadres buits------------------------")
print("")
print("Hola, benvingut al programa de creació de quadres buits :D")
print("")
print("--------------------------------Instruccions--------------------------------")
print("Hauràs d'introduir un valor per l'altura i la llargada del quadre")
print("IMPORTANT tingues en compte no posar ningun caracter que no sigui un nombre")
print("En aquest cas el prgrama fallara i s'haurà de reiniciar")
print("")
print("--------------------------------Instruccions--------------------------------")
print("")
print("Perfavor, premeu intro per continuar")
print("")
input("------------------------Generador de quadres buits------------------------")
os.system("clear")

def programa():
    altura = int(input("--> Defineix l'altura: "))
    ancho = int(input("--> Defineix la llargada: "))
    inici = time.time()

    print("")

    for i in range(0, altura+1):
        for j in range(0, ancho+1):
            if i == 0 or i == altura:
                print(" * ", end="")
            else:
                if j == 0 or j == ancho:
                    print(" * ", end="")
                else:
                    print("   ", end="")
        print("")
    
    print("")

    time.sleep(0)
    fin = time.time()   
    tiempo = fin - inici 

    print("CONSTRUIT SATISFACTORIAMENT", "(""temps total:", tiempo,"sec"")")
    
    def reinicio():
        reiniciar = input("Desitja continuar? [Y/n]: ")
        if reiniciar == "Y":
            os.system("clear")
            programa()
        elif reiniciar == "y":
            os.system("clear")
            programa()
        elif reiniciar == "n":
            print("")
            print("Moltes gràcies per utilitzar aquest programa!")
            print("© 2023-2023 Miquel Estruch. All rights reserved")
            exit()
        else:
            print("No t'he entès.")
            reinicio()
    reinicio()



programa()
