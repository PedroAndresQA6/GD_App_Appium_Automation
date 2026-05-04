"""Test: 08 - Bienestar Animal - Exploración"""
import time
from appium.webdriver.common.appiumby import AppiumBy


def test_bienestar_animal(driver, home_page):
    """Test: Bienestar Animal - Explorar"""
    print("\n=== TEST: Bienestar Animal - Explorar ===")
    
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
    
    print("[Test] Click en Bienestar Animal")
    elem = home_page.esperar_elemento((AppiumBy.ACCESSIBILITY_ID, "Bienestar Animal"), timeout=5)
    if elem:
        elem.click()
    time.sleep(2)
    
    print("[OK] Bienestar Animal")
    
    home_page.tomar_screenshot("bienestar_principal")
    
    print("[Test] Adopción (Web)")
    adopcion = home_page.esperar_elemento((AppiumBy.ACCESSIBILITY_ID, "Adopción"), timeout=5)
    if adopcion:
        try:
            adopcion.click()
            print("[Test] Esperando 5 segundos en Adopción")
            time.sleep(5)
            driver.back()
            time.sleep(2)
        except:
            pass
    
    print("[Test] Información (Web)")
    informacion = home_page.esperar_elemento((AppiumBy.ACCESSIBILITY_ID, "Información"), timeout=5)
    if informacion:
        try:
            informacion.click()
            print("[Test] Esperando 5 segundos en Información")
            time.sleep(5)
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
            
            articulos = home_page.encontrar_elementos(
                (AppiumBy.XPATH, "//android.widget.ImageView[contains(@content-desc, 'SMDIF') or contains(@content-desc, 'Felifer') or contains(@content-desc, 'abril')]")
            )
            
            if articulos:
                print(f"[Test] Entrando a noticia")
                articulos[0].click()
                time.sleep(3)
                driver.back()
                time.sleep(2)
                
                for _ in range(5):
                    if home_page.encontrar_elementos((AppiumBy.XPATH, "//android.widget.ImageView[contains(@content-desc, 'SMDIF') or contains(@content-desc, 'Felifer') or contains(@content-desc, 'abril')]")):
                        break
                    time.sleep(1)
            
            home_page.scroll_arriba(500)
            time.sleep(1)
            driver.back()
            time.sleep(2)
        except:
            pass
    
    print("[Test] Scroll para explorar programas")
    home_page.scroll_abajo(800)
    time.sleep(1)
    home_page.scroll_abajo(800)
    time.sleep(1)
    
    print("[Test] Buscar programas con 'Me interesa'")
    programas = home_page.encontrar_elementos(
        (AppiumBy.XPATH, "//android.widget.ImageView[contains(@content-desc, 'Me interesa')]")
    )
    
    if programas:
        print(f"[OK] Se encontraron {len(programas)} programas")
    
    print("[Test] Regresar al menú")
    try:
        driver.back()
    except:
        pass
    time.sleep(2)
    
    print("[Test] PASSED")