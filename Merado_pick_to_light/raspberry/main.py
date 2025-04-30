# 📁 raspberry/main.py
from machine import Pin
import utime
import urequests
from wifi_lib import wifi_init
from config import users_config

# Inicializa WiFi
wifi_init()

# URL del servidor
SERVER_URL = 'http://192.168.0.100:5000'  # ⚠️ cambia esta IP según tu red

# Función para encender LED según color
colors = {
    "off": (0, 0, 0),
    "green": (0, 1, 0),
    "blue": (0, 0, 1),
    "red": (1, 0, 0),
    "yellow": (1, 1, 0),
    "magenta": (1, 0, 1),
    "cyan": (0, 1, 1)
}

def set_led(led_pins, color):
    r, g, b = colors.get(color, (0, 0, 0))
    led_pins["r"].value(r)
    led_pins["g"].value(g)
    led_pins["b"].value(b)

# Bucle principal
while True:
    for user in users_config:
        for estante in users_config[user]:
            led_pins = users_config[user][estante]
            try:
                res = urequests.get(f"{SERVER_URL}/get_status/{user}/{estante}")
                estado = res.json().get("color", "off")
                set_led(led_pins, estado)
                res.close()
            except Exception as e:
                print(f"Error en {user}-{estante}: {e}")
    utime.sleep(1)