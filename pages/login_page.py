"""Login Page Object"""
import time
from pages.base_page import BasePage
from config.locators import LoginLocators


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = LoginLocators
    
    def iniciar_sesion(self, email, password):
        print(f"[Login] Iniciando sesión con: {email}")
        
        campo_email = self.esperar_elemento(self.locators.CAMPO_EMAIL, timeout=15)
        if campo_email:
            campo_email.clear()
            campo_email.send_keys(email)
            print("[Login] Email ingreado")
        
        time.sleep(0.5)
        
        campo_password = self.esperar_elemento(self.locators.CAMPO_PASSWORD, timeout=10)
        if campo_password:
            campo_password.clear()
            campo_password.send_keys(password)
            print("[Login] Password ingresada")
        
        time.sleep(0.5)
        
        self.esperar_elemento(self.locators.BOTON_ENTRAR, timeout=10).click()
        print("[Login] Click en Entrar")
        
        time.sleep(3)
        print("[Login] Sesión iniciada")
    
    def esta_en_pantalla_login(self):
        return self.esta_visible(self.locators.CAMPO_EMAIL, timeout=5) is not None