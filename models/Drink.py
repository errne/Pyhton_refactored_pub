class Drink:

    def __init__(self, name, price, alcohol_level):
        self.name = name
        self.price = price
        self.alcohol_level = alcohol_level

    @property
    def attribute(self):  # implements the get - this name is *the* name
        return self._alcohol_level

    #
    @attribute.setter
    def attribute(self, value):  # name must be the same
        self.alcohol_level = value

    #
    @attribute.deleter
    def attribute(self):  # again, name must be the same
        del self._alcohol_level
