import reflex as rx
import asyncio


from ..ui.base import base_page
from .. import navigation


#------------------------------ FOR DATABASE ---------------------------------------------------------------------
class ContactEntryModel(rx.Model, table= True):
    first_name: str
    last_name: str | None = None
    email: str | None = None
    message: str


#------------------------------ FOR CONTACT INFO ---------------------------------------------------------------------
class ContactState(rx.State):

    form_data: dict[str,str] = {}
    did_submit: bool = False

    @rx.var
    def thank_you(self):
        first_name = self.form_data.get("first_name") or ""
        return f"Thank you {first_name}".strip() + " for leaving your message !"

    async def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data
        data = {}
        for k,v in form_data.items():
            if v == "" or v is None:
                continue
            data[k] = v
        # print(data)     -> This was to check the value that were entered and if it worked during the testing
        with rx.session() as session:
            db_entry = ContactEntryModel(
                **data
            )
            session.add(db_entry)
            session.commit()
            self.did_submit = True
            yield
            # sleep -> timeout -> setTimeout
            await asyncio.sleep(5)
            self.did_submit = False
            yield




@rx.page(
    route=navigation.routes.CONTACT_ROUTE
)
#------------------------------ CONTACT UI  ---------------------------------------------------------------------
def contact_page() -> rx.Component:
    my_form = rx.form(
        rx.vstack(
            rx.hstack(
                rx.input(
                name = "first_name",
                placeholder = "First Name",
                required = True,
                type = "text",
                width = "100%",
                ),
            rx.input(
                name = "last_name",
                placeholder = "Last Name",
                required = False,
                type = "text",
                width = "100%",
                ),
            width = "100%",
            ),
            rx.input(
                name = "email",
                placeholder = "Your email",
                required = False,
                #type = "email",
                width = "100%",
            ),
            rx.text_area(
                name = "message",
                placeholder = "Your message!",
                required = True,
                type = "text",
                width = "100%",
            ),
            rx.button("Submit", type = "submit"),
        ),
        on_submit = ContactState.handle_submit,
        reset_on_submit = True,
    )

    my_child = rx.vstack(
        rx.heading("New phone who dis ?", size = "9"),
        rx.cond(ContactState.did_submit, rx.button(rx.icon(tag="star"), ContactState.thank_you, color_scheme = "green")),
        rx.desktop_only(
            rx.box(my_form,
                   width="40vw"),
        ),
        rx.mobile_and_tablet(my_form,
                             width="75vw"),
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