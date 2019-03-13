import unittest
from models.Customer import *

class CustomerSpec(unittest.TestCase):

    def test_name(self):
        cust1 = Customer("Jim", 33, 55)
        self.assertEqual(cust1.drunkenness_level(), 0)