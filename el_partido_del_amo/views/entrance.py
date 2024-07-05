import reflex as rx
from el_partido_del_amo.styles.styles import Size
from el_partido_del_amo.styles.styles import content_in_the_center_style, content_in_the_center_style_1
from el_partido_del_amo.styles.colors import TextColor
import el_partido_del_amo.constants as constants

def entrance() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.center(
                rx.heading(
                    "¡Entradas a la venta!",
                    font_size=f"{Size.DEFAULT.value}rem",  # Ajustar el tamaño del heading
                    text_align="center",  # Alinear el heading al centro
                    margin_bottom=f"{Size.DEFAULT.value}rem",  # Añadir margen inferior al heading
                    margin_y=f"{Size.SMALL.value}rem",
                    style={
                        "@media (max-width: 768px)": {
                            "font_size": "1.5rem"
                            }
                        }
                ),
                style=content_in_the_center_style_1
            ),
            rx.center(
                rx.image(
                    src="entrances.png",
                    alt="Logo de entrada con fondo transparente",
                    width="300px",  # Ajustar el tamaño de la imagen
                    height="auto",
                    max_width="300px",
                    margin_y=Size.SMALL.value  # Añadir margen vertical a la imagen
                ),
                style=content_in_the_center_style_1
            ),
            rx.hstack(
                rx.text(
                    "Puedes comprarlas en físico en Calle Maliz 10 o en digital en ",
                    font_size=f"{Size.SMALL.value}rem",  # Ajustar el tamaño del texto
                    text_align="center",  # Alinear el texto al centro
                ),
                rx.link(
                    "https://balanzofit.com/",
                    href=constants.WEB_URL,  
                    is_external=True,
                    style={
                        "font_size": f"{Size.SMALL.value}rem", 
                        "text_align": "center",
                        "display": "inline",  # Hacer el enlace un bloque para centrarlo
                    },  # Ajustar el tamaño y alinear el enlace
                ),
                wrap="wrap",  # Permitir que el contenido se ajuste en varias líneas si es necesario
                justify="center"
            ),
            rx.hstack(
                    rx.text(
                        "Quedan ",
                        font_size=f"{Size.SMALL.value}rem",  # Ajustar el tamaño del texto
                        text_align="center"  # Alinear el texto al centro
                    ),
                    rx.text(
                        "1000 ",
                        color=TextColor.ACCENT.value,
                        font_size=f"{Size.SMALL.value}rem",  # Ajustar el tamaño del texto
                        text_align="center"  # Alinear el texto al centro
                    ),
                    rx.text(
                        "entradas, ¡hazte con la tuya!",
                        font_size=f"{Size.SMALL.value}rem",  # Ajustar el tamaño del texto
                        text_align="center"  # Alinear el texto al centro
                    ),
                spacing=Size.DEFAULT.value,  # Añadir espacio entre los textos
                wrap="wrap",  # Permitir que el contenido se ajuste en varias líneas si es necesario
                justify="center"
                ),
            spacing=Size.BIG.value,  # Añadir espacio entre todos los elementos
            margin_y=f"{Size.SMALL.value}rem"
        ),
        style=content_in_the_center_style_1
    )