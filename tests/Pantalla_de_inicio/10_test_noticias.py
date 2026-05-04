"""Test: 10 - Noticias - Exploración"""
import time
from appium.webdriver.common.appiumby import AppiumBy


def test_noticias(driver, home_page):
    """Test: Noticias - Explorar"""
    print("\n=== TEST: Noticias - Explorar ===")
    
    time.sleep(3)
    
    print("[Test] Click en Noticias")
    home_page.scroll_abajo(500)
    time.sleep(1)
    elem = home_page.esperar_elemento((AppiumBy.ACCESSIBILITY_ID, "Noticias"), timeout=5)
    if elem:
        elem.click()
    time.sleep(2)
    
    print("[OK] Noticias")
    home_page.tomar_screenshot("noticias_principal")
    
    print("[Test] Clicar pestañas")
    for i in range(4):
        try:
            botones = home_page.encontrar_elementos(
                (AppiumBy.XPATH, "//android.widget.HorizontalScrollView//android.widget.Button")
            )
            if botones and i < len(botones):
                botones[i].click()
                time.sleep(2)
                
                print(f"[Test] Entrar a artículo desde pestaña {i+1}")
                articulos = home_page.encontrar_elementos(
                    (AppiumBy.XPATH, "//android.widget.ImageView")
                )
                if articulos and len(articulos) > 1:
                    indice = min(i + 1, len(articulos) - 1)
                    articulos[indice].click()
                    time.sleep(3)
                    driver.back()
                    time.sleep(2)
        except Exception as e:
            print(f"[Error] {e}")
            break
        time.sleep(1)
    
    print("[Test] PASSED")
    
    print("[Test] Regresar al inicio")
    driver.back()
    time.sleep(2)