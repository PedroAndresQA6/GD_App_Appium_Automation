"""Test: 13 - Trámites"""
import time
from appium.webdriver.common.appiumby import AppiumBy


def test_tramites(driver, home_page):
    """Test: Trámites - Explorar opciones"""
    print("\n=== TEST: Trámites ===")
    
    time.sleep(3)
    
    if not home_page.verificar_saludo():
        print("[Test] Volviendo a inicio...")
        try:
            driver.back()
        except:
            pass
        time.sleep(2)
    
    print("[Test] Click en Trámites")
    home_page.click_servicio("Trámites")
    time.sleep(3)
    
    print("[Test] Click en primer Ver todo (Más buscados)")
    ver_todo_1 = home_page.esperar_elemento(
        (AppiumBy.XPATH, "//android.widget.Button[@content-desc='Ver todo']"), 
        timeout=5
    )
    if ver_todo_1:
        ver_todo_1.click()
        time.sleep(2)
        print("[OK] Ver todo clicked")
    
    print("[Test] Click en primer trámite (Padron de Contratistas)")
    primer_tramite = home_page.esperar_elemento(
        (AppiumBy.XPATH, "//android.view.View[@content-desc='Padron de Contratistas']"), 
        timeout=5
    )
    if primer_tramite:
        primer_tramite.click()
        time.sleep(2)
        print("[OK] Trámite abierto")
        
        print("[Test] Scroll down 3 veces")
        home_page.scroll_abajo(500)
        time.sleep(1)
        home_page.scroll_abajo(500)
        time.sleep(1)
        home_page.scroll_abajo(500)
        time.sleep(1)
        
        print("[Test] Click en pestaña Archivos")
        archivos = home_page.esperar_elemento(
            (AppiumBy.XPATH, "//android.widget.RadioButton[@content-desc='Archivos']"), 
            timeout=5
        )
        if archivos:
            archivos.click()
            time.sleep(2)
            print("[OK] Archivos seleccionado")
        
        print("[Test] Regresar a lista de trámites")
        driver.back()
        time.sleep(2)
    
    print("[Test] Click en segundo trámite (Renovación con pago)")
    segundo_tramite = home_page.esperar_elemento(
        (AppiumBy.XPATH, "//android.view.View[@content-desc='Renovación con pago']"), 
        timeout=5
    )
    if segundo_tramite:
        segundo_tramite.click()
        time.sleep(2)
        print("[OK] Trámite abierto")
        
        print("[Test] Scroll down 3 veces")
        home_page.scroll_abajo(500)
        time.sleep(1)
        home_page.scroll_abajo(500)
        time.sleep(1)
        home_page.scroll_abajo(500)
        time.sleep(1)
        
        print("[Test] Click en pestaña Archivos")
        archivos = home_page.esperar_elemento(
            (AppiumBy.XPATH, "//android.widget.RadioButton[@content-desc='Archivos']"), 
            timeout=5
        )
        if archivos:
            archivos.click()
            time.sleep(2)
            print("[OK] Archivos seleccionado")
        
        print("[Test] Regresar a lista de trámites")
        driver.back()
        time.sleep(2)
    
    print("[Test] Click en tercer trámite (Renovación de Licencia)")
    tercer_tramite = home_page.esperar_elemento(
        (AppiumBy.XPATH, "//android.view.View[@content-desc='Renovación de Licencia']"), 
        timeout=5
    )
    if tercer_tramite:
        tercer_tramite.click()
        time.sleep(2)
        print("[OK] Trámite abierto")
        
        print("[Test] Scroll down 3 veces")
        home_page.scroll_abajo(500)
        time.sleep(1)
        home_page.scroll_abajo(500)
        time.sleep(1)
        home_page.scroll_abajo(500)
        time.sleep(1)
        
        print("[Test] Click en pestaña Archivos")
        archivos = home_page.esperar_elemento(
            (AppiumBy.XPATH, "//android.widget.RadioButton[@content-desc='Archivos']"), 
            timeout=5
        )
        if archivos:
            archivos.click()
            time.sleep(2)
            print("[OK] Archivos seleccionado")
        
        print("[Test] Regresar a lista de trámites")
        driver.back()
        time.sleep(2)
    
    print("[Test] Regresar a pantalla de Trámites")
    driver.back()
    time.sleep(2)
    
    print("[Test] Click en segundo Ver todo (Dependencias)")
    ver_todo_2 = home_page.esperar_elemento(
        (AppiumBy.XPATH, "(//android.widget.Button[@content-desc='Ver todo'])[2]"), 
        timeout=5
    )
    if ver_todo_2:
        ver_todo_2.click()
        time.sleep(2)
        print("[OK] Ver todo clicked")
    
    print("[Test] Ingresar a cada dependencia")
    
    print("[Test] Click en Instituto Municipal de la Juventud")
    dependencia_1 = home_page.esperar_elemento(
        (AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='Instituto Municipal de la Juventud']"), 
        timeout=5
    )
    if dependencia_1:
        dependencia_1.click()
        time.sleep(3)
        print("[OK] Dependencia abierta")
        driver.back()
        time.sleep(2)
    
    print("[Test] Click en Secretaria de servicios publicos municipales")
    dependencia_2 = home_page.esperar_elemento(
        (AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='Secretaria de servicios publicos municipales']"), 
        timeout=5
    )
    if dependencia_2:
        dependencia_2.click()
        time.sleep(3)
        print("[OK] Dependencia abierta")
        driver.back()
        time.sleep(2)
    
    print("[Test] Click en Secretaría de Administración")
    dependencia_3 = home_page.esperar_elemento(
        (AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='Secretaría de Administración']"), 
        timeout=5
    )
    if dependencia_3:
        dependencia_3.click()
        time.sleep(3)
        print("[OK] Dependencia abierta")
        driver.back()
        time.sleep(2)
    
    print("[Test] Regresar a inicio (2 driver.back)")
    driver.back()
    time.sleep(2)
    driver.back()
    time.sleep(2)
    
    print("[Test] PASSED")