"""Configuraciones globales del proyecto"""
import os

class Settings:
    APP_NAME = "Gobierno Digital"
    APP_PACKAGE = "com.rymsolutions.gdqro"
    APP_ACTIVITY = ".MainActivity"
    
    APPIUM_HOST = os.environ.get("APPIUM_HOST", "localhost")
    APPIUM_PORT = os.environ.get("APPIUM_PORT", "4723")
    APPIUM_URL = f"http://{APPIUM_HOST}:{APPIUM_PORT}"
    
    IMPLICIT_WAIT = int(os.environ.get("IMPLICIT_WAIT", "10"))
    EXPLICIT_WAIT = int(os.environ.get("EXPLICIT_WAIT", "30"))
    SCREENSHOT_DELAY = int(os.environ.get("SCREENSHOT_DELAY", "2"))
    
    DEFAULT_TIMEOUT = int(os.environ.get("DEFAULT_TIMEOUT", "30"))
    
    SCREENSHOTS_DIR = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "reports", "screenshots"
    )
    
    CREDENTIALS = {
        "email": os.environ.get("GD_EMAIL", "pedro@test.com"),
        "password": os.environ.get("GD_PASSWORD", "password123")
    }
    
    ANDROID_DEVICE = os.environ.get("ANDROID_DEVICE", "emulator-5554")
    
    AUTO_GRANT_PERMISSIONS = os.environ.get("AUTO_GRANT_PERMISSIONS", "true").lower() == "true"
    NO_RESET = True
    FULL_RESET = False