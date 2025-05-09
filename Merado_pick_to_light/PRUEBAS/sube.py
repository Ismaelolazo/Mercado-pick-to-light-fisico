# subir_estado_gondolas.py
import firebase_admin
from firebase_admin import credentials, firestore
import os

# Ruta del archivo de credenciales
cred_path = os.path.join(os.path.dirname(__file__), '..', 'firebase', 'picktolight-ae00d-firebase-adminsdk-fbsvc-854efeaaf9.json')
cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred)
db = firestore.client()

# Datos simulados: encender G03, G06, G10
estado = {
    "G03": True,
    "G06": True,
    "G10": True
}

# Subir a Firestore
doc_ref = db.collection("Guiado").document("EstadoGondolas")
doc_ref.set(estado)

print("Estado de góndolas subido correctamente.")
