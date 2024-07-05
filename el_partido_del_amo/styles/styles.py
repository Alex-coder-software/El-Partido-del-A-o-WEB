import reflex as rx
from enum import Enum
from el_partido_del_amo.styles.fonts import Font
from el_partido_del_amo.styles.colors import TextColor, Color

STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Kanit:wght@200&display=swap"
]

BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "color": TextColor.PRIMARY.value,
    "background": Color.PRIMARY.value
}

GLOBAL_STYLES = {
    "body, html": {
        "margin": "0",
        "padding": "0",
        "overflow-x": "hidden",  # Prevenir el desbordamiento horizontal
        "width": "100%",
        "box-sizing": "border-box",
    },
    "*": {
        "boxSizing": "border-box",  # Asegurar que padding y border se incluyan en el tamaño total
    },
}

class Size(Enum):
    ZERO = "0"
    SMALLER = "1.5"
    SMALL = "2"
    DEFAULT = "4"
    MEDIUM = "6"
    BIG = "8"
    VERY_BIG = "9"

content_in_the_center_style_1={
    "display": "flex",
    "justifyContent": "center",
    "alignItems": "center",
    "padding": f"{Size.SMALL.value}rem",  # Padding para centrar el contenido sin ocupar toda la altura
    "height": "auto",  # Altura automática en lugar de 100vh
    "marginLeft": "auto",  # Centrar horizontalmente usando auto margin
    "marginRight": "auto",  # Centrar horizontalmente usando auto margin
    }


content_in_the_center_style = {
    "display": "flex",
    "flexDirection": "column",
    "alignItems": "center",
    "justifyContent": "center",
    "width": "100%",
    "padding": "1rem",
    "@media (max-width: 768px)": {
        "heading": {
            "font_size": "1.5rem"
        },
        "text": {
            "font_size": "0.875rem"
        },
        "image": {
            "width": "100%",
            "max_width": "200px"
        }
    }
}