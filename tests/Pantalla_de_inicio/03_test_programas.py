"""Test: 03 - Programas - Exploración"""
import time
from appium.webdriver.common.appiumby import AppiumBy


def test_programas_explorar(driver, home_page):
    """Test: Programas - Explorar opciones"""
    print("\n=== TEST: Programas - Explorar ===")
    
    time.sleep(3)
    
    if not home_page.verificar_saludo():
        print("[Test] Volviendo a inicio...")
        driver.back()
        time.sleep(2)
        if not home_page.verificar_saludo():
            driver.back()
            time.sleep(2)
    
    print("[Test] Click en Programas")
    home_page.click_servicio("Programas")
    time.sleep(2)
    
    print("[Test] Verificando pantalla de Programas")
    page_source = driver.page_source
    assert "Desarrollo Social" in page_source, "No se encontró Desarrollo Social"
    print("[OK] Título Desarrollo Social encontrado")
    
    print("[Test] Verificar opciones: Credencial, Noticias, Contacto")
    assert "Credencial" in page_source
    print("[OK] Credencial encontrado")
    assert "Noticias" in page_source
    print("[OK] Noticias encontrado")
    assert "Contacto" in page_source
    print("[OK] Contacto encontrado")
    
    home_page.tomar_screenshot("programas_principal")
    
    print("[Test] Click en Credencial")
    credencial = home_page.esperar_elemento((AppiumBy.ACCESSIBILITY_ID, "Credencial"), timeout=5)
    if credencial:
        credencial.click()
        time.sleep(2)
        time.sleep(3)
        try:
            driver.back()
        except:
            pass
        time.sleep(2)
    
    print("[Test] Click en Noticias")
    noticias = home_page.esperar_elemento((AppiumBy.ACCESSIBILITY_ID, "Noticias"), timeout=5)
    if noticias:
        noticias.click()
        time.sleep(2)
        home_page.scroll_abajo(500)
        time.sleep(1)
        home_page.scroll_arriba(500)
        time.sleep(1)
        driver.back()
        time.sleep(2)
    
    print("[Test] Click en Contacto")
    contacto = home_page.esperar_elemento((AppiumBy.ACCESSIBILITY_ID, "Contacto"), timeout=5)
    if contacto:
        contacto.click()
        time.sleep(2)
        time.sleep(3)
        try:
            driver.back()
        except:
            pass
        time.sleep(2)
    
    print("[Test] Regresar al menú")
    try:
        driver.back()
    except:
        pass
    time.sleep(2)
    
    print("[Test] PASSED")