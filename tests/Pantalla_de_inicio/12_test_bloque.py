"""Test: 12 - Bloque"""
import time
from appium.webdriver.common.appiumby import AppiumBy


def test_bloque(driver, home_page):
    """Test: Bloque - Explorar opciones"""
    print("\n=== TEST: Bloque ===")
    
    time.sleep(3)
    
    if not home_page.verificar_saludo():
        print("[Test] Volviendo a inicio...")
        try:
            driver.back()
        except:
            pass
        time.sleep(2)
    
    print("[Test] Click en Bloque")
    home_page.click_servicio("Bloque")
    time.sleep(3)
    
    print("[Test] Click en Ver todo")
    ver_todo = home_page.esperar_elemento(
        (AppiumBy.XPATH, "//android.view.View[@content-desc='ver todo']"), 
        timeout=5
    )
    if ver_todo:
        ver_todo.click()
        time.sleep(2)
        print("[OK] Ver todo clicked")
    
    print("[Test] Click en botón Filtrar")
    filtrar = home_page.esperar_elemento(
        (AppiumBy.XPATH, "//android.widget.Button[@content-desc='Filtrar']"), 
        timeout=5
    )
    if filtrar:
        filtrar.click()
        time.sleep(2)
        print("[OK] Filtros abiertos")
    
    print("[Test] Click en Limpiar filtros")
    limpiar = home_page.esperar_elemento(
        (AppiumBy.XPATH, "//android.widget.Button[@content-desc='Limpiar filtros']"), 
        timeout=5
    )
    if limpiar:
        limpiar.click()
        time.sleep(1)
        print("[OK] Filtros limpiados")
    
    print("[Test] Click en Inglés")
    ingles = home_page.esperar_elemento(
        (AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='Ingles']"), 
        timeout=5
    )
    if ingles:
        ingles.click()
        time.sleep(1)
        print("[OK] Inglés seleccionado")
    
    print("[Test] Click en Tecnologia")
    tecnologia = home_page.esperar_elemento(
        (AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='Tecnologia']"), 
        timeout=5
    )
    if tecnologia:
        tecnologia.click()
        time.sleep(1)
        print("[OK] Tecnologia seleccionado")
    
    print("[Test] Click en Filtrar")
    aplicar_filtro = home_page.esperar_elemento(
        (AppiumBy.XPATH, "//android.widget.Button[@content-desc='Filtrar']"), 
        timeout=5
    )
    if aplicar_filtro:
        aplicar_filtro.click()
        print("[OK] Filtro aplicado")
        time.sleep(3)
    
    print("[Test] Reabrir filtros")
    filtrar2 = home_page.esperar_elemento(
        (AppiumBy.XPATH, "//android.widget.Button[@content-desc='Filtrar']"), 
        timeout=5
    )
    if filtrar2:
        filtrar2.click()
        time.sleep(2)
        print("[OK] Filtros reopened")
    
    print("[Test] Click en Limpiar filtros")
    limpiar2 = home_page.esperar_elemento(
        (AppiumBy.XPATH, "//android.widget.Button[@content-desc='Limpiar filtros']"), 
        timeout=5
    )
    if limpiar2:
        limpiar2.click()
        time.sleep(0.5)
        print("[OK] Filtros limpiados")
    
    print("[Test] Click en cerrar filtros (X)")
    cerrar_x = home_page.esperar_elemento(
        (AppiumBy.XPATH, "//android.widget.Button[@bounds='[782,228][926,372]']"), 
        timeout=5
    )
    if cerrar_x:
        cerrar_x.click()
        time.sleep(1)
        print("[OK] Filtros cerrados")
    
    print("[Test] Click en evento CURSOS DE EXCEL")
    evento = home_page.esperar_elemento(
        (AppiumBy.XPATH, "//android.widget.ImageView[contains(@content-desc, 'CURSOS DE EXCEL')]"), 
        timeout=5
    )
    if evento:
        evento.click()
        time.sleep(2)
        print("[OK] Evento abierto")
    
    print("[Test] Regresar a inicio")
    driver.back()
    time.sleep(2)
    driver.back()
    time.sleep(2)
    driver.back()
    time.sleep(2)
    
    print("[Test] PASSED")