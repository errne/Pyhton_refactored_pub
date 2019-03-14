import unittest
from models.Customer import *
from models.Drink import *
from models.Food import *
from models.Pub import *


class PubSpec(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Jim", 33, 55)
        self.underage = Customer("Minnie", 17, 10)
        self.drink1 = Drink("Helles", 6, 5)
        self.drink2 = Drink("Pilsner", 5, 4)
        self.drink3 = Drink("Trappist", 6, 7)
        self.food = Food("Sausage", 3, 3)

        self.stock = {self.drink1: 5, self.drink2: 3, self.drink3: 6}
        self.pub = Pub("Refactorr", self.stock)

    def test_name(self):
        self.assertEqual(self.pub.name, "Refactorr")

    def test_pub_has_menu(self):
        self.assertEqual({self.drink1: 5, self.drink2: 3, self.drink3: 6}, self.pub.drinks)

    def test_check_item_stock_level(self):
        self.assertEqual(3, self.pub.check_stock(self.drink2))
        self.assertEqual(6, self.pub.check_stock(self.drink3))

    def test_reduce_item_stock_level(self):
        self.pub.reduce_stock(self.drink2)
        self.assertEqual(2, self.pub.check_stock(self.drink2))

    def test_can_check_till(self):
        self.assertEqual(10, self.pub.check_till())

    def test_can_add_money_for_till(self):
        self.pub.add_money_to_till(self.drink1.price)
        self.assertEqual(16, self.pub.check_till())

    def test_pub_can_check_age(self):
        self.assertEqual(True, self.pub.check_age(self.customer))

    def test_pub_can_check_age__underage_customer(self):
        self.assertEqual(False, self.pub.check_age(self.underage))

    def test_pub_can_check_drunkenness_level(self):
        self.assertEqual(True, self.pub.is_customer_sober_enough(self.customer))

    def test_pub_can_check_drunkenness_level__too_drunk(self):
        self.customer.drink_drink(self.drink3)
        self.customer.drink_drink(self.drink3)
        self.customer.drink_drink(self.drink3)
        self.assertEqual(False, self.pub.is_customer_sober_enough(self.customer))
        self.assertEqual("You are too drunk!", self.pub.sell_item(self.customer, self.drink3))

    def test_pub_can_sell_item(self):
        self.pub.sell_item(self.customer, self.drink1)
        self.assertEqual(16, self.pub.check_till())
        self.assertEqual(49, self.customer.check_wallet())
        self.assertEqual(4, self.pub.check_stock(self.drink1))

    def test_pub_can_sell_item__food(self):
        self.pub.sell_item(self.customer, self.food)
        self.assertEqual(13, self.pub.check_till())
        self.assertEqual(52, self.customer.check_wallet())

    def test_pub_can_sell_item__not_too_drunk(self):
        self.pub.sell_item(self.customer, self.drink3)
        self.pub.sell_item(self.customer, self.drink3)
        self.pub.sell_item(self.customer, self.drink2)
        self.pub.sell_item(self.customer, self.drink2)
        self.assertEqual(32, self.pub.check_till())
        self.assertEqual(33, self.customer.check_wallet())
        self.assertEqual(1, self.pub.check_stock(self.drink2))

    def test_pub_can_sell_item__too_drunk_buys_pizza(self):
        self.pub.sell_item(self.customer, self.drink3)
        self.pub.sell_item(self.customer, self.drink3)
        self.pub.sell_item(self.customer, self.drink3)
        self.pub.sell_item(self.customer, self.food)
        self.assertEqual(31, self.pub.check_till())
        self.assertEqual(34, self.customer.check_wallet())

    def test_pub_cannot_sell_item__underage(self):
        self.pub.sell_item(self.underage, self.drink2)
        self.assertEqual(10, self.pub.check_till())
        self.assertEqual(10, self.underage.check_wallet())
        self.assertEqual("You are too young!", self.pub.sell_item(self.underage, self.drink3))

    def test_pub_cannot_sell_item__when_not_in_stock(self):
        self.pub.sell_item(self.customer, self.drink2)
        self.pub.sell_item(self.customer, self.drink2)
        self.pub.sell_item(self.customer, self.drink2)
        self.pub.sell_item(self.customer, self.drink2)
        self.assertEqual(25, self.pub.check_till())
        self.assertEqual(40, self.customer.check_wallet())
        self.assertEqual(0, self.pub.check_stock(self.drink2))

    def test_pub_stock_value(self):
        self.assertEqual(81, self.pub.evaluate_stock())




