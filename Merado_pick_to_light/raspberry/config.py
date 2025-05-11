# 📁 raspberry/config.py
from machine import Pin

# Mapeo de pines según tu asignación final
# Verde (derecha), Azul (izquierda)
gondolas = {
    # Izquierda - Azules
    "G01": Pin(0, Pin.OUT),   # V1
    "G02": Pin(1, Pin.OUT),   # V2
    "G03": Pin(2, Pin.OUT),   # V3
    "G04": Pin(13, Pin.OUT),  # V4
    "G05": Pin(14, Pin.OUT),  # V5
    "G06": Pin(15, Pin.OUT),  # V6

    # Derecha - Verdes
    "G07": Pin(28, Pin.OUT),  # A1
    "G08": Pin(27, Pin.OUT),  # A2
    "G09": Pin(26, Pin.OUT),  # A3
    "G10": Pin(19, Pin.OUT),  # A4
    "G11": Pin(18, Pin.OUT),  # A5
    "G12": Pin(17, Pin.OUT),  # A6
    "G18": Pin(16, Pin.OUT),  # R6
}

