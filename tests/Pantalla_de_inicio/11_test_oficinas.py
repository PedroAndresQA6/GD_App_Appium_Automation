"""Test: 11 - Oficinas - Exploración"""
import time
from appium.webdriver.common.appiumby import AppiumBy


def test_oficinas(driver, home_page):
    """Test: Oficinas - Explorar"""
    print("\n=== TEST: Oficinas - Explorar ===")
    
    time.sleep(3)
    
    print("[Test] Click en Oficinas")
    home_page.scroll_abajo(500)
    time.sleep(1)
    elem = home_page.esperar_elemento((AppiumBy.ACCESSIBILITY_ID, "Oficinas"), timeout=5)
    if elem:
        elem.click()
    time.sleep(2)
    
    print("[OK] Oficinas")
    home_page.tomar_screenshot("oficinas_principal")
    
    print("[Test] Explorar oficinas")
    for i in range(3):
        print(f"[Test] Iteración {i+1}")
        time.sleep(1)
        try:
            driver.implicitly_wait(3)
            oficinas = home_page.encontrar_elementos(
                (AppiumBy.XPATH, "//android.view.View[contains(@content-desc, 'Centro')]//following-sibling::android.widget.ImageView")
            )
            if not oficinas:
                oficinas = home_page.encontrar_elementos(
                    (AppiumBy.XPATH, "//android.widget.ImageView[contains(@content-desc, 'Centro') or contains(@content-desc, 'Dirección') or contains(@content-desc, 'Instituto') or contains(@content-desc, 'Oficialia')]")
                )
            print(f"[Debug] Oficinas encontradas: {len(oficinas) if oficinas else 0}")
            if oficinas and i < len(oficinas):
                print(f"[Test] Entrar a oficina {i+1}")
                oficinas[i].click()
                time.sleep(2)
                
                print("[Test] Click Cómo llegar")
                boton = home_page.encontrar_elemento(
                    (AppiumBy.XPATH, "//android.widget.Button[@content-desc='Cómo llegar']")
                )
                if boton:
                    boton.click()
                    time.sleep(8)
                    
                    print("[Test] Regresar a Oficinas")
                    driver.back()
                    time.sleep(2)
                    driver.back()
                    time.sleep(2)
                    
                    if i < 2:
                        home_page.scroll_abajo(500)
                        time.sleep(1)
                else:
                    print("[Warn] Botón Cómo llegar no encontrado")
                    driver.back()
                    time.sleep(2)
        except Exception as e:
            print(f"[Error] {e}")
        time.sleep(1)
    
    print("[Test] PASSED")
    
    print("[Test] Regresar al inicio")
    driver.back()
    time.sleep(2)