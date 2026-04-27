"""Localizadores por pagina"""
from appium.webdriver.common.appiumby import AppiumBy


class LoginLocators:
    CAMPO_EMAIL = (AppiumBy.XPATH, "//android.widget.EditText[contains(@hint, 'email')]")
    CAMPO_PASSWORD = (AppiumBy.XPATH, "//android.widget.EditText[contains(@hint, 'contrase')]")
    BOTON_ENTRAR = (AppiumBy.XPATH, "//android.widget.Button[@content-desc='Entrar a Mediplanner']")


class HomeLocators:
    TAB_INICIO = (AppiumBy.ACCESSIBILITY_ID, "Inicio\nPestaña 1 de 5")
    TAB_MEDICOS = (AppiumBy.ACCESSIBILITY_ID, "Médicos\nPestaña 2 de 5")
    TAB_CONSULTAS = (AppiumBy.ACCESSIBILITY_ID, "Consultas\nPestaña 3 de 5")
    TAB_MEDICINAS = (AppiumBy.ACCESSIBILITY_ID, "Medicinas\nPestaña 4 de 5")
    TAB_ESTUDIOS = (AppiumBy.ACCESSIBILITY_ID, "Estudios\nPestaña 5 de 5")
    MENU_PERFIL = (AppiumBy.XPATH, "//android.view.View[@bounds='[48,192][538,366]']")
    PERFIL = (AppiumBy.ACCESSIBILITY_ID, "Perfil\nPestaña de 5")


class MedicinesLocators:
    BOTON_AGREGAR = (AppiumBy.XPATH, "//android.widget.Button[@bounds='[1136,168][1280,312]']")
    CAMPO_BUSCAR = (AppiumBy.XPATH, "//android.widget.EditText[@hint='Busca o escribe el nombre del medicamento']")
    BOTON_SELECCIONAR = (AppiumBy.XPATH, "//android.widget.Button[@content-desc='Seleccionar']")
    
    PRESENTACIONES = {
        "Tabletas": (AppiumBy.XPATH, "//android.view.View[@content-desc='Tabletas']"),
        "Suspension": (AppiumBy.XPATH, "//android.view.View[@content-desc='Suspension']"),
        "Capsulas": (AppiumBy.XPATH, "//android.view.View[@content-desc='Capsulas']"),
        "Ampolleta": (AppiumBy.XPATH, "//android.view.View[@content-desc='Ampolleta']"),
    }
    
    UNIDADES = {
        "miligramos": (AppiumBy.XPATH, "//android.view.View[@content-desc='miligramos']"),
        "mililitros": (AppiumBy.XPATH, "//android.view.View[@content-desc='mililitros']"),
        "gotas": (AppiumBy.XPATH, "//android.view.View[@content-desc='gotas']"),
    }
    
    VIAS = {
        "Oral": (AppiumBy.XPATH, "//android.view.View[@content-desc='Oral']"),
        "Subcutanea": (AppiumBy.XPATH, "//android.view.View[@content-desc='Subcutanea']"),
        "Intramuscular": (AppiumBy.XPATH, "//android.view.View[@content-desc='Intramuscular']"),
    }
    
    BOTON_SIGUIENTE = (AppiumBy.XPATH, "//android.widget.Button[@content-desc='Siguiente']")
    BOTON_FINALIZAR = (AppiumBy.XPATH, "//android.widget.Button[@content-desc='Finalizar']")


class PerfilLocators:
    BOTON_AGREGAR_DEPENDIENTE = (AppiumBy.XPATH, "//android.widget.Button[@content-desc='Agregar dependiente']")
    CAMPO_NOMBRE = (AppiumBy.XPATH, "//android.widget.EditText[@bounds='[48,977][1232,1121]']")
    CAMPO_APELLIDO_P = (AppiumBy.XPATH, "//android.widget.EditText[@bounds='[48,1229][1232,1373]']")
    CAMPO_APELLIDO_M = (AppiumBy.XPATH, "//android.widget.EditText[@bounds='[48,1481][1232,1625]']")
    CAMPO_FECHA = (AppiumBy.XPATH, "//android.widget.EditText[@bounds='[48,1733][1232,1877]']")
    BOTON_SEXO = (AppiumBy.XPATH, "//android.widget.Button[@bounds='[48,1985][1232,2129]']")
    BOTON_PARENTESCO = (AppiumBy.XPATH, "//android.widget.Button[@bounds='[48,2237][1232,2381]']")
    BOTON_CONTINUAR = (AppiumBy.XPATH, "//android.widget.Button[@content-desc='Continuar']")


class CommonLocators:
    BOTON_ATRAS = (AppiumBy.XPATH, "//android.widget.Button[@bounds='[12,168][156,312]']")