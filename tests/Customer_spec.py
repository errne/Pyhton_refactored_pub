import unittest
from models.Customer import *


class CustomerSpec(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Jim", 33, 55)

    def test_name(self):
        self.assertEqual(self.customer.name, "Jim")

    def test_age(self):
        self.assertEqual(self.customer.show_id(), 33)

    def test_wallet(self):
        self.assertEqual(self.customer.check_wallet(), 55)

    def test_drunkenness_level(self):
        self.assertEqual(self.customer.drunkenness_level(), 0)
