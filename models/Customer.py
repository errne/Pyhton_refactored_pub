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

    def eat_food(self, food):
        self.drunkenness -= food.rejuvenation_level
        if self.drunkenness < 0:
            self.drunkenness = 0

    def drunkenness_level(self):
        return self.drunkenness

    def buy_item(self, item):
        self.wallet -= item.price
        if type(item).__name__ == "Drink":
            self.drink_drink(item)
        if type(item).__name__ == "Food":
            self.eat_food(item)
        return item.price


