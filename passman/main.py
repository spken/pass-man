from py_cui import PyCUI
from database.db import Database
from screens.entry_view import EntryView
from screens.add_view import AddView
from typing import Dict


class PassMan:
    """
    A CUI-based password manager.
    """

    def __init__(self, master: PyCUI) -> None:
        """
        :param master: The root PyCUI object.
        """
        self.master = master
        self.db = Database()
        self.data: Dict[str, Dict[str, str]] = {}
        self.set_data()
        self.set_up_cui()

    def set_data(self) -> None:
        """
        Retrieve all entries from the database and store them in self.data.
        """
        try:
            entries = self.db.get_all_entries()
            for entry in entries:
                self.data[entry.website] = {
                    'username': entry.username,
                    'password': entry.password
                }
        except Exception as e:
            print(f"Error retrieving data from the database: {e}")

    def set_up_cui(self) -> None:
        """
        Set up the CUI layout and bind key commands.
        """
        self.master.set_title('passman - home')

        entry_view = EntryView(data=self.data, master=self.master)
        entry_view.display()

        av = AddView(master=self.master, passman=self)
        self.master.add_key_command('a', av.display)  # TODO: doesn't work, fix


if __name__ == '__main__':
    root = PyCUI(10, 4)
    pm = PassMan(root)
    root.start()
