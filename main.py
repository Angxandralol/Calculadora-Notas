import os 
from Semestre.menu import menuSemestre

opcion = 1
while(opcion!=0):
    os.system("cls")
    print("Bienvenido a la Calculadora de Notas\n")
    print("OPCIONES:\n")
    print("1) Nuevo Semestre\n")
    print("2) Visualizar Semestre\n")
    print("0) SALIR\n")
    opcion = int(input())

    if (opcion == 1):
        menuSemestre()
    