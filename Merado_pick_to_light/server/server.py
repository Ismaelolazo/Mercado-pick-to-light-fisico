# 📁 server/server.py
from flask import Flask, jsonify
import firebase_admin
from firebase_admin import credentials, firestore
import os

app = Flask(__name__)

# Inicializar Firebase
cred_path = os.path.join(os.path.dirname(__file__), '..', 'firebase', 'parqueosupreme-firebase-adminsdk-i836b-44b7396c40.json')
cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred)
db = firestore.client()

# Ruta para consultar si una góndola debe encenderse
@app.route('/get_status/gondolas/<gondola_id>', methods=['GET'])
def get_gondola_status(gondola_id):
    try:
        doc_ref = db.collection('Guiado').document('EstadoGondolas')
        doc = doc_ref.get()
        if doc.exists:
            data = doc.to_dict()
            estado = 1 if data.get(gondola_id) else 0
            return jsonify({"estado": estado})
        else:
            return jsonify({"estado": 0}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)