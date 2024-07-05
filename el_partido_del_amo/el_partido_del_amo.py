import reflex as rx
from el_partido_del_amo.views.navbar import navbar
from el_partido_del_amo.views.header import header
from el_partido_del_amo.views.date import date
from el_partido_del_amo.views.entrance import entrance
from el_partido_del_amo.views.teams import teams
from el_partido_del_amo.views.footer import footer
import el_partido_del_amo.styles.styles as styles

def index() -> rx.Component:
    return rx.box(
        rx.script("document.documentElement.lang='es'"),
        rx.vstack(
            navbar(),
            header(),
            date(),
            entrance(),
            teams(),
            footer()
        ),
        style={
            "width": "100%",
            "maxWidth": "100vw",  # Asegura que no exceda el ancho de la ventana
            "overflowX": "hidden"  # Esconde cualquier desbordamiento horizontal
        }
    )

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style={**styles.BASE_STYLE, **styles.GLOBAL_STYLES}
)

app.add_page(
    index,
    title="El Partido del Año",
    description=
        "El Partido del Año. Toda la información que necesitas sobre uno de los mayores eventos del año."
    )

app._compile()