class Food:

    def __init__(self, name, price, rejuvenation_level):
        self.name = name
        self.price = price
        self.rejuvenation_level = rejuvenation_level

    @property
    def attribute(self):
        return self._rejuvenation_level

    #
    @attribute.setter
    def attribute(self, value):
        self.rejuvenation_level = value

    #
    @attribute.deleter
    def attribute(self):
        del self._rejuvenation_level
