"""Pytest configuration and fixtures"""
import pytest
import os
import sys
from appium import webdriver
from appium.options.android import UiAutomator2Options
from config.settings import Settings


sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


@pytest.fixture(scope="session")
def credenciales():
    """Credenciales de acceso"""
    return Settings.CREDENTIALS


@pytest.fixture(scope="session")
def appium_server_url():
    """URL del servidor Appium"""
    return Settings.APPIUM_URL


def obtener_dispositivo():
    """Obtiene el dispositivo Android conectado"""
    try:
        import subprocess
        result = subprocess.run(["adb", "devices"], capture_output=True, text=True, timeout=10)
        lines = result.stdout.strip().split('\n')
        devices = [line.split()[0] for line in lines[1:] if line.strip() and 'device' in line]
        for device in devices:
            if '5554' in device:
                return device
        return devices[0] if devices else "emulator-5554"
    except:
        return "emulator-5554"


@pytest.fixture(scope="session")
def device_name():
    """Nombre del dispositivo"""
    return Settings.ANDROID_DEVICE


def obtener_opciones(device_name):
    """Obtiene las opciones del driver"""
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.device_name = device_name
    options.app_package = Settings.APP_PACKAGE
    options.app_activity = Settings.APP_ACTIVITY
    options.no_reset = Settings.NO_RESET
    options.full_reset = Settings.FULL_RESET
    options.set_capability("autoGrantPermissions", Settings.AUTO_GRANT_PERMISSIONS)
    options.set_capability("enforceXPath1", True)
    options.set_capability("skipUnlock", True)
    options.set_capability("newCommandTimeout", 300)
    return options


@pytest.fixture(scope="function")
def driver(appium_server_url, device_name):
    """Driver de Appium"""
    options = obtener_opciones(device_name)
    driver = webdriver.Remote(command_executor=appium_server_url, options=options)
    driver.implicitly_wait(Settings.IMPLICIT_WAIT)
    yield driver
    try:
        driver.quit()
    except:
        pass


@pytest.fixture(scope="function")
def login_page(driver):
    """Page Object de Login"""
    from pages.login_page import LoginPage
    return LoginPage(driver)


@pytest.fixture(scope="function")
def home_page(driver):
    """Page Object de Home"""
    from pages.home_page import HomePage
    return HomePage(driver)