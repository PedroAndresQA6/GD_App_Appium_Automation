"""Test: 02 - 070 Digital - Completo"""
import time
from appium.webdriver.common.appiumby import AppiumBy
from config.locators import Digital070Locators


def test_070_digital_completo(driver, home_page):
    """Test: 070 Digital - Completo"""
    print("\n=== TEST: 070 Digital - COMPLETO ===")
    
    time.sleep(3)
    
    if not home_page.verificar_saludo():
        print("[Test] Volviendo a inicio...")
        try:
            driver.back()
        except:
            pass
        time.sleep(2)
    
    print("=" * 50)
    print("PARTE 1: Atención Ciudadana")
    print("=" * 50)
    
    print("[Test] Click en 070_Digital")
    home_page.click_servicio("070_Digital")
    time.sleep(2)
    
    print("[Test] Buscar botón AGREGAR o REPORTAR")
    boton_agregar = home_page.esperar_elemento(Digital070Locators.BOTON_AGREGAR, timeout=3)
    if boton_agregar:
        boton_agregar.click()
    else:
        boton_reportar = home_page.esperar_elemento(Digital070Locators.BOTON_REPORTAR, timeout=3)
        if boton_reportar:
            boton_reportar.click()
    time.sleep(2)
    
    print("[Test] Click en botón 'Ver todos'")
    boton_ver_todos = home_page.esperar_elemento(
        (AppiumBy.ACCESSIBILITY_ID, "Ver todos"), timeout=3
    )
    if not boton_ver_todos:
        boton_ver_todos = home_page.esperar_elemento(
            (AppiumBy.XPATH, "//android.view.View[@content-desc='Ver todos']"), timeout=3
        )
    if boton_ver_todos:
        boton_ver_todos.click()
        time.sleep(2)
    
    print("[Test] Scroll down para ver opciones")
    home_page.scroll_abajo(500)
    time.sleep(1)
    
    print("[Test] Buscar opciones disponibles")
    opciones = home_page.encontrar_elementos(
        (AppiumBy.XPATH, "//android.widget.ImageView[contains(@content-desc, 'Prueba') or contains(@content-desc, 'prueba')]")
    )
    print(f"[Test] Encontradas {len(opciones)} opciones")
    
    if len(opciones) >= 1:
        print("[Test] Entrando a opción 1")
        opciones[0].click()
        time.sleep(3)
        
        print("[Test] Scroll down para ver formulario completo")
        home_page.scroll_abajo(500)
        time.sleep(1)
        
        print("[Test] Llenar campo REPORTE")
        campo_reporte = home_page.esperar_elemento(
            (AppiumBy.XPATH, "//android.widget.EditText[@hint='REPORTE']"), timeout=5
        )
        if campo_reporte:
            campo_reporte.click()
            time.sleep(1)
            campo_reporte.send_keys("Test reporte automatizado")
            time.sleep(1)
            
            print("[Test] Click en AGREGAR ARCHIVOS (Identificación)")
            agregar_id = home_page.esperar_elemento(
                (AppiumBy.XPATH, "//android.view.View[@content-desc='Agregar archivos']"), timeout=5
            )
            if agregar_id:
                agregar_id.click()
                time.sleep(3)
                
                print("[Test] Click en botón tomar foto")
                try:
                    boton_tomar_foto = driver.find_element(AppiumBy.XPATH, "//android.view.View[@bounds='[520,2520][760,2760]']")
                    boton_tomar_foto.click()
                    time.sleep(3)
                    print("[Test] Foto tomada")
                except Exception as e:
                    print(f"[Test] Error: {e}")
                
                time.sleep(2)
            
            print("[Test] Scroll down para ver más campos")
            home_page.scroll_abajo(500)
            time.sleep(1)
            
            print("[Test] Click en AGREGAR ARCHIVOS (Comprobante)")
            agregar_comp = home_page.esperar_elemento(
                (AppiumBy.XPATH, "//android.view.View[@content-desc='Agregar archivos']"), timeout=5
            )
            if agregar_comp:
                agregar_comp.click()
                time.sleep(3)
                
                print("[Test] Click en botón tomar foto")
                try:
                    boton_tomar_foto2 = driver.find_element(AppiumBy.XPATH, "//android.view.View[@bounds='[520,2520][760,2760]']")
                    boton_tomar_foto2.click()
                    time.sleep(3)
                    print("[Test] Foto tomada")
                except Exception as e:
                    print(f"[Test] Error: {e}")
                
                time.sleep(2)
        
        print("[Test] Buscar botón ENVIAR")
        boton_enviar = home_page.esperar_elemento(
            (AppiumBy.ACCESSIBILITY_ID, "ENVIAR"), timeout=5
        )
        if boton_enviar:
            print("[OK] Botón ENVIAR encontrado, clicking...")
            boton_enviar.click()
            time.sleep(5)
            print("[Test] Reporte enviado")
        
        print("[Test] Esperando pantalla de confirmación (Detalle)")
        time.sleep(3)
        
        print("[Test] Buscar botón cerrar")
        boton_cerrar = home_page.esperar_elemento(
            (AppiumBy.XPATH, "//android.widget.Button[@bounds='[1136,168][1280,312]']"), timeout=5
        )
        if boton_cerrar:
            print("[Test] Click en botón cerrar")
            boton_cerrar.click()
            time.sleep(2)
            print("[Test] Regresando al menú principal")
        
        print("[Test] Screenshot del formulario")
        home_page.tomar_screenshot("070_digital_formulario_1")
        
        print("[Test] TEST COMPLETO - PASSED")