class Point:
    color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"pont({self.x},{self.y})")


Point.color = "yellow"
p = Point(1, 2)
p.z = 3
p.color = "green"
p.draw()
print(p, "\n", p.color)
q = Point.zero()
q.draw()
print(q.color)
