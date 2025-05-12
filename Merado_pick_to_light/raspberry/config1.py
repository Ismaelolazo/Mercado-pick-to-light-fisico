# 📁 raspberry/config.py
from machine import Pin

# Mapeo de pines según tu asignación final
# Verde (derecha), Azul (izquierda)
gondolas = {
    # Izquierda - Azules
    "G13": Pin(0, Pin.OUT),   # V1
    "G14": Pin(1, Pin.OUT),   # V2
    "G15": Pin(2, Pin.OUT),   # V3
    "G17": Pin(14, Pin.OUT),  # V4
    "G16": Pin(15, Pin.OUT),  # V5

    # Derecha - Verdes
    "G19": Pin(28, Pin.OUT),  # A1
    "G20": Pin(27, Pin.OUT),  # A2
    "G24": Pin(26, Pin.OUT),  # A3
    "G21": Pin(22, Pin.OUT),  # A3
    "G23": Pin(19, Pin.OUT),  # A4
    "G22": Pin(18, Pin.OUT),  # A5
    "G25": Pin(17, Pin.OUT),  # A6
    "G26": Pin(16, Pin.OUT),  # R6
}


