"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from rxconfig import config

from .ui.base import base_page # from the package 'ui' grab the module 'base' and import the function 'base_page'. Th '.' means in the same root as the current file

from . import  blog, contact, navigation, pages

#----------------------------------------------------- BACKEND ------------------------------------------------------------------------------------
class State(rx.State):
    """The app state."""

    title_heading = "Welcome to Reflex!"



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
                    rx.button(
                        rx.icon(tag="skull"),
                        "Click on me and see what happens!",
                        color_scheme="red",
                    ),
                    href=navigation.routes.ABOUT_ROUTE
                ),
                spacing="5",
                justify="center",
                min_height="85vh",
                align="center",
                )
    return base_page(my_child)






#----------------------------------------------------- PAGES --------------------------------------------------------------------------------------
app = rx.App()
app.add_page(index, route=navigation.routes.HOME_ROUTE)
app.add_page(pages.about_page, route=navigation.routes.ABOUT_ROUTE)
app.add_page(pages.pricing_page, route=navigation.routes.PRICING_ROUTE)
app.add_page(contact.contact_page, route=navigation.routes.CONTACT_ROUTE)
app.add_page(contact.contact_entries_list_page,
             route=navigation.routes.CONTACT_ENTRIES_ROUTE,
             on_load=contact.ContactState.list_entries
             )
