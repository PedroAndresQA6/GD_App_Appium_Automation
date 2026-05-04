"""Localizadores por pagina - Gobierno Digital"""
from appium.webdriver.common.appiumby import AppiumBy


class GDLocators:
    SALUDO = (AppiumBy.ACCESSIBILITY_ID, "Hola Pedro Andrés")
    PREGUNTA = (AppiumBy.ACCESSIBILITY_ID, "¿Cómo te puedo ayudar hoy?")
    TITULO_SERVICIOS = (AppiumBy.ACCESSIBILITY_ID, "Servicios")
    TITULO_TE_PODRIA_INTERESAR = (AppiumBy.ACCESSIBILITY_ID, "Te podría interesar")

    SERVICIOS = {
        "070_Digital": (AppiumBy.ACCESSIBILITY_ID, "070 Digital"),
        "Programas": (AppiumBy.ACCESSIBILITY_ID, "Programas"),
        "DIF": (AppiumBy.ACCESSIBILITY_ID, "DIF"),
        "Movilidad": (AppiumBy.ACCESSIBILITY_ID, "Movilidad"),
        "Turismo": (AppiumBy.ACCESSIBILITY_ID, "Turismo"),
        "Cultura": (AppiumBy.ACCESSIBILITY_ID, "Cultura"),
        "Bienestar_Animal": (AppiumBy.ACCESSIBILITY_ID, "Bienestar Animal"),
        "Deporte": (AppiumBy.ACCESSIBILITY_ID, "Deporte"),
        "Noticias": (AppiumBy.ACCESSIBILITY_ID, "Noticias"),
        "Oficinas": (AppiumBy.ACCESSIBILITY_ID, "Oficinas"),
        "Bloque": (AppiumBy.ACCESSIBILITY_ID, "Bloque"),
        "Trámites": (AppiumBy.ACCESSIBILITY_ID, "Trámites"),
    }

    TAB_INICIO = (AppiumBy.ACCESSIBILITY_ID, "Inicio\nPestaña 1 de 4")
    TAB_EXPLORAR = (AppiumBy.ACCESSIBILITY_ID, "Explorar\nPestaña 2 de 4")
    TAB_NOTIFICACIONES = (AppiumBy.ACCESSIBILITY_ID, "Notificaciones\nPestaña 3 de 4")
    TAB_CREDENCIAL = (AppiumBy.ACCESSIBILITY_ID, "Credencial\nPestaña 4 de 4")


class CommonLocators:
    BOTON_ATRAS = (AppiumBy.ACCESSIBILITY_ID, "Atrás")


class Digital070Locators:
    BOTON_REPORTAR = (AppiumBy.ACCESSIBILITY_ID, "REPORTAR")
    OPCION_ATENCION_CIUDADANA = (AppiumBy.ACCESSIBILITY_ID, "Prueba - Atención Ciudadana: Expediente único")
    TITULO_CREAR_REPORTE = (AppiumBy.ACCESSIBILITY_ID, "Crear Reporte")
    CAMPO_REPORTE = (AppiumBy.XPATH, "//android.widget.EditText[@hint='REPORTE']")
    BOTON_ENVIAR = (AppiumBy.ACCESSIBILITY_ID, "ENVIAR")
    CAMPO_UBICACION = (AppiumBy.ACCESSIBILITY_ID, "Ubicación")
    CAMPO_IDENTIFICACION = (AppiumBy.ACCESSIBILITY_ID, "IDENTIFICACIÓN OFICIAL")
    CAMPO_COMPROBANTE = (AppiumBy.ACCESSIBILITY_ID, "COMPROBANTE DE DOMICILIO")
    AGREGAR_ARCHIVOS = (AppiumBy.ACCESSIBILITY_ID, "Agregar archivos")
    BOTON_TOMAR_FOTO = (AppiumBy.XPATH, "//android.view.View[@bounds='[520,2520][760,2760]']")
    TITULO_DETALLE = (AppiumBy.ACCESSIBILITY_ID, "Detalle")
    BOTON_CERRAR = (AppiumBy.XPATH, "//android.widget.Button[@bounds='[1136,168][1280,312]']")
    BOTON_AGREGAR = (AppiumBy.XPATH, "//android.widget.Button[@bounds='[1130,165][1280,315]']")
    BOTON_CERRAR_POPUP = (AppiumBy.ACCESSIBILITY_ID, "Cerrar")
    OPCION_REPORTE_2 = (AppiumBy.XPATH, "//android.widget.ImageView[@bounds='[48,765][1232,969]']")
    OPCION_PRUEBA_27 = (AppiumBy.ACCESSIBILITY_ID, "PRUEBA 27")
    OPCION_PRUEBA_6_ENERO = (AppiumBy.ACCESSIBILITY_ID, "prueba 6 de enero 2026")
    CAMPO_CURP = (AppiumBy.XPATH, "//android.widget.EditText[@hint='CURP']")