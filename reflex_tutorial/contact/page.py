import reflex as rx

# Packages & modules created by me
from .. import navigation
from ..ui.base import base_page

from . import form, state


# ------------------------------ CONTACT UI  ---------------------------------------------------------------------
def contact_page() -> rx.Component:
    my_child = rx.vstack(
        rx.heading("New phone who dis ?", size = "9"),
        rx.cond(state.ContactState.did_submit,rx.button(rx.icon(tag = "star"), state.ContactState.thank_you, color_scheme = "green")
                ),
        rx.desktop_only(
            rx.box(form.contact_form(),
                   width = "40vw"
                   ),
            ),
        rx.mobile_and_tablet(form.contact_form(),
                             width = "75vw"
                             ),
        rx.button(
            rx.icon(tag = "skull"),
            "Flatbush Zombies!",
            color_scheme = "red",
            ),
        spacing = "5",
        justify = "center",
        min_height = "85vh",
        align = "center",
        )
    return base_page(my_child)
