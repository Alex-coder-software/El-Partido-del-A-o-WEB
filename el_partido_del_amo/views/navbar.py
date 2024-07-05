import reflex as rx
from el_partido_del_amo.styles.styles import Size
from el_partido_del_amo.styles.colors import Color
import el_partido_del_amo.constants as constants

def navbar() -> rx.Component:
    return rx.vstack(
            rx.hstack(
                rx.image(
                    src="logo.png",
                    alt="Logo de el Partido del Año",
                    width="100px",
                    height="auto",
                    border_radius="15px 50px",
                ),
                rx.heading(
                    "El Partido del Año",
                    padding=Size.BIG.value,
                    trim="normal",
                    align="center",
                    margin_y="0"
                ),
                rx.spacer(),
                rx.hstack(
                    rx.link(
                        rx.image(
                            src="twitter.png",
                            alt="Logo de Twitter",
                            width="60px",
                            height="0,50rem",
                            margin_right="10px",
                        ),
                        href=constants.TWITTER_URL,
                        is_external=True,
                        margin_bottom=Size.BIG.value
                    ),
                    rx.link(
                        rx.image(
                            src="youtube.jpg",
                            alt="Logo de Youtube",
                            width="60px",
                            height="0,50rem",
                            margin_right="10px",
                        ),
                        href=constants.YOUTUBE_URL,
                        is_external=True,
                        margin_bottom=Size.BIG.value
                    ),
                    rx.link(
                        rx.image(
                            src="instagram.jpg",
                            alt="Logo de Instagram",
                            width="60px",
                            height="0,50rem",
                            margin_right="100px",
                            style={
                            "transition": "width 0.2s",
                            "@media (max-width: 768px)": {
                                "width": "20px"  # Ajusta el tamaño para la vista móvil
                                }
                            }
                        ),
                        href=constants.INSTAGRAM_URL,
                        is_external=True,
                        margin_bottom=Size.BIG.value
                    ),
                    margin_bottom=Size.BIG.value
                ),
                rx.color_mode.button(position="top-right"),
            align_items="center",
            width="100%",
            z_index="9999", # Asegurarse de que la navbar esté en la parte superior
        ),
        z_index="9999", # Asegurarse de que la navbar esté en la parte superior
        position="fixed",
        border_bottom=f"0.45rem solid {Color.SECONDARY.value}",
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        top="0",
        left="0",  
        right="0", 
        width="100%",
        background_color=Color.PRIMARY.value # Esto asegura que la navbar tiene un fondo opaco, lo cual es crucial para evitar que otros elementos la atraviesen visualmente
    )