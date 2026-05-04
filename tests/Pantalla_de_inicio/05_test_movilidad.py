"""Test: 05 - Movilidad"""
import time
from appium.webdriver.common.appiumby import AppiumBy


def test_movilidad(driver, home_page):
    """Test: Movilidad - Explorar opciones"""
    print("\n=== TEST: Movilidad ===")
    
    time.sleep(3)
    
    if not home_page.verificar_saludo():
        print("[Test] Volviendo a inicio...")
        try:
            driver.back()
        except:
            pass
        time.sleep(2)
    
    print("[Test] Click en Movilidad")
    home_page.click_servicio("Movilidad")
    time.sleep(3)
    
    print("[Test] Verificar mapa")
    page_source = driver.page_source
    assert "Mapa" in page_source or "Google" in page_source
    print("[OK] Mapa cargado")
    
    print("[Test] Click en Ver lista")
    ver_lista = home_page.esperar_elemento(
        (AppiumBy.XPATH, "//android.view.View[@content-desc='Ver lista']"), 
        timeout=5
    )
    if ver_lista:
        ver_lista.click()
        time.sleep(2)
        print("[OK] Lista abierta")
    
    print("[Test] Scroll en lista")
    home_page.scroll_abajo(500)
    time.sleep(1)
    home_page.scroll_abajo(500)
    time.sleep(1)
    
    print("[Test] Click en elemento de la lista")
    elementos = driver.find_elements(AppiumBy.XPATH, "//android.widget.ImageView[contains(@content-desc, 'Restaurantes')]")
    if elementos:
        elementos[0].click()
        time.sleep(2)
        print("[OK] Elemento abierto")
        
        print("[Test] Click en mapa para cerrar lista")
        mapa = driver.find_element(AppiumBy.XPATH, "//android.view.TextureView[@content-desc='Mapa de Google']")
        mapa.click()
        time.sleep(2)
        print("[OK] Lista cerrada")
    
    print("[Test] Verificar lista cerrada")
    ver_lista_check = home_page.esperar_elemento(
        (AppiumBy.XPATH, "//android.view.View[@content-desc='Ver lista']"), 
        timeout=5
    )
    if ver_lista_check:
        print("[OK] Lista cerrada - continuando con filtros")
    
    print("[Test] Click en filtro QroBus")
    qrobus = home_page.esperar_elemento(
        (AppiumBy.XPATH, "//android.view.View[@content-desc='QroBus']"), 
        timeout=5
    )
    if qrobus:
        qrobus.click()
        time.sleep(3)
        print("[OK] Filtro QroBus aplicado")
    
    print("[Test] Click en filtro Ver todo para restaurar")
    ver_todo = home_page.esperar_elemento(
        (AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='Ver todo']"), 
        timeout=5
    )
    if ver_todo:
        ver_todo.click()
        time.sleep(3)
        print("[OK] Filtro Ver todo aplicado")
    
    print("[Test] Click en filtro Culturales")
    culturales = home_page.esperar_elemento(
        (AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='Culturales']"), 
        timeout=5
    )
    if culturales:
        culturales.click()
        time.sleep(3)
        print("[OK] Filtro Culturales aplicado")
    
    print("[Test] Click en filtro Ver todo para restaurar")
    ver_todo = home_page.esperar_elemento(
        (AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='Ver todo']"), 
        timeout=5
    )
    if ver_todo:
        ver_todo.click()
        time.sleep(3)
        print("[OK] Filtro Ver todo aplicado")
    
    print("[Test] Click en filtro Estac.")
    estac = home_page.esperar_elemento(
        (AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='Estac.']"), 
        timeout=5
    )
    if estac:
        estac.click()
        time.sleep(3)
        print("[OK] Filtro Estac. aplicado")
    
    print("[Test] Click en marcador del mapa")
    marcador = home_page.esperar_elemento(
        (AppiumBy.XPATH, "//android.view.View[@content-desc='Marcador de mapa']"), 
        timeout=5
    )
    if marcador:
        marcador.click()
        time.sleep(3)
        print("[OK] Info del marcador abierta")
        
        print("[Test] Click en mapa para cerrar info")
        mapa = driver.find_element(AppiumBy.XPATH, "//android.view.TextureView[@content-desc='Mapa de Google']")
        mapa.click()
        time.sleep(2)
        print("[OK] Info del marcador cerrada")
    
    print("[Test] Regresar a inicio")
    driver.back()
    time.sleep(2)
    
    print("[Test] PASSED")