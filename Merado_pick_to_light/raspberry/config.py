# 📁 raspberry/config.py
from machine import Pin

# Configuración física por góndola, sin relación con usuarios
# Este archivo es para el PRIMER protoboard (rasp1), que controlará G01–G10

# Mapeo de góndolas reales a pines GPIO del Raspberry Pi Pico W
# Asegúrate de conectar físicamente los LEDs a estos pines

gondolas = {
    "G01": Pin(0, Pin.OUT),
    "G02": Pin(1, Pin.OUT),
    "G03": Pin(2, Pin.OUT),
    "G04": Pin(3, Pin.OUT),
    "G05": Pin(4, Pin.OUT),
    "G06": Pin(5, Pin.OUT),
    "G07": Pin(6, Pin.OUT),
    "G08": Pin(7, Pin.OUT),
    "G09": Pin(8, Pin.OUT),
    "G10": Pin(9, Pin.OUT)
}

