import py_cui


class PasswordManager:
    def __init__(self, master):
        self.master = master
        self.master.set_title("Password Manager")

        # Website list
        self.website_list = self.master.add_scroll_menu(
            "Websites", 0, 0, row_span=10
        )
        self.website_list.add_item_list(["Website1", "Website2", "Website3"])

        # Password details
        self.details = self.master.add_text_block(
            "Details", 0, 1, row_span=10, column_span=3
        )
        self.details.set_text("Select a website to view details")

        # Website onselect
        self.website_list.add_key_command(
            py_cui.keys.KEY_ENTER,
            self.display_details
        )

    def display_details(self):
        selected_website = self.website_list.get()
        if selected_website == "Website1":
            details_text = "Website: Website1\n \
                Username: user1\nPassword: pass1"
        elif selected_website == "Website2":
            details_text = "Website: Website2\n \
                Username: user2\nPassword: pass2"
        elif selected_website == "Website3":
            details_text = "Website: Website3\n \
                Username: user3\nPassword: pass3"
        else:
            details_text = "No details available"

        self.details.set_text(details_text)


root = py_cui.PyCUI(10, 4)
pm = PasswordManager(root)
root.start()
