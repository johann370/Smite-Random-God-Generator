class God:
    def __init__(self, name, link, pantheon, god_class, release_date):
        self.name = name
        self.link = link
        self.pantheon = pantheon
        self.god_class = god_class
        self.release_date = release_date

    def get_name(self):
        return self.name

    def get_link(self):
        return self.link

    def get_pantheon(self):
        return self.pantheon

    def get_class(self):
        return self.god_class

    def get_release_date(self):
        return self.release_date
