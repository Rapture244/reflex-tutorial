"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from rxconfig import config

from .ui.base import base_page # from the package 'ui' grab the module 'base' and import the function 'base_page'. Th '.' means in the same root as the current file

#----------------------------------------------------- BACKEND ------------------------------------------------------------------------------------
class State(rx.State):
    """The app state."""

    title_heading = "Welcome to Reflex!"

    def handle_title_input_change(self, val):
        self.title_heading = val



    ...

#----------------------------------------------------- FRONTEND -----------------------------------------------------------------------------------
def index() -> rx.Component:
    # Welcome Page (Index)
    my_child= rx.vstack(
        rx.heading(State.title_heading, size="9"),
                rx.text(
                    "Get started by editing ",
                    rx.code(f"{config.app_name}/{config.app_name}.py"),
                    size="5",
                ),
                rx.link(
                    rx.button("Check out our docs!"),
                    href="https://reflex.dev/docs/getting-started/introduction/",
                    is_external=True,
                ),
                rx.input(placeholder =State.title_heading,
                        default_value = State.title_heading,
                        max_value = 30,
                        on_change = State.handle_title_input_change,
                ),
                rx.button(
                    rx.icon(tag="skull"),
                    "I'm just a cool Button but i do nothing!",
                    color_scheme="red",
                ),
                spacing="5",
                justify="center",
                min_height="85vh",
                text_align="center",
                align="center",
                )
    return base_page(my_child)

#----------------------------------------------------- PAGES --------------------------------------------------------------------------------------
app = rx.App()
app.add_page(index)


