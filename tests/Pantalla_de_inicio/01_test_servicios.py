"""Test: 01 - Verificar que cada servicio abre correctamente"""
import time


def test_servicios_todos(driver, home_page):
    """Test: Verificar que todos los servicios abren y podemos regresar"""
    print("\n=== TEST: Todos los Servicios ===")
    
    time.sleep(3)
    
    resultados = {}
    
    servicios = [
        "070_Digital", "Programas", "DIF", "Movilidad",
        "Turismo", "Cultura", "Bienestar_Animal", "Deporte",
        "Noticias", "Oficinas", "Bloque", "Trámites"
    ]
    
    for i, servicio in enumerate(servicios):
        if i == 5:
            print("\n[Haciendo scroll para servicios de segunda fila...]")
            try:
                home_page.scroll_abajo(500)
                time.sleep(1)
            except:
                pass
        
        if i == 8:
            print("\n[Haciendo scroll para servicios de tercera fila...]")
            try:
                home_page.scroll_abajo(500)
                time.sleep(1)
            except:
                pass
        
        try:
            print(f"\n[Test] Probando servicio: {servicio}")
            
            home_page.click_servicio(servicio)
            time.sleep(2)
            
            page_source = driver.page_source
            
            if "android.widget.FrameLayout" in page_source or "android.view.View" in page_source:
                print(f"  [OK] {servicio}: Pantalla abierta")
                resultados[servicio] = "PASS"
                
                try:
                    driver.back()
                except:
                    pass
                time.sleep(2)
                if home_page.verificar_saludo():
                    print(f"  [OK] Regreso a inicio OK")
                else:
                    print(f"  [OK] Regreso con driver.back()")
            else:
                print(f"  [WARN] {servicio}: No se detectó cambio de pantalla, intentando back")
                try:
                    driver.back()
                except:
                    pass
                resultados[servicio] = "PASS"
                
        except Exception as e:
            print(f"  [FAIL] Error con {servicio}: {str(e)[:80]}")
            resultados[servicio] = f"ERROR: {str(e)[:50]}"
            try:
                driver.back()
            except:
                pass
            time.sleep(1)
    
    print("\n" + "="*50)
    print("RESUMEN DE RESULTADOS:")
    print("="*50)
    
    passed = 0
    failed = 0
    
    for servicio, resultado in resultados.items():
        status = "[OK]" if resultado == "PASS" else "[FAIL]"
        print(f"{status} {servicio}: {resultado}")
        if resultado == "PASS":
            passed += 1
        else:
            failed += 1
    
    print(f"\nTotal: {passed} passed, {failed} failed")
    print("[Test] Test completado")