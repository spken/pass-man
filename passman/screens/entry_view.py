import py_cui


class EntryView:
    """
    Home-screen view for all entries.
    """
    def __init__(self, data, master):
        """
        :param data: The entry data.
        :param master: The root PyCUI object.
        """
        self.data = data
        self.master = master
        self.website_list = None

    def display(self):
        self.website_column()
        self.details_column()
        self.website_list.add_key_command(
            py_cui.keys.KEY_ENTER,
            self.display_details
        )

    def website_column(self):
        """
        Set up the website list column in the CUI.
        """
        self.website_list = self.master.add_scroll_menu(
            'Websites', 0, 0, row_span=10
        )
        self.website_list.add_item_list(self.data.keys())

    def details_column(self):
        """
        Set up the details column in the CUI.
        """
        self.details = self.master.add_text_block(
            'Details', 0, 1, row_span=10, column_span=3
        )
        self.details.set_text('Select a website to view details')

    def display_details(self):
        """
        Display the details of the selected website.
        """
        selected_website = self.website_list.get()
        if selected_website in self.data:
            details = self.data[selected_website]
            details_text = (f"Website: {selected_website}\n"
                            f"Username: {details['username']}\n"
                            f"Password: {details['password']}")
        else:
            details_text = 'No details available'

        self.details.set_text(details_text)
