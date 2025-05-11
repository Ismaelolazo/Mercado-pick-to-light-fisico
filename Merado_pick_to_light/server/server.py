# 📁 server/server.py
from flask import Flask, jsonify
import firebase_admin
from firebase_admin import credentials, firestore
import os
import threading
import time

app = Flask(__name__)

# Inicializar Firebase
cred_path = os.path.join(os.path.dirname(__file__), '..', 'firebase', 'picktolight-ae00d-firebase-adminsdk-fbsvc-854efeaaf9.json')
cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred)
db = firestore.client()

# 🧠 Caché en memoria
estado_cache = {}
cache_lock = threading.Lock()

# 🕒 Intervalo de actualización en segundos
ACTUALIZAR_CADA = 20

def actualizar_cache_periodicamente():
    global estado_cache
    while True:
        try:
            doc = db.collection('Guiado').document('EstadoGondolas').get()
            if doc.exists:
                with cache_lock:
                    estado_cache = doc.to_dict()
                print("[CACHE] Estado actualizado")
        except Exception as e:
            print(f"[ERROR CACHE] {e}")
        time.sleep(ACTUALIZAR_CADA)

# Ruta para consultar el estado cacheado
@app.route('/get_status/gondolas/<gondola_id>', methods=['GET'])
def get_gondola_status(gondola_id):
    with cache_lock:
        estado = estado_cache.get(gondola_id, False)
    return jsonify({"estado": 1 if estado else 0})

# Lanzar hilo de actualización de caché al iniciar
if __name__ == '__main__':
    threading.Thread(target=actualizar_cache_periodicamente, daemon=True).start()
    app.run(host='0.0.0.0', port=5000)
