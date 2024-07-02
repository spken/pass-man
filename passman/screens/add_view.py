from py_cui import PyCUI
from database.db import Database
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from main import PassMan


class AddView:
    def __init__(self, master: PyCUI, passman: 'PassMan') -> None:
        self.master = master
        self.db = Database()
        self.passman = passman

    def display(self) -> None:
        """
        Method to switch to the 'add' screen and
        set up input fields for new entry.
        """
        self.master.clear()

        self.master.set_title('passman - add')

        self.website_input = self.master.add_text_box('Website:', 0, 0)
        self.username_input = self.master.add_text_box('Username:', 1, 0)
        self.password_input = self.master.add_text_box(
            'Password:', 2, 0, password=True
        )

        self.save_button = self.master.add_button(
            'Save', 3, 0, command=self.save
        )
        self.cancel_button = self.master.add_button(
            'Cancel', 3, 1, command=self.cancel
        )

    def save(self) -> None:
        """
        Method to save the new entry to the database.
        """
        website = self.website_input.get()
        username = self.username_input.get()
        password = self.password_input.get()

        try:
            self.db.add_entry(website, username, password)
            print(f'Saved new entry for website: {website}')
        except Exception as e:
            print(f'Error saving entry to database: {e}')

        self.master.clear()
        self.passman.set_up_cui()

    def cancel(self) -> None:
        """
        Method to cancel adding a new entry and go back to the main screen.
        """
        self.master.clear()
        self.passman.set_up_cui()
