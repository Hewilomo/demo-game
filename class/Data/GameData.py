#Librerias
import json
import os

class GameData:
    def __init__(self, archivo='SaveData.json'):
        self.archivo = archivo
        self.mapa = None
        self.personaje = {}
        self.inventario = []
        self.dinero = None
        self.vida = None
        self.vivo = None
        self.cargarDatos()
        
    def cargarDatos(self):
        pass