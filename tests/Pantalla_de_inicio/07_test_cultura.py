"""Test: 07 - Cultura - Exploración"""
import time
from appium.webdriver.common.appiumby import AppiumBy


def test_cultura_explorar(driver, home_page):
    """Test: Cultura - Explorar"""
    print("\n=== TEST: Cultura - Explorar ===")
    
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
    
    print("[Test] Click en Cultura")
    home_page.click_servicio("Cultura")
    time.sleep(2)
    
    if "Cultura" not in driver.page_source:
        print("[Test] Scroll para buscar Cultura")
        home_page.scroll_abajo(500)
        time.sleep(1)
    
    assert "Querétaro" in driver.page_source
    print("[OK] Cultura")
    
    home_page.tomar_screenshot("cultura_principal")
    
    print("[Test] Cartelera")
    cartelera = home_page.esperar_elemento((AppiumBy.ACCESSIBILITY_ID, "Cartelera"), timeout=5)
    if cartelera:
        try:
            cartelera.click()
            time.sleep(2)
            home_page.scroll_abajo(500)
            time.sleep(1)
            
            articulos = home_page.encontrar_elementos(
                (AppiumBy.XPATH, "//android.widget.ImageView[contains(@content-desc, 'CONOCE') or contains(@content-desc, 'abril')]")
            )
            
            if articulos:
                print(f"[Test] Entrando a artículo")
                articulos[0].click()
                time.sleep(3)
                driver.back()
                time.sleep(2)
            
            home_page.scroll_arriba(500)
            time.sleep(1)
            driver.back()
            time.sleep(2)
        except:
            pass
    
    print("[Test] Explorar")
    explorar = home_page.esperar_elemento((AppiumBy.ACCESSIBILITY_ID, "Explorar"), timeout=5)
    if explorar:
        try:
            explorar.click()
            time.sleep(2)
            home_page.scroll_abajo(500)
            time.sleep(1)
            home_page.scroll_arriba(500)
            time.sleep(1)
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
    
    print("[Test] Artículo principal")
    home_page.scroll_abajo(800)
    time.sleep(1)
    
    articulo = home_page.esperar_elemento(
        (AppiumBy.XPATH, "//android.widget.ImageView[contains(@content-desc, 'Cultural')]"),
        timeout=5
    )
    if not articulo:
        home_page.scroll_abajo(800)
        time.sleep(1)
        articulo = home_page.esperar_elemento(
            (AppiumBy.XPATH, "//android.widget.ImageView[contains(@content-desc, 'Cultural')]"),
            timeout=5
        )
    
    if articulo:
        print(f"[Test] Entrando a artículo principal")
        articulo.click()
        time.sleep(3)
        driver.back()
        time.sleep(2)
    
    print("[Test] Regresar al menú")
    try:
        driver.back()
    except:
        pass
    time.sleep(2)
    
    print("[Test] PASSED")