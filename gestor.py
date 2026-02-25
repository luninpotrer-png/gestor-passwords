import json
from json import JSONDecodeError
import hashlib

def hashear(password):
    return hashlib.sha256(password.encode()).hexdigest()

def cargar_datos():
    try:
        with open("datos.json", "r") as d:
            return json.load(d)
    except (JSONDecodeError,FileNotFoundError):
        return None

def guardar_datos(datos):
    with open("datos.json", "w") as d:
        json.dump(datos,d, indent=4)

def configurar_master(password):
    datos = {
        "master" : hashear(password),
        "bovedas" : {
            "Redes Sociales" : [],
            "Trabajo" : [],
            "Bancos" : []
        }
    }
    guardar_datos(datos)

def verificar_master(intento,masterkey):
    if hashear(intento) == masterkey:
        return True
    else:
        return False