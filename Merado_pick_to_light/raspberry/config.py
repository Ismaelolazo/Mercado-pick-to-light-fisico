# 📁 raspberry/config.py
from machine import Pin

# Definimos los pines RGB para cada estante por usuario
# Puedes cambiar los pines según cómo los tengas conectados
users_config = {
    "usuario1": {
        "A1": {"r": Pin(2, Pin.OUT), "g": Pin(3, Pin.OUT), "b": Pin(4, Pin.OUT)},
        "A2": {"r": Pin(5, Pin.OUT), "g": Pin(6, Pin.OUT), "b": Pin(7, Pin.OUT)},
        "A3": {"r": Pin(8, Pin.OUT), "g": Pin(9, Pin.OUT), "b": Pin(10, Pin.OUT)},
        "A4": {"r": Pin(11, Pin.OUT), "g": Pin(12, Pin.OUT), "b": Pin(13, Pin.OUT)},
    },
    "usuario2": {
        "B1": {"r": Pin(14, Pin.OUT), "g": Pin(15, Pin.OUT), "b": Pin(16, Pin.OUT)},
        "B2": {"r": Pin(17, Pin.OUT), "g": Pin(18, Pin.OUT), "b": Pin(19, Pin.OUT)},
        "B3": {"r": Pin(20, Pin.OUT), "g": Pin(21, Pin.OUT), "b": Pin(22, Pin.OUT)},
        "B4": {"r": Pin(26, Pin.OUT), "g": Pin(27, Pin.OUT), "b": Pin(28, Pin.OUT)},
    }
}