"""Test: 06 - Turismo - Exploración"""
import time
from appium.webdriver.common.appiumby import AppiumBy


def test_turismo_explorar(driver, home_page):
    """Test: Turismo - Explorar"""
    print("\n=== TEST: Turismo - Explorar ===")
    
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
    
    print("[Test] Click en Turismo")
    home_page.click_servicio("Turismo")
    time.sleep(2)
    
    assert "Querétaro" in driver.page_source
    print("[OK] Turismo")
    
    home_page.tomar_screenshot("turismo_principal")
    
    print("[Test] Explorar")
    explorar = home_page.esperar_elemento((AppiumBy.ACCESSIBILITY_ID, "Explorar"), timeout=5)
    if explorar:
        try:
            explorar.click()
            time.sleep(2)
            time.sleep(3)
            driver.back()
            time.sleep(2)
        except:
            pass
    
    print("[Test] Noticias")
    noticias = home_page.esperar_elemento((AppiumBy.ACCESSIBILITY_ID, "Noticias"), timeout=5)
    if noticias:
        try:
            noticias.click()
            time.sleep(2)
            home_page.scroll_abajo(500)
            time.sleep(1)
            home_page.scroll_arriba(500)
            time.sleep(1)
            driver.back()
            time.sleep(2)
        except:
            pass
    
    print("[Test] Transporte")
    transporte = home_page.esperar_elemento((AppiumBy.ACCESSIBILITY_ID, "Transporte"), timeout=5)
    if transporte:
        try:
            transporte.click()
            time.sleep(3)
            
            if "WebView" in driver.page_source:
                print("[OK] WebView")
                
                servicios = ["Qrobus"]
                
                for svc in servicios:
                    elem = home_page.esperar_elemento(
                        (AppiumBy.XPATH, f"//*[contains(@content-desc, '{svc}')]"), 
                        timeout=5
                    )
                    if not elem:
                        home_page.scroll_abajo(400)
                        time.sleep(1)
                        elem = home_page.esperar_elemento(
                            (AppiumBy.XPATH, f"//*[contains(@content-desc, '{svc}')]"), 
                            timeout=5
                        )
                    
                    if elem:
                        print(f"[OK] {svc}")
                        elem.click()
                        time.sleep(2)
                        home_page.scroll_abajo(300)
                        time.sleep(1)
                        home_page.scroll_arriba(300)
                        time.sleep(1)
                    else:
                        print(f"[WARN] {svc}")
                
                driver.back()
            else:
                print("[WARN] WebView no detectado")
                driver.back()
            
            time.sleep(2)
            
            contacto = home_page.esperar_elemento((AppiumBy.ACCESSIBILITY_ID, "Contacto"), timeout=5)
            if contacto:
                contacto.click()
                time.sleep(2)
                home_page.scroll_abajo(500)
                time.sleep(1)
                home_page.scroll_arriba(500)
                time.sleep(1)
                driver.back()
                time.sleep(2)
        except Exception as e:
            print(f"[ERROR] Transporte: {e}")
    
    print("[Test] Scroll eventos")
    home_page.scroll_abajo(800)
    time.sleep(1)
    home_page.scroll_arriba(500)
    time.sleep(1)
    
    print("[Test] Regresar al menú")
    try:
        driver.back()
    except:
        pass
    time.sleep(2)
    
    print("[Test] PASSED")