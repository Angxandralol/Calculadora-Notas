from typing import List
import os
from Materias.materias import Materia

class Semestre():
    numero: int
    materias = []

    def __init__(self, numero):
        self.numero = numero

    def nuevaMateria(self):
        print("Nombre de la Materia Inscrita: ")
        nombreMateria = input()
        materia = Materia(nombreMateria)
        return materia
    
    def añadirMateria(self, materia):
        self.materias.append(materia)

    def inscripcionMateria(self):
        opcion = 1
        while(opcion == 1):
            materia = self.nuevaMateria()
            self.añadirMateria(materia)
            print("¿Desea inscribir otra materia? (Si=1 / No=0)")
            opcion = int(input())
            print("\n")

    def getMaterias(self):
        os.system("cls")
        print("MATERIAS INSCRITAS EN EL SEMESTRE", self.numero,":")
        for materia in self.materias:
            print(materia.nombre)
        input()