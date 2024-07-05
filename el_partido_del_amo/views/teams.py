import reflex as rx
from el_partido_del_amo.styles.styles import Size
from el_partido_del_amo.styles.styles import content_in_the_center_style
from el_partido_del_amo.styles.colors import TextColor, Color
import el_partido_del_amo.constants as constants

def teams() -> rx.Component:
    return rx.center(
            rx.vstack(
                rx.hstack(
                    rx.center(
                        rx.vstack(
                            # Contenedor del Deportivo Alavés
                            rx.heading(
                                "Deportivo Alavés",
                                font_size=f"{Size.SMALL.value}rem",  # Ajustar el tamaño del texto
                                text_align="center",  # Alinear el texto al centro
                                color=TextColor.SECONDARY.value
                            ),
                            rx.text(
                                """El Deportivo Alavés busca ganar la final de la Champions en este grandioso derbi tras una grandiosa temporada. 
                                Entre sus estrellas encontramos al pichichi de la competición, 
                                Samu Omorodion quién viene de marcar hat-trick en las semifinales.
                                """,
                                font_size=f"{Size.SMALLER.value}rem",  # Ajustar el tamaño del texto
                                text_align="start",  # Alinear el texto al centro
                                color=TextColor.SECONDARY.value,
                                style={"fontWeight": "bold"}  # Texto en negrita
                            ),
                            rx.image(
                                src="deportivo_alaves.jpg",
                                alt="Diseño propio de la alineación del Deportivo Alavés",
                                width="300px",  # Ajustar el tamaño de la imagen
                                height="auto",
                                margin_y=Size.DEFAULT.value,  # Añadir margen vertical a la imagen
                                marginRight="auto",
                                marginLeft="auto"
                            )
                        ),
                        style=content_in_the_center_style
                    ),
                    rx.spacer(flex=1), # Añadir espaciador a la izquierda de la imagen central

                    # Imagen central "vs"
                    rx.center(  # Centrar verticalmente la imagen
                        rx.image(
                            src="vs.jpg",
                            alt="Imagen logotipo de \"versus\"",
                            width="20rem",
                            height="auto",
                            margin_y="auto",
                            padding_top=Size.BIG.value
                        ),
                        style={
                        "display": "flex",
                        "justifyContent": "center",
                        "alignItems": "center",
                        "height": "100%",  # Asegurar que el contenedor ocupa toda la altura disponible
                        "flexDirection": "column",  # Añadir esta propiedad para centrar verticalmente
                        "marginRight": "auto",
                        "marginLeft": "auto"
                        }  # Centrar horizontal y verticalmente
                    ),
                    rx.spacer(flex=1), # Añadir espaciador a la derecha de la imagen central

                    # Contenedor de SD Eibar
                    rx.center(
                        rx.vstack(
                            rx.heading(
                                "SD Eibar",
                                font_size=f"{Size.SMALL.value}rem",  # Ajustar el tamaño del texto
                                text_align="center",  # Alinear el texto al centro
                                color=TextColor.SECONDARY.value,
                            ),
                            rx.text(
                                """Por otro lado el Eibar viene de pasar por encima del Milán en las semifinales, 
                                dejando un impactante 7-0 global después de la icónica manita que marcaron en San Siro. 
                                Sin duda alguna su mejor jugador es Corpás, quién tiene el mayor número de asistencias en toda la competición.
                                """,
                                font_size=f"{Size.SMALLER.value}rem",  # Ajustar el tamaño del texto
                                text_align="start",  # Alinear el texto al centro
                                color=TextColor.SECONDARY.value,
                                style={"fontWeight": "bold"}  # Texto en negrita
                            ),
                            rx.image(
                                src="eibar.jpg",
                                alt="Diseño propio de la alineación de la SD Eibar",
                                width="300px",  # Ajustar el tamaño de la imagen
                                height="auto",
                                margin_y=Size.DEFAULT.value,  # Añadir margen vertical a la imagen
                                marginRight="auto",
                                marginLeft="auto"
                            )
                        ),
                        style=content_in_the_center_style
                    ),
            ),
            rx.center(
                rx.text(
                    """El gran choque entre titanes solo puede 
                    dejar un ganador, ¿te lo perderás?
                    """,
                    font_size=f"{Size.SMALLER.value}rem",  # Ajustar el tamaño del texto
                    text_align="start",  # Alinear el texto al centro
                    color=TextColor.SECONDARY.value,
                    style={"fontWeight": "bold"}  # Texto en negrita
                ),
                style=content_in_the_center_style
            )
        ),
        style=content_in_the_center_style,
        bg=Color.TERTIARY.value
    )