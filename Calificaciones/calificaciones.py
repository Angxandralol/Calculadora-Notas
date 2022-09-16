from tokenize import String
from numpy import integer

class Calificacion():
    nombre: String 
    calificacionMaxima: int
    calificacionObtenida: int
    porcentajeMaximo: int
    porcentajeObtenido: int

    def __init__(self, calificacionMaxima, porcentajeMaximo):
        self.calificacionMaxima = calificacionMaxima
        self.porcentajeMaximo = porcentajeMaximo

    def setCalificacionObtenida(self, calificacionObtenida):
        self.calificacionObtenida = calificacionObtenida
        self.setPorcentajeObtenido()

    def getCalificacionObtenida(self):
        return self.calificacionObtenida

    def setPorcentajeObtenido(self):
        self.porcentajeObtenido = (self.calificacionObtenida * self.porcentajeObtenido) / self.calificacionMaxima

