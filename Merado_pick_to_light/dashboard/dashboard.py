# 📁 dashboard/dashboard.py
import panel as pn
import requests
from bokeh.themes import Theme

pn.extension()

# Configuración de usuario y estantes
usuarios = {
    "usuario1": ["A1", "A2", "A3", "A4"],
    "usuario2": ["B1", "B2", "B3", "B4"]
}

# URL del servidor
SERVER_URL = "http://localhost:5000"

# Función para actualizar el color del estante
def enviar_color(usuario, estante, color):
    try:
        r = requests.post(f"{SERVER_URL}/update_status/{usuario}/{estante}", json={"color": color})
        print(f"[{usuario} - {estante}] -> {color}: {r.status_code}")
    except Exception as e:
        print(f"Error al enviar color: {e}")

# Crear interfaz gráfica por usuario
panels = []

for usuario, estantes in usuarios.items():
    estantes_widgets = []
    for estante in estantes:
        botones = pn.Row(
            pn.widgets.Button(name="Apagar", button_type="default", width=70),
            pn.widgets.Button(name="Verde", button_type="success", width=70),
            pn.widgets.Button(name="Azul", button_type="primary", width=70),
            pn.widgets.Button(name="Rojo", button_type="danger", width=70)
        )

        def callback_generator(usuario, estante, color):
            return lambda event: enviar_color(usuario, estante, color)

        botones[0].on_click(callback_generator(usuario, estante, "off"))
        botones[1].on_click(callback_generator(usuario, estante, "green"))
        botones[2].on_click(callback_generator(usuario, estante, "blue"))
        botones[3].on_click(callback_generator(usuario, estante, "red"))

        estantes_widgets.append(pn.Column(f"**{estante}**", botones))

    panel_usuario = pn.Column(f"### {usuario.upper()}", *estantes_widgets)
    panels.append(panel_usuario)

# Agregar lista de productos y funcionalidad de selección
productos = ["Carne", "Frutas", "Verduras", "Lácteos", "Panadería"]

# Función para manejar la selección de productos
def seleccionar_producto(event):
    producto = event.new
    try:
        r = requests.post(f"{SERVER_URL}/select_product", json={"producto": producto})
        print(f"Producto seleccionado: {producto} -> {r.status_code}")
    except Exception as e:
        print(f"Error al seleccionar producto: {e}")

# Widget para seleccionar productos
producto_selector = pn.widgets.Select(name="Seleccionar Producto", options=productos, width=300)
producto_selector.param.watch(seleccionar_producto, 'value')

# Actualización para eliminar el argumento 'style' no válido en pn.pane.Markdown
header = pn.pane.Markdown(
    """# Bienvenido al Mercado Pick to Light
    ### Seleccione un producto para ser guiado al puesto correspondiente mediante LEDs.
    """,
    align="center"
)

footer = pn.pane.Markdown(
    """---
    **Nota:** Este sistema utiliza tecnología ESP32 y LEDs para guiar a los clientes.
    """,
    align="center"
)

# Eliminar el argumento 'background' y aplicar estilos mediante CSS
css = """
body {
    background-color: #ecf0f1;
}
"""

pn.extension(raw_css=[css])

dashboard = pn.Column(
    header,
    pn.Spacer(height=20),
    pn.Row(
        pn.Spacer(width=200),
        producto_selector,
        pn.Spacer(width=200),
    ),
    pn.Spacer(height=50),
    footer,
    sizing_mode="stretch_width"
)

dashboard.servable()

# Si se ejecuta directamente
if __name__ == '__main__':
    pn.serve(dashboard, title="Mercado Pick to Light")