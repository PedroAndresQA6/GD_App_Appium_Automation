"""Test de ejemplo - Login y navegar a perfil"""
import time
from appium.webdriver.common.appiumby import AppiumBy
from config.settings import Settings
from config.locators import HomeLocators


def test_ejemplo_login(driver, home_page):
    """Test funcional de ejemplo"""
    print("\n=== TEST: Ejemplo - Login y Navegacion ===")
    
    time.sleep(2)
    
    # Verificar que estamos en la pantalla de inicio (en pestana Inicio)
    if home_page.esta_en_inicio():
        print("[Test] Ya en pantalla de inicio")
    else:
        # Navegar a inicio
        home_page.navegar_inicio()
    
    # Abrir menu perfil
    home_page.abrir_perfil()
    time.sleep(1)
    
    # Tomar screenshot
    home_page.tomar_screenshot("test_ejemplo_perfil")
    print("[Test] Perfil abierto - Test completado")
    print(f"[Test] PASSED")


def test_login_basico(driver, login_page):
    """Test de login basico"""
    print("\n=== TEST: Login Basico ===")
    
    login_page.iniciar_sesion(
        Settings.CREDENTIALS["email"],
        Settings.CREDENTIALS["password"]
    )
    
    print("[Test] Login completado")


def test_navegacion_tabs(driver, home_page):
    """Test de navegacion por todas las tabs"""
    print("\n=== TEST: Navegacion Tabs ===")
    
    home_page.navegar_inicio()
    time.sleep(1)
    
    home_page.navegar_medicos()
    time.sleep(1)
    
    home_page.navegar_consultas()
    time.sleep(1)
    
    home_page.navegar_medicinas()
    time.sleep(1)
    
    home_page.navegar_estudios()
    time.sleep(1)
    
    home_page.navegar_inicio()
    print("[Test] Navegacion completada")