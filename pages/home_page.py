"""Home Page Object - Gobierno Digital"""
import time
from pages.base_page import BasePage
from config.locators import GDLocators, CommonLocators


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = GDLocators

    def verificar_saludo(self):
        return self.esta_visible(self.locators.SALUDO, timeout=5) is not None

    def verificar_pregunta(self):
        return self.esta_visible(self.locators.PREGUNTA, timeout=5) is not None

    def verificar_servicios(self):
        return self.esta_visible(self.locators.TITULO_SERVICIOS, timeout=5) is not None

    def obtener_texto_saludo(self):
        return self.obtener_texto(self.locators.SALUDO)

    def obtener_texto_pregunta(self):
        return self.obtener_texto(self.locators.PREGUNTA)

    def click_servicio(self, nombre_servicio):
        if nombre_servicio in self.locators.SERVICIOS:
            self.hacer_click(self.locators.SERVICIOS[nombre_servicio])
            time.sleep(1)
            print(f"[Click] Servicio: {nombre_servicio}")
        else:
            raise Exception(f"Servicio no encontrado: {nombre_servicio}")

    def scroll_servicios(self):
        self.scroll_abajo(500)
        time.sleep(1)
        print("[Scroll] Abajo para ver más servicios")

    def verificar_interes(self):
        return self.esta_visible(self.locators.TITULO_TE_PODRIA_INTERESAR, timeout=5) is not None

    def ir_inicio(self):
        self.hacer_click(self.locators.TAB_INICIO)
        time.sleep(1)
        print("[Nav] Pestaña Inicio")

    def ir_explorar(self):
        self.hacer_click(self.locators.TAB_EXPLORAR)
        time.sleep(1)
        print("[Nav] Pestaña Explorar")

    def ir_notificaciones(self):
        self.hacer_click(self.locators.TAB_NOTIFICACIONES)
        time.sleep(1)
        print("[Nav] Pestaña Notificaciones")

    def ir_credencial(self):
        self.hacer_click(self.locators.TAB_CREDENCIAL)
        time.sleep(1)
        print("[Nav] Pestaña Credencial")

    def esta_en_inicio(self):
        return self.esta_visible(self.locators.TAB_INICIO, timeout=3) is not None

    def volver(self):
        btn_atras = self.esperar_elemento(CommonLocators.BOTON_ATRAS, timeout=5)
        if btn_atras:
            btn_atras.click()
            time.sleep(1)
            print("[Nav] Botón atrás")