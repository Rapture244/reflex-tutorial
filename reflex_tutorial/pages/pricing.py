import reflex as rx

from ..ui.base import base_page



def pricing_page() -> rx.Component:
    # Welcome Page (Index)
    my_child= rx.vstack(
        rx.heading("Hand me all ur money!", size="9"),
                rx.text(
                    "Don't need no green thought I got some to spend in the end all i really need is a friend",
                ),
                rx.button(
                    rx.icon(tag="skull"),
                    "I'm just a cool Button but i do nothing!",
                    color_scheme="red",
                ),
                spacing="5",
                justify="center",
                min_height="85vh",
                align="center",
                )
    return base_page(my_child)