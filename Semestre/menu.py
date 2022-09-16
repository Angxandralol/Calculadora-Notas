import os 
from Semestre.semestre import Semestre

def menuSemestre():
    opcion = 1
    while(opcion!=0):
        os.system("cls")
        print("SECCION: Nuevo Semestre\n")
        print("OPCIONES:\n")
        print("1) Crear Nuevo Semestre\n")
        print("0) SALIR\n")
        opcion = int(input())

        if (opcion == 1):
            os.system("cls")
            print("Numero de Semestre: ")
            numeroSemestre = int(input())
            semestre = Semestre(numeroSemestre)
            semestre.inscripcionMateria()
            semestre.getMaterias()

        