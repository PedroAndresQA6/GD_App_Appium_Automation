"""Datos de prueba"""
from config.settings import Settings


class TestData:
    CREDENTIALS = Settings.CREDENTIALS
    
    NOMBRES_VALIDOS = [
        "Juan", "Pedro", "Carlos", "Luis", "Miguel", "Jose",
        "Maria", "Ana", "Sofia", "Laura", "Kenia", "Elena"
    ]
    
    APELLIDOS = [
        "Garcia", "Martinez", "Rodriguez", "Lopez", "Gonzalez",
        "Perez", "Sanchez", "Ramirez", "Torres", "Flores"
    ]
    
    PARENTESCOS = [
        "Hijo(a)", "Padre", "Madre", "Abuelo(a)", "Primo(a)", 
        "Sobrino(a)", "Tio(a)"
    ]
    
    MEDICAMENTOS = [
        "Paracetamol", "Ibuprofeno", "Amoxicilina", "Omeprazol", 
        "Metformina", "Losartan", "Amlodipino", "Atorvastatina"
    ]
    
    PRESENTACIONES = ["Tabletas", "Suspension", "Capsulas", "Ampolleta"]
    
    UNIDADES = ["miligramos", "mililitros", "gotas"]
    
    VIAS = ["Oral", "Subcutanea", "Intramuscular", "Intravenosa"]
    
    FRECUENCIAS = [
        "Una vez al día", "Dos veces al día", "3 veces al día",
        "Más de 3 veces al día", "Cada x hora"
    ]
    
    DURACIONES = ["5 días", "1 semana", "10 días", "15 días", "30 días"]
    
    DATOS_PERSONALES = {
        "nombre": "Juan",
        "apellido_p": "Garcia",
        "apellido_m": "Martinez",
        "curp": "GAHJ900101HNLRRN01",
        "email": "juan.prueba@test.com",
        "telefono": "5512345678"
    }
    
    MEDICOS_ESPECIALIDADES = [
        "Internista", "Cardiologo", "Pediatra", "Ginecologo",
        "Dermatologo", "Oftalmologo", "Ortopedista", "Neurologo"
    ]
    
    ESTADOS = [
        "Ciudad de Mexico", "Jalisco", "Nuevo Leon", "Queretaro",
        "Puebla", "Veracruz", "Guanajuato"
    ]