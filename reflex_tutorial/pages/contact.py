import reflex as rx

from ..ui.base import base_page

def contact_page() -> rx.Component:
    # Welcome Page (Index)
    my_child= rx.vstack(
        rx.heading("New phone who dis ?", size="9"),
                rx.text(
                    "Not a good time unless I smoke mine, Too many drugs that make u go blind !",
                ),
                rx.button(
                    rx.icon(tag="skull"),
                    "Flatbush Zombies!",
                    color_scheme="red",
                ),
                spacing="5",
                justify="center",
                min_height="85vh",
                align="center",
                )
    return base_page(my_child)