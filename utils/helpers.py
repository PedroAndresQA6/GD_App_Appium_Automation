"""Funciones auxiliares"""
import random
import time
from datetime import datetime, timedelta


def generar_nombre_aleatorio():
    """Genera un nombre aleatorio"""
    nombres = ["Juan", "Pedro", "Carlos", "Luis", "Miguel", "Jose", 
              "Maria", "Ana", "Sofia", "Laura", "Kenia", "Carlos"]
    return random.choice(nombres)


def generar_fecha_aleatoria(anio_min=1960, anio_max=2000):
    """Genera una fecha aleatoria"""
    inicio = datetime(anio_min, 1, 1)
    fin = datetime(anio_max, 12, 31)
    delta = fin - inicio
    dias = random.randint(0, delta.days)
    fecha = inicio + timedelta(days=dias)
    return fecha.strftime("%d/%m/%Y")


def esperar_segundos(segundos):
    """Espera por segundos especificados"""
    time.sleep(segundos)


def scroll_hasta_elemento(driver, locator, direccion="abajo"):
    """Scroll hasta encontrar un elemento"""
    for _ in range(10):
        try:
            elemento = driver.find_element(*locator)
            if elemento:
                return elemento
        except:
            pass
        
        if direccion == "abajo":
            driver.swipe(540, 1400, 540, 600, 300)
        else:
            driver.swipe(540, 600, 540, 1400, 300)
        time.sleep(0.5)
    
    return None


def obtener_elemento_aleatorio(locator_list):
    """Obtiene un elemento aleatorio de una lista"""
    if locator_list:
        return random.choice(locator_list)
    return None


def formatear_numero(numero):
    """Formatea un numero con separador de miles"""
    return f"{numero:,}".replace(",", ".")


def generar_curp_valido():
    """Genera un CURP basico valido"""
    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numeros = "0123456789"
    curp = ""
    curp += random.choice(letras)
    curp += random.choice(letras)
    curp += random.choice(letras)
    curp += random.choice(letras)
    curp += random.choice(letras[1:])
    curp += random.choice(letras[1:])
    curp += random.choice(numeros) * 2
    curp += random.choice(numeros) * 2
    curp += random.choice(numeros) + random.choice(letras)
    curp += random.choice(letras) * 2
    return curp


def generar_telefono():
    """Genera un numero de telefono aleatorio"""
    numeros = "0123456789"
    telefono = "55"
    for _ in range(8):
        telefono += random.choice(numeros)
    return telefono