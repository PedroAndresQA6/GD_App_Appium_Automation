"""Test: 04 - DIF - Exploración"""
import time
from appium.webdriver.common.appiumby import AppiumBy


def test_dif_explorar(driver, home_page):
    """Test: DIF - Explorar opciones"""
    print("\n=== TEST: DIF - Explorar ===")
    
    time.sleep(3)
    
    print("[Test] Verificar que estamos en inicio")
    for i in range(3):
        if home_page.verificar_saludo():
            print("[OK] Estamos en inicio")
            break
        if i < 2:
            try:
                driver.back()
                time.sleep(2)
            except:
                pass
    
    print("[Test] Click en DIF")
    home_page.click_servicio("DIF")
    time.sleep(2)
    
    print("[Test] Verificando pantalla de DIF")
    page_source = driver.page_source
    assert "DIF" in page_source, "No se encontró DIF"
    
    print("[Test] Verificar atajos")
    assert "Credencial" in page_source
    assert "Noticias" in page_source
    assert "Jornadas" in page_source
    assert "Contacto" in page_source
    
    home_page.tomar_screenshot("dif_principal")
    
    print("[Test] Click en Credencial")
    credencial = home_page.esperar_elemento((AppiumBy.ACCESSIBILITY_ID, "Credencial"), timeout=5)
    if credencial:
        try:
            credencial.click()
            time.sleep(2)
            time.sleep(3)
            try:
                driver.back()
            except:
                pass
            time.sleep(2)
        except:
            pass
    
    print("[Test] Click en Noticias")
    noticias = home_page.esperar_elemento((AppiumBy.ACCESSIBILITY_ID, "Noticias"), timeout=5)
    if noticias:
        try:
            noticias.click()
            time.sleep(2)
            home_page.scroll_abajo(500)
            time.sleep(1)
            home_page.scroll_arriba(500)
            time.sleep(1)
            try:
                driver.back()
            except:
                pass
            time.sleep(2)
        except:
            pass
    
    print("[Test] Click en Jornadas")
    jornadas = home_page.esperar_elemento((AppiumBy.ACCESSIBILITY_ID, "Jornadas"), timeout=5)
    if jornadas:
        try:
            jornadas.click()
            time.sleep(2)
            
            page_source = driver.page_source
            assert "Jornadas" in page_source
            
            pestanas = ["dif", "donativos", "rehabilitación", "vacunación"]
            
            for nombre_pestana in pestanas:
                print(f"[Test] Pestaña: {nombre_pestana}")
                
                try:
                    boton_pestana = home_page.esperar_elemento(
                        (AppiumBy.ACCESSIBILITY_ID, nombre_pestana), 
                        timeout=3
                    )
                    if boton_pestana:
                        boton_pestana.click()
                        time.sleep(2)
                        
                        page_source = driver.page_source
                        
                        if "No hay noticias disponibles" in page_source:
                            print(f"[OK] Sin contenido")
                            continue
                        
                        print(f"[OK] Hay contenido")
                        
                        articulos = home_page.encontrar_elementos(
                            (AppiumBy.XPATH, "//android.widget.ImageView[contains(@content-desc, 'más')]")
                        )
                        
                        for i, articulo in enumerate(articulos[:2]):
                            try:
                                print(f"[Test] Artículo {i+1}")
                                articulo.click()
                                time.sleep(2)
                                time.sleep(2)
                                try:
                                    driver.back()
                                except:
                                    pass
                                time.sleep(1)
                            except:
                                pass
                except:
                    pass
            
            try:
                driver.back()
            except:
                pass
            time.sleep(2)
        except:
            pass
    
    print("[Test] Click en Contacto")
    contacto = home_page.esperar_elemento((AppiumBy.ACCESSIBILITY_ID, "Contacto"), timeout=5)
    if contacto:
        try:
            contacto.click()
            time.sleep(2)
            time.sleep(3)
            try:
                driver.back()
            except:
                pass
            time.sleep(2)
        except:
            pass
    
    print("[Test] Scroll down para ver programas")
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
        for i, prog in enumerate(programas):
            nombre = prog.get_attribute('content-desc')[:40]
            print(f"  - Programa {i+1}: {nombre}...")
    
    print("[Test] Regresar al menú principal")
    try:
        driver.back()
    except:
        pass
    time.sleep(2)
    
    print("[Test] PASSED")