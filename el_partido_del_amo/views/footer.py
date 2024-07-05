import reflex as rx
import el_partido_del_amo.constants as constants
from el_partido_del_amo.styles.styles import Size

def footer() -> rx.Component:
    return rx.center(
        rx.hstack(
            rx.text(
                "© 2024 El Partido del Año | Todos los derechos reservados.",
                margin_left="0px",
                margin_right="0px",
                align_items="start",
                style={
                    #"white-space": "nowrap",
                    "@media (max-width: 768px)": {
                        "font-size": "0.75rem",
                        "margin_left": "0px",
                        "textAlign": "center",
                        "margin_bottom": "5px"  # Reducir espacio inferior en móviles
                    }
                }
            ),
            rx.spacer(flex=1),
            rx.logo(
                margin_left="0px",
                margin_right="0px",
                align_items="center",
                style={
                    "@media (max-width: 768px)": {
                        "margin_left": "0px",
                        "margin_bottom": "5px"  # Reducir espacio inferior en móviles
                    }
                }
            ),
            rx.spacer(flex=1),
            rx.hstack(
                rx.link(
                    rx.image(
                        src="twitter.png",
                        alt="Logo de twitter",
                        width="20px",  # Ajustar tamaño para móvil
                        height="20px",
                        margin_left="10px",
                        style={
                            "@media (min-width: 769px)": {
                                "width": "30px",  # Tamaño más pequeño para escritorio
                                "height": "30px",
                                "margin_left": "15px"  # Espacio entre iconos en escritorio
                            }
                        }  # Tamaño para escritorio
                    ),
                    href=constants.TWITTER_URL,
                    is_external=True
                ),
                rx.link(
                    rx.image(
                        src="youtube.jpg",
                        alt="Logo de youtube",
                        width="20px",
                        height="20px",
                        margin_left="10px",
                        style={
                            "@media (min-width: 769px)": {
                                "width": "30px",
                                "height": "30px",
                                "margin_left": "15px"  # Espacio entre iconos en escritorio
                            }
                        }
                    ),
                    href=constants.YOUTUBE_URL,
                    is_external=True
                ),
                rx.link(
                    rx.image(
                        src="instagram.jpg",
                        alt="Logo de instagram",
                        width="20px",
                        height="20px",
                        margin_left="10px",
                        style={
                            "@media (min-width: 769px)": {
                                "width": "30px",
                                "height": "30px",
                                "margin_left": "15px"  # Espacio entre iconos en escritorio
                            }
                        }
                    ),
                    href=constants.INSTAGRAM_URL,
                    is_external=True
                ),
                rx.link(
                    rx.image(
                        src="github.jpg",
                        alt="Logo de Github",
                        width="40px",
                        height="20px",
                        style={
                            "@media (min-width: 769px)": {
                                "width": "50px",
                                "height": "30px",
                                "margin_left": "15px"  # Espacio entre iconos en escritorio
                            }
                        }
                    ),
                    href=constants.REPO_URL,
                    is_external=True
                ),
                margin_left="30px",
                style={
                    "@media (max-width: 768px)": {
                        "margin_left": "0px",
                        "justifyContent": "center",
                        "flexWrap": "wrap",
                        "margin_bottom": "5px"  # Reducir espacio inferior en móviles
                    }
                }
            ),
            align_items="end",
            margin_left="0px",
            style={
                "flexWrap": "wrap",
                "@media (max-width: 768px)": {
                    "flexDirection": "column",
                    "alignItems": "center"
                }
            }
        ),
        style={
            "display": "flex",
            "flexDirection": "row",
            "width": "100%",
            "padding": "1rem",  # Reducir padding en escritorio
            "@media (max-width: 768px)": {
                "flexDirection": "column",
                "textAlign": "center",
                "padding": "1rem"  # Mantener padding en móviles
            }
        }
    ) 