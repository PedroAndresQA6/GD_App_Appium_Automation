"""Funciones de navegacion"""
import time
from appium.webdriver.common.appiumby import AppiumBy
from config.locators import HomeLocators


def volver_inicio(driver, home_page):
    """Navega al inicio desde cualquier pantalla"""
    print("[Navegando] Volviendo a Inicio...")
    
    max_intentos = 5
    for intento in range(max_intentos):
        if home_page.esta_en_inicio():
            break
        
        try:
            btn_atras = driver.find_element(AppiumBy.XPATH, 
                "//android.widget.Button[@bounds='[12,168][156,312]']")
            if btn_atras:
                btn_atras.click()
                time.sleep(1)
        except:
            tabs = [
                HomeLocators.TAB_INICIO,
                HomeLocators.TAB_MEDICOS,
                HomeLocators.TAB_CONSULTAS,
                HomeLocators.TAB_MEDICINAS,
                HomeLocators.TAB_ESTUDIOS,
            ]
            for tab in tabs:
                try:
                    driver.find_element(*tab).click()
                    time.sleep(1)
                    if home_page.esta_en_inicio():
                        break
                except:
                    continue
    
    if home_page.esta_en_inicio():
        home_page.navegar_inicio()
        time.sleep(1)
        print("[Navegando] Ahora en Inicio")
    
    return home_page