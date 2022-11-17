class Circle:
    def __init__(self, radius):
        self._radius = self.set_radius(radius)

    def set_radius(self, radius):
        if isinstance(radius, float):
            return radius
        else:
            print("invalid radius")
            return None


c1 = Circle(8.0)
c2 = Circle("x")

print(c1._radius)
print(c2._radius)
