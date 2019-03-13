class Customer:

    def __init__(self, name, age, wallet):
        self.name = name
        self.age = age
        self.wallet = wallet
        self.drunkenness = 0

    def name(self):
        return self._name

    def show_id(self):
        return self.age

    def check_wallet(self):
        return self.wallet

    def drink_drink(self, beverage):
        self.drunkenness += beverage.alcohol_level

    def drunkenness_level(self):
        return self.drunkenness


