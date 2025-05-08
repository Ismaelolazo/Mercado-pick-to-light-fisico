from machine import Pin
import utime
import urequests
from wifi_lib import wifi_init
from config import gondolas

# 1. Conexión a WiFi
wifi_init()

# 2. IP local de tu servidor Flask (ej. 192.168.1.5)
SERVER_URL = 'http://192.168.1.5:5000'  # ✅ Asegúrate que esta IP es accesible desde el Pico

# 3. Loop de consulta
while True:
    for gondola_id, led_pin in gondolas.items():
        try:
            url = f"{SERVER_URL}/get_status/gondolas/{gondola_id}"
            response = urequests.get(url)
            estado = response.json().get("estado", 0)
            led_pin.value(1 if estado else 0)
            response.close()
        except Exception as e:
            print(f"[Error] {gondola_id}: {e}")
    utime.sleep(1)

