import py_cui
from database.db import Database
from screens.entry_view import EntryView


class PassMan:
    """
    A CUI-based password manager.
    """

    def __init__(self, master):
        """
        :param master: The root PyCUI object.
        """
        self.master = master
        self.db = Database()
        self.data = {}
        self.set_data()
        self.set_up_cui()

    def set_data(self):
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

    def set_up_cui(self):
        """
        Set up the CUI layout and bind key commands.

        :param master: The root PyCUI object.
        """
        self.master.set_title('passman')

        entry_view = EntryView(data=self.data, master=self.master)
        entry_view.display()


if __name__ == '__main__':
    root = py_cui.PyCUI(10, 4)
    pm = PassMan(root)
    root.start()
