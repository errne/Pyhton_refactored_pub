class Pub:

    def __init__(self, name, drinks):
        self.name = name
        self.drinks = drinks
        self.till = 10

    def check_till(self):
        return self.till

    def add_money_to_till(self, cash):
        self.till += cash

    def check_stock(self, item):
        return self.drinks[item]

    def check_age(self, customer):
        return customer.show_id() >= 18

    def is_customer_sober_enough(self, customer):
        return customer.drunkenness_level() < 20

    def reduce_stock(self, item):
        self.drinks[item] -= 1

    def sell_item(self, customer, item):
        if type(item).__name__ == "Drink":
            if not self.check_age(customer):
                return "You are too young!"
            if not self.is_customer_sober_enough(customer):
                return "You are too drunk!"
            if self.check_stock(item) <= 0:
                return "we don't have that anymore!"
            self.reduce_stock(item)
        cash = customer.buy_item(item)
        self.add_money_to_till(cash)

    def evaluate_stock(self):
        total_value = 0
        for key, value in self.drinks.items():
            total_value += key.price*value
        return total_value
