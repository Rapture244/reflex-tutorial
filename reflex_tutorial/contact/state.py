# Libraries
from typing import List
import reflex as rx
import asyncio

from sqlmodel import select
from .model import ContactEntryModel


#------------------------------ FOR CONTACT INFO ---------------------------------------------------------------------
class ContactState(rx.State):
    form_data: dict[str,str] = {}
    entries: List['ContactEntryModel'] = []
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
        await asyncio.sleep(5)
        self.did_submit = False
        yield

    def list_entries(self):
        with rx.session() as session:
            entries = session.exec(
                select(ContactEntryModel)
                ).all()
            self.entries = entries


