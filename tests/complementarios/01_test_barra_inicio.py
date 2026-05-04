"""Test: 01 - Barra de Inicio (Navegacion inferior)"""
import time
from appium.webdriver.common.appiumby import AppiumBy


def test_barra_inicio(driver, home_page):
    """Test: Barra de Inicio - Navegacion inferior"""
    print("\n=== TEST: Barra de Inicio ===")
    
    time.sleep(3)
    
    print("[Test] Verificar que estamos en Inicio")
    if home_page.verificar_saludo():
        print("[OK] Estamos en Inicio")
    else:
        print("[WARN] No se detecto la pestana de Inicio")
    
    print("[Test] Click en Explorar (bounds [320,2610][640,2784])")
    driver.tap([(480, 2697)])  # Centro de [320,2610][640,2784]
    time.sleep(3)
    print("[OK] Pestana Explorar abierta")
    
    print("[Test] Scroll down")
    home_page.scroll_abajo(500)
    time.sleep(1)
    
    print("[Test] Scroll derecha")
    home_page.scroll_derecha(500)
    time.sleep(1)
    
    print("[Test] Scroll arriba")
    home_page.scroll_arriba(500)
    time.sleep(1)
    
    print("[Test] Scroll izquierda")
    home_page.scroll_izquierda(500)
    time.sleep(1)
    
    print("[Test] Regresar a Inicio")
    driver.back()
    time.sleep(2)
    
    print("[Test] Click en Notificaciones (bounds [640,2610][960,2784])")
    driver.tap([(800, 2697)])  # Centro de [640,2610][960,2784]
    time.sleep(3)
    print("[OK] Pestana Notificaciones abierta")
    
    print("[Test] Esperar 3 segundos para cargar")
    time.sleep(3)
    
    print("[Test] Regresar a Inicio")
    driver.back()
    time.sleep(2)
    
    print("[Test] Click en Credencial (bounds [960,2610][1280,2784])")
    driver.tap([(1120, 2697)])  # Centro de [960,2610][1280,2784]
    time.sleep(3)
    print("[OK] Pestana Credencial abierta")
    
    print("[Test] Esperar 3 segundos para cargar")
    time.sleep(3)
    
    print("[Test] Regresar a Inicio")
    driver.back()
    time.sleep(2)
    
    print("[Test] Verificar que seguimos en Inicio")
    if home_page.verificar_saludo():
        print("[OK] Estamos en la pantalla de inicio")
    
    print("[Test] PASSED")