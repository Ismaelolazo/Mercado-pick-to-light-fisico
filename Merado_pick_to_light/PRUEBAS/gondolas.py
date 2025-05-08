import firebase_admin
from firebase_admin import credentials, firestore
import os

# Inicializar Firebase
cred_path = os.path.join(os.path.dirname(__file__), '..', 'firebase', 'picktolight-ae00d-firebase-adminsdk-fbsvc-854efeaaf9.json')
cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred)
db = firestore.client()

# Góndolas a activar (true = encender LED)
estado_gondolas = {
    "G01": True,
    "G03": True,
    "G05": True,
    "G08": True
}

# Subir al documento
doc_ref = db.collection('Guiado').document('EstadoGondolas')
doc_ref.set(estado_gondolas)

print("Estados de góndolas actualizados exitosamente.")