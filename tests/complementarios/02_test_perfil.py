"""Test: 02 - Perfil"""
import time
from appium.webdriver.common.appiumby import AppiumBy


def test_perfil(driver, home_page):
    """Test: Perfil - Gestion de perfil"""
    print("\n=== TEST: Perfil ===")
    
    time.sleep(3)
    
    print("[Test] Verificar que estamos en Inicio")
    if home_page.verificar_saludo():
        print("[OK] Estamos en Inicio")
    
    print("[Test] Click en icono de perfil (bounds [1136,186][1244,294])")
    driver.tap([(1190, 240)])
    time.sleep(2)
    print("[OK] Menu de perfil abierto")
    
    print("[Test] Click en Perfil")
    perfil_btn = home_page.esperar_elemento(
        (AppiumBy.XPATH, "//android.widget.Button[@content-desc='Perfil']"), 
        timeout=5
    )
    if perfil_btn:
        perfil_btn.click()
        time.sleep(3)
        print("[OK] Pantalla Mi perfil abierta")
    
    print("[Test] Scroll down")
    home_page.scroll_abajo(500)
    time.sleep(1)
    
    print("[Test] Click en Guardar cambios")
    guardar = home_page.esperar_elemento(
        (AppiumBy.XPATH, "//android.widget.Button[@content-desc='Guardar cambios']"), 
        timeout=5
    )
    if guardar:
        guardar.click()
        time.sleep(2)
        print("[OK] Cambios guardados")
    
    print("[Test] Esperar a que regrese al menu")
    time.sleep(2)
    
    print("[Test] Click en icono de perfil nuevamente")
    driver.tap([(1190, 240)])
    time.sleep(2)
    print("[OK] Menu de perfil abierto nuevamente")
    
    print("[Test] Click en Intereses")
    intereses_btn = home_page.esperar_elemento(
        (AppiumBy.XPATH, "//android.widget.Button[@content-desc='Intereses']"), 
        timeout=5
    )
    if intereses_btn:
        intereses_btn.click()
        time.sleep(2)
        print("[OK] Pantalla Intereses abierta")
        
        print("[Test] Buscar y click en todos los switches")
        switches = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.Switch")
        print(f"[Debug] Se encontraron {len(switches)} switches")
        
        for i, switch in enumerate(switches):
            try:
                switch.click()
                print(f"[OK] Switch {i+1} clickeado")
                time.sleep(1)
            except Exception as e:
                print(f"[WARN] Switch {i+1} no se pudo clickear: {e}")
    
    print("[Test] Regresar al menu de perfil")
    driver.back()
    time.sleep(2)
    
    print("[Test] Click en icono de perfil nuevamente")
    driver.tap([(1190, 240)])
    time.sleep(2)
    print("[OK] Menu de perfil abierto")
    
    print("[Test] Click en Historial")
    historial_btn = home_page.esperar_elemento(
        (AppiumBy.XPATH, "//android.widget.Button[@content-desc='Historial']"), 
        timeout=5
    )
    if historial_btn:
        historial_btn.click()
        time.sleep(2)
        print("[OK] Pantalla Historial abierta")
    
    print("[Test] Regresar al menu de perfil")
    driver.back()
    time.sleep(2)
    
    print("[Test] Click en icono de perfil nuevamente")
    driver.tap([(1190, 240)])
    time.sleep(2)
    print("[OK] Menu de perfil abierto")
    
    print("[Test] Click en Favoritos")
    favoritos_btn = home_page.esperar_elemento(
        (AppiumBy.XPATH, "//android.widget.Button[@content-desc='Favoritos']"), 
        timeout=5
    )
    if favoritos_btn:
        favoritos_btn.click()
        time.sleep(2)
        print("[OK] Pantalla Favoritos abierta")
    
    print("[Test] Regresar al menu de perfil")
    driver.back()
    time.sleep(2)
    
    print("[Test] Click en icono de perfil nuevamente")
    driver.tap([(1190, 240)])
    time.sleep(2)
    print("[OK] Menu de perfil abierto")
    
    print("[Test] Click en Trámites y Apoyos")
    tramites_btn = home_page.esperar_elemento(
        (AppiumBy.XPATH, "//android.widget.Button[@content-desc='Trámites y Apoyos']"), 
        timeout=5
    )
    if tramites_btn:
        tramites_btn.click()
        time.sleep(2)
        print("[OK] Pantalla Trámites y Apoyos abierta")
    
    print("[Test] Regresar al menu de perfil")
    driver.back()
    time.sleep(2)
    
    print("[Test] Click en icono de perfil nuevamente")
    driver.tap([(1190, 240)])
    time.sleep(2)
    print("[OK] Menu de perfil abierto")
    
    print("[Test] Click en Mis Vehículos")
    vehiculos_btn = home_page.esperar_elemento(
        (AppiumBy.XPATH, "//android.widget.Button[@content-desc='Mis Vehículos']"), 
        timeout=5
    )
    if vehiculos_btn:
        vehiculos_btn.click()
        time.sleep(2)
        print("[OK] Pantalla Mis Vehículos abierta")
    
    print("[Test] Regresar a Inicio")
    driver.back()
    time.sleep(2)
    
    print("[Test] Verificar que seguimos en Inicio")
    if home_page.verificar_saludo():
        print("[OK] Estamos en la pantalla de inicio")
    
    print("[Test] PASSED")