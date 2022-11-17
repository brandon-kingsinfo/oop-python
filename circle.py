class Circle:
    def __init__(self, radius, color="red"):
        self.radius = radius
        self.color = color

    def calc_area(self) -> float:
        """
        calculates the area of a acircle

        Returns:
            float: area of a circle
        """
        return self.radius * 2 * 3.14


c1 = Circle(5)
c2 = Circle(10, "yellow")

print(c1.calc_area())
print(c2.calc_area())
print(c1.color)
print(c2.color)
