class Circle:
    def __init__(self, radius):
        # use self.radius, not self._radius
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        if isinstance(radius, int) and radius > 0:
            self._radius = radius
        else:
            print("invalid radius")


c1 = Circle(10)
c2 = Circle("hh")
