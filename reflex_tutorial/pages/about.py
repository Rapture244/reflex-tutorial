import reflex as rx

from ..ui.base import base_page



def about_page() -> rx.Component:
    # Welcome Page (Index)
    my_child= rx.vstack(
        rx.heading("MF DOOM - The supervillain!", size="9"),
                rx.text(
                    "All CAPS when u spell the man name",
                ),
                rx.button(
                    rx.icon(tag="bird"),
                    "I'm just a cool Button but i do nothing!",
                    color_scheme="violet",
                ),
                spacing="5",
                justify="center",
                min_height="85vh",
                align="center",
                )
    return base_page(my_child)