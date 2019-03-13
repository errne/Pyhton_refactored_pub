import unittest
from models.Customer import *
from models.Drink import *
from models.Food import *


class CustomerSpec(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Jim", 33, 55)
        self.drink = Drink("Helles", 6, 5)
        self.food = Food("Saussage", 3, 3)

    def test_name(self):
        self.assertEqual(self.customer.name, "Jim")

    def test_age(self):
        self.assertEqual(self.customer.show_id(), 33)

    def test_wallet(self):
        self.assertEqual(self.customer.check_wallet(), 55)

    def test_drunkenness_level(self):
        self.assertEqual(self.customer.drunkenness_level(), 0)

    def test_drunkenness_level__after_drink(self):
        self.customer.drink_drink(self.drink)
        self.assertEqual(self.customer.drunkenness_level(), 5)

    def test_drunkenness_level__after_food(self):
        self.customer.drink_drink(self.drink)
        self.customer.eat_food(self.food)
        self.assertEqual(self.customer.drunkenness_level(), 2)
