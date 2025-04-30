# 📁 server/server.py
from flask import Flask, request, jsonify

app = Flask(__name__)

# Diccionario de estados para cada usuario y estante
estado_guiado = {
    "usuario1": {
        "A1": {"color": "off"},
        "A2": {"color": "off"},
        "A3": {"color": "off"},
        "A4": {"color": "off"}
    },
    "usuario2": {
        "B1": {"color": "off"},
        "B2": {"color": "off"},
        "B3": {"color": "off"},
        "B4": {"color": "off"}
    }
}

@app.route('/get_status/<usuario>/<estante>', methods=['GET'])
def get_status(usuario, estante):
    try:
        color = estado_guiado[usuario][estante]["color"]
        return jsonify({"color": color})
    except KeyError:
        return jsonify({"error": "Usuario o estante no válido"}), 404

@app.route('/update_status/<usuario>/<estante>', methods=['POST'])
def update_status(usuario, estante):
    data = request.get_json()
    color = data.get("color", "off")
    try:
        estado_guiado[usuario][estante]["color"] = color
        return jsonify({"status": "OK", "color": color})
    except KeyError:
        return jsonify({"error": "Usuario o estante no válido"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)