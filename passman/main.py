import py_cui
from database.db import Database


class PassMan:
    def __init__(self, master):
        self.db = Database()
        self.data = {}
        self.set_data()
        self.set_up_cui(master)

    def set_data(self):
        entries = self.db.get_all_entries()
        for entry in entries:
            self.data[entry.website] = {
                'username': entry.username,
                'password': entry.password
            }

    def set_up_cui(self, master):
        self.master = master
        self.master.set_title('passman')

        self.website_column()
        self.details_column()

        self.website_list.add_key_command(
            py_cui.keys.KEY_ENTER,
            self.display_details
        )

    def website_column(self):
        self.website_list = self.master.add_scroll_menu(
            'Websites', 0, 0, row_span=10
        )
        self.website_list.add_item_list(self.data.keys())

    def details_column(self):
        self.details = self.master.add_text_block(
            'Details', 0, 1, row_span=10, column_span=3
        )
        self.details.set_text('Select a website to view details')

    def display_details(self):
        selected_website = self.website_list.get()
        if selected_website in self.data:
            details = self.data[selected_website]
            details_text = (f"Website: {selected_website}\n"
                            f"Username: {details['username']}\n"
                            f"Password: {details['password']}")
        else:
            details_text = 'No details available'

        self.details.set_text(details_text)


if __name__ == '__main__':
    root = py_cui.PyCUI(10, 4)
    pm = PassMan(root)
    root.start()
