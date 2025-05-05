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

# Mapeo de productos a estantes
producto_a_estante = {
    "Carne": ("usuario1", "A1"),
    "Frutas": ("usuario1", "A2"),
    "Verduras": ("usuario2", "B1"),
    "Lácteos": ("usuario2", "B2"),
    "Panadería": ("usuario1", "A3")
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

@app.route('/select_product', methods=['POST'])
def select_product():
    data = request.get_json()
    producto = data.get("producto")

    if producto not in producto_a_estante:
        return jsonify({"error": "Producto no válido"}), 400

    usuario, estante = producto_a_estante[producto]

    # Apagar todos los LEDs primero
    for user, estantes in estado_guiado.items():
        for est in estantes:
            estado_guiado[user][est]["color"] = "off"

    # Encender el LED del estante correspondiente
    estado_guiado[usuario][estante]["color"] = "green"

    return jsonify({"status": "OK", "producto": producto, "usuario": usuario, "estante": estante})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)