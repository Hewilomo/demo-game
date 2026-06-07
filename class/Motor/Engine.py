#Librerias
import json
import os
#Metodos
def guardarDatos(datos, nombreArchivo):
    with open(nombreArchivo, 'w') as archivo:
        json.dump(datos, archivo)

def cargarDatos(nombreArchivo):
    if os.path.exists(nombreArchivo):
        with open(nombreArchivo, 'r') as archivo:
            datos = json.load(archivo)
            return datos
    else:
        return None
    