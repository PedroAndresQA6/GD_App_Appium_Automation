"""Base Page Object con metodos comunes"""
import os
import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
    
    def hacer_click(self, locator, timeout=None):
        timeout = timeout or 10
        elemento = self.esperar_elemento(locator, timeout)
        if elemento:
            elemento.click()
        else:
            raise Exception(f"Elemento no encontrado: {locator}")
    
    def ingresar_texto(self, locator, texto, timeout=None):
        timeout = timeout or 10
        elemento = self.esperar_elemento(locator, timeout)
        if elemento:
            elemento.clear()
            elemento.send_keys(texto)
        else:
            raise Exception(f"Elemento no encontrado: {locator}")
    
    def esperar_elemento(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        try:
            return wait.until(EC.presence_of_element_located(locator))
        except:
            return None
    
    def esta_visible(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        try:
            return wait.until(EC.visibility_of_element_located(locator))
        except:
            return None
    
    def obtener_texto(self, locator, timeout=10):
        elemento = self.esperar_elemento(locator, timeout)
        return elemento.text if elemento else None
    
    def tomar_screenshot(self, nombre):
        from config.settings import Settings
        os.makedirs(Settings.SCREENSHOTS_DIR, exist_ok=True)
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        filename = f"{nombre}_{timestamp}.png"
        filepath = os.path.join(Settings.SCREENSHOTS_DIR, filename)
        self.driver.save_screenshot(filepath)
        print(f"[Screenshot]: {filepath}")
        return filepath
    
    def scroll_abajo(self, duracion=300):
        size = self.driver.get_window_size()
        inicio_x = size['width'] // 2
        inicio_y = int(size['height'] * 0.8)
        fin_y = int(size['height'] * 0.2)
        self.driver.swipe(inicio_x, inicio_y, inicio_x, fin_y, duracion)
    
    def scroll_arriba(self, duracion=300):
        size = self.driver.get_window_size()
        inicio_x = size['width'] // 2
        inicio_y = int(size['height'] * 0.2)
        fin_y = int(size['height'] * 0.8)
        self.driver.swipe(inicio_x, inicio_y, inicio_x, fin_y, duracion)
    
    def ocultar_keyboard(self):
        try:
            self.driver.hide_keyboard()
        except:
            pass
    
    def obtener_atributo(self, locator, atributo, timeout=10):
        elemento = self.esperar_elemento(locator, timeout)
        return elemento.get_attribute(atributo) if elemento else None
    
    def encontrar_elementos(self, locator):
        return self.driver.find_elements(*locator)
    
    def encontrar_elemento(self, locator):
        return self.driver.find_element(*locator)