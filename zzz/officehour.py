class Restaruant:
    def __init__(self, name, address, menu, employees):
        self.name = name
        self.address = address
        self.menu = menu
        self.employees = employees
        self.is_open = False
        self.is_close = True

    def open_close(self): #
        if not self.is_open:
            self.is_open = True
        else:
            self.is_open = False

    def add_drinks_to_menu(self, drink):
        self.menu.append(drink)
Jessys_Restaurant = Restaruant("Jessy's Restuarant", "1234 Dojo Lane Coding, Ca, 09876", )