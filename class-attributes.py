class Robot:
    # class attributes
    robot_count = 0

    def __init__(self, name):
        Robot.robot_count += 1
        self._id = Robot.robot_count
        self.name = name


r1 = Robot("R2D2")
r2 = Robot("R2D3")

# non-public members are not meant to be accessed directly
print(r1._id)
print(r2._id)

print(Robot.robot_count)
