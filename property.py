class Circle:
    VALID_COLORS = ("red", "green", "blue")

    def __init__(self, radius):
        self._radius = self.set_radius(radius)

    def get_radius(self):
        return self._radius

    def set_radius(self, radius):
        if isinstance(radius, float):
            return radius
        else:
            print("invalid radius")
            return None

    radius = property(get_radius, set_radius)


c1 = Circle(8.0)
c2 = Circle("x")

print(c1.radius)
print(c2.radius)
