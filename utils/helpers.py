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


def agregar_archivo_tomar_foto(driver, home_page, descripcion="Agregar archivos"):
    """
    Función para agregar archivo tomando una foto con la cámara.
    
    Args:
        driver: WebDriver de Appium
        home_page: Page Object de HomePage
        descripcion: Texto del botón de agregar archivos (default: "Agregar archivos")
    
    Returns:
        bool: True si se tomó la foto exitosamente, False otherwise
    """
    from appium.webdriver.common.appiumby import AppiumBy
    
    print(f"[Helper] Click en '{descripcion}'")
    boton_agregar = home_page.esperar_elemento(
        (AppiumBy.XPATH, f"//android.view.View[@content-desc='{descripcion}']"), 
        timeout=5
    )
    
    if boton_agregar:
        boton_agregar.click()
        time.sleep(3)
        
        print("[Helper] Buscando botón para tomar foto")
        try:
            boton_tomar_foto = driver.find_element(
                AppiumBy.XPATH, 
                "//android.view.View[@bounds='[520,2520][760,2760]']"
            )
            boton_tomar_foto.click()
            time.sleep(3)
            print("[Helper] Foto tomada exitosamente")
            return True
        except Exception as e:
            print(f"[Helper] Error al tomar foto: {e}")
            return False
    else:
        print(f"[Helper] No se encontró botón '{descripcion}'")
        return False