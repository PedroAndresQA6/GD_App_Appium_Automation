"""Home Page Object"""
import time
from pages.base_page import BasePage
from config.locators import HomeLocators, CommonLocators


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = HomeLocators
    
    def navegar_inicio(self):
        self.hacer_click(self.locators.TAB_INICIO)
        time.sleep(2)
        print("[Nav] Pestaña Inicio")
    
    def navegar_medicos(self):
        self.hacer_click(self.locators.TAB_MEDICOS)
        time.sleep(2)
        print("[Nav] Pestaña Médicos")
    
    def navegar_consultas(self):
        self.hacer_click(self.locators.TAB_CONSULTAS)
        time.sleep(2)
        print("[Nav] Pestaña Consultas")
    
    def navegar_medicinas(self):
        self.hacer_click(self.locators.TAB_MEDICINAS)
        time.sleep(2)
        print("[Nav] Pestaña Medicinas")
    
    def navegar_estudios(self):
        self.hacer_click(self.locators.TAB_ESTUDIOS)
        time.sleep(2)
        print("[Nav] Pestaña Estudios")
    
    def abrir_perfil(self):
        self.hacer_click(self.locators.MENU_PERFIL)
        time.sleep(1)
        print("[Nav] Menú Perfil abierto")
    
    def esta_en_inicio(self):
        return self.esta_visible(self.locators.TAB_INICIO, timeout=3) is not None
    
    def volver(self):
        btn_atras = self.esperar_elemento(CommonLocators.BOTON_ATRAS, timeout=5)
        if btn_atras:
            btn_atras.click()
            time.sleep(1)
            print("[Nav] Botón atrás")