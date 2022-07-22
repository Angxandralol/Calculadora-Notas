from tokenize import String

class Materia():
    nombre: String
    calificaciones = []

    def __init__(self, nombre):
        self.nombre = nombre

    def setNombre(self, nombre):
        self.nombre = nombre
        
    def getNombre(self):
        return self.nombre

    def setCalificaciones(self, calificacion):
        self.append(calificacion)

    
