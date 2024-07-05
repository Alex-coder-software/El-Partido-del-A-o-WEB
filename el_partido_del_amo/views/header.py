import reflex as rx
from el_partido_del_amo.styles.styles import Size
from el_partido_del_amo.styles.colors import TextColor
import el_partido_del_amo.constants as constants

def header() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.center(
                rx.link(
                    rx.text.em(
                        "¡En vivo en Youtube!",
                        align="center",
                        spacing="3",
                        width="100%",
                        as_="label",
                        font_size=f"{Size.SMALL.value}rem",  # Ajusta el tamaño del texto
                        font_weight="bold",  # Opcional: para hacer el texto más visible
                    ),
                    href=constants.YOUTUBE_URL,
                    is_external=True,
                    color_scheme="indigo",
                    margin_top=Size.SMALL.value,
                    _hover={
                        "color": TextColor.PRIMARY.value,  # Cambia el color al pasar el mouse
                        "text_decoration": "underline",  # Agrega subrayado al pasar el mouse
                    },
                    margin_bottom=Size.ZERO.value # Ajusta el margen inferior
                ),
            ),
            rx.center(
                rx.image(
                    src="header_logo.png",
                    alt="Logo de El Partido del Año",
                    width="600px",
                    height="auto",
                    border_radius="15px 50px",
                    margin="0rem",
                    padding="0rem"
                ),
            ),
            width="100%",
            align_items="center",  # Centra el contenido horizontalmente
            spacing=Size.ZERO.value,  # Reduce el espaciado entre elementos
            padding_top=f"{Size.SMALL.value}rem",  # Agrega padding superior para separar el header del techo
        ),
        width="100%",
        margin="4px",
        padding="4px",
        trim="normal", 
        align="center", 
        margin_y="105px" 
    )