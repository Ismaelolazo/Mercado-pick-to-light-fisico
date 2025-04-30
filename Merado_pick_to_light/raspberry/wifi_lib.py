# 📁 raspberry/wifi_lib.py
import network
import time
import rp2
from secrets import secrets  # Debes tener un archivo 'secrets.py' con tus credenciales

def wifi_init():
    rp2.country('DE')  # Puedes cambiarlo según tu país
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    ssid = secrets['NombreDeTuRedWiFi']
    pw = secrets['pw']

    wlan.connect(ssid, pw)

    timeout = 10
    while timeout > 0:
        if wlan.status() >= 3:
            break
        print("Conectando a WiFi...")
        time.sleep(1)
        timeout -= 1

    if wlan.status() != 3:
        raise RuntimeError("Fallo en la conexión WiFi")
    else:
        ip = wlan.ifconfig()[0]
        print(f"Conectado con IP: {ip}")