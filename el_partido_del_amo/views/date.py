import reflex as rx
from el_partido_del_amo.styles.styles import Size
from el_partido_del_amo.styles.colors import Color, TextColor

def date() -> rx.Component:
    return rx.box(
        rx.center(
            rx.box(
                rx.vstack(
                    rx.heading(
                        "El partido comienza en",
                        padding=f"{Size.SMALL.value}rem",
                        trim="normal",
                        margin_y="0",
                        text_align="center",  # Alinear el texto al centro
                        font_size="2.5rem",  # Ajustar el tamaño del heading
                        color=TextColor.ACCENT.value
                    ),
                    rx.text(
                        "",
                        id="countdown",  # Añadir un id para el elemento de la cuenta atrás
                        font_size="3rem",  # Ajustar el tamaño del contador
                        margin_y="0.5rem",  # Reducir el margen superior del contador
                        align="center",
                        text_align="center",  # Alinear el texto al centro
                    ),
                    style={
                        "border": "1px solid white",  # Borde blanco de 1px
                        "padding": "1rem",  # Padding interno del marco
                        "borderRadius": "30px",  # Radio de borde del marco
                        "marginTop": "0",  # Margen superior del marco a cero
                        "marginBottom": f"{Size.SMALL.value}rem",  # Margen inferior del marco
                        "alignItems": "center",  # Centrar elementos verticalmente dentro del marco
                        "width": "100%",  # Ajustar el ancho al contenido
                        "marginLeft": "auto",  # Centrar horizontalmente usando auto margin
                        "marginRight": "auto",  # Centrar horizontalmente usando auto margin
                    },
                    align_items="center",  # Centrar verticalmente los elementos del box
                ),
            ),
            style={
                "display": "flex",
                "justifyContent": "center",
                "alignItems": "center",
                "padding": f"{Size.SMALL.value}rem",  # Padding para centrar el contenido sin ocupar toda la altura
                "height": "auto"  # Altura automática en lugar de 100vh
            }
        ),
        rx.script(src="/js/countdown.js"),  # Incluir el script dentro del contenedor principal
        style={
            "backgroundColor": Color.SECONDARY.value,  # Color de fondo de la vista
            "width": "100vw",  # Ancho completo de la ventana
            "height": "50vh",  # Altura completa de la ventana
            "display": "flex",
            "justifyContent": "center",
            "alignItems": "center",
            "padding": f"{Size.SMALL.value}rem",  # Padding para centrar el contenido
        }
    )