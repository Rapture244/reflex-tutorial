"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


#----------------------------------------------------- BACKEND ------------------------------------------------------------------------------------
class State(rx.State):
    """The app state."""

    title_heading = "Welcome to Reflex!"

    def handle_title_input_change(self, val):
        self.title_heading = val



    ...

#----------------------------------------------------- FRONTEND -----------------------------------------------------------------------------------
def navbar() -> rx.Component:
    return rx.heading("SaaS", size="9")

def base_page(child: rx.Component, hide_navbar=False, *args, **kwargs) -> rx.Component:
    if not isinstance(child, rx.Component):
        child = rx.heading("This is not a valid child element")
    if hide_navbar:
        return rx.container(
            child,
            rx.logo(),
            rx.color_mode.button(position="bottom_left"),
        )
    return rx.container(
        navbar(),
        child,
        rx.logo(),
        rx.color_mode.button(position="bottom_left"),
    )

def index() -> rx.Component:
    # Welcome Page (Index)
    return base_page(
        rx.vstack(
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
        ),
        #hide_navbar=True
    )

#----------------------------------------------------- PAGES --------------------------------------------------------------------------------------
app = rx.App()
app.add_page(index)


#----------------------------------------------------- WHAT DID I DO ? -----------------------------------------------------------------------------
""" 
"""