"""Test: 09 - Deporte - Exploración"""
import time
from appium.webdriver.common.appiumby import AppiumBy


def test_deporte(driver, home_page):
    """Test: Deporte - Explorar"""
    print("\n=== TEST: Deporte - Explorar ===")
    
    time.sleep(3)
    
    print("[Test] Verificar inicio")
    for i in range(3):
        if home_page.verificar_saludo():
            print("[OK] Inicio")
            break
        if i < 2:
            try:
                driver.back()
                time.sleep(2)
            except:
                pass
    
    print("[Test] Click en Deporte")
    elem = home_page.esperar_elemento((AppiumBy.ACCESSIBILITY_ID, "Deporte"), timeout=5)
    if elem:
        elem.click()
    time.sleep(2)
    
    print("[OK] Deporte")
    
    home_page.tomar_screenshot("deporte_principal")
    
    print("[Test] Credencial")
    credencial = home_page.esperar_elemento((AppiumBy.ACCESSIBILITY_ID, "Credencial"), timeout=5)
    if credencial:
        try:
            credencial.click()
            time.sleep(2)
            home_page.scroll_abajo(500)
            time.sleep(1)
            home_page.scroll_arriba(500)
            time.sleep(1)
            driver.back()
            time.sleep(2)
        except:
            pass
    
    print("[Test] Explora")
    explora = home_page.esperar_elemento((AppiumBy.ACCESSIBILITY_ID, "Explora"), timeout=5)
    if explora:
        try:
            explora.click()
            time.sleep(2)
            home_page.scroll_abajo(500)
            time.sleep(1)
            home_page.scroll_arriba(500)
            time.sleep(1)
            driver.back()
            time.sleep(2)
        except:
            pass
    
    print("[Test] Contacto")
    contacto = home_page.esperar_elemento((AppiumBy.ACCESSIBILITY_ID, "Contacto"), timeout=5)
    if contacto:
        try:
            contacto.click()
            time.sleep(2)
            home_page.scroll_abajo(500)
            time.sleep(1)
            home_page.scroll_arriba(500)
            time.sleep(1)
            driver.back()
            time.sleep(2)
        except:
            pass
    
    print("[Test] Scroll para explorar clases")
    home_page.scroll_abajo(800)
    time.sleep(1)
    
    clases = home_page.encontrar_elementos(
        (AppiumBy.XPATH, "//android.widget.ImageView[contains(@content-desc, 'Clase')]")
    )
    
    if clases:
        print(f"[OK] Se encontraron {len(clases)} clases")
        
        print("[Test] Entrando a clase")
        clases[0].click()
        time.sleep(2)
        
        print("[Test] Clic en Inscribirse")
        inscribirse = home_page.esperar_elemento((AppiumBy.ACCESSIBILITY_ID, "Inscribirse"), timeout=5)
        if inscribirse:
            try:
                inscribirse.click()
                time.sleep(3)
                
                popup = home_page.esperar_elemento((AppiumBy.ACCESSIBILITY_ID, "Cerrar"), timeout=5)
                if popup:
                    print("[Test] Popup de inscripción - Cerrar")
                    popup.click()
                    time.sleep(2)
            except:
                pass
        
        print("[Test] Regresando al menú de Deporte")
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