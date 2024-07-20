"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


#----------------------------------------------------- BACKEND ------------------------------------------------------------------------------------
class State(rx.State):
    """The app state."""

    # STEP 3: Create 3 variables with the 1st one being our title heading
    title_heading = "Welcome to Reflex!"
    heading1 = "All CAPS when u spell the man name"
    heading2 = "MF DOOM - The Supervillain"

    # STEP 4: Create an even handler that that changes the value of the var 'title_heading'
    def change_heading(self):
        if self.title_heading == "Welcome to Reflex!":
            self.title_heading = self.heading1
        elif self.title_heading == self.heading1:
            self.title_heading = self.heading2
        else:
            self.title_heading = "Welcome to Reflex!"

    ...



#----------------------------------------------------- FRONTEND -----------------------------------------------------------------------------------
def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading(State.title_heading, size="9"),  # STEP 2: turn the heading string into a variable that we move into our State
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

            # STEP 1: Create a new button
            rx.button(
                rx.icon(tag="skull"),
                "Click me to see what I can do!",
                color_scheme="red",
                on_click=State.change_heading, # STEP 5 : We add our event_trigger = Event_handler to our component
            ),

            spacing="5",
            justify="center",
            min_height="85vh",

        ),

        rx.logo(),
    )

#----------------------------------------------------- PAGES --------------------------------------------------------------------------------------
app = rx.App()
app.add_page(index)
