import math

class Vector:

    def __init__(self, x: float, y: float):
        self._x = x; self._y = y
        self._color = None

    def normalize(self):
        l = self.length()
        return Vector(self._x / l, self._y / l)

    def length(self):
        return math.sqrt(self._x ** 2 + self._y ** 2)

    def to_tuple(self):
        return (self._x, self._y)

    def get_point(p1, p2, n1, n2):
        m1 = n1._y / (n1._x) if n1._x != 0 else 1
        m2 = n2._y / (n2._x) if n2._x != 0 else 1

        b1 = p1._y - m1 * p1._x
        b2 = p2._y - m2 * p2._x

        px = (b2 - b1) / (m1 - m2)
        py = m1 * px + b1

        return Vector(px, py)

    def __mul__(self, other):
        return Vector(self._x * other._x, self._y * other._y)

    def __truediv__(self, other):
        return Vector(self._x / other._x, self._y / other._y)

    def __add__(self, other):
        return Vector(self._x + other._x, self._y + other._y)

    def __sub__(self, other):
        return Vector(self._x - other._x, self._y - other._y)

    def __str__(self):
        return f"<{self._x}, {self._y}>"

    def line_intersection(line1, line2):
        xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
        ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

        def det(a, b):
            return a[0] * b[1] - a[1] * b[0]

        div = det(xdiff, ydiff)
        if div == 0:
            raise Exception('lines do not intersect')

        d = (det(*line1), det(*line2))
        x = det(d, xdiff) / div
        y = det(d, ydiff) / div
        return x, y


if __name__ == "__main__":
    a1 = Vector(0, 1)
    a2 = Vector(1, 0)

    b1 = Vector(1, 0)
    b2 = Vector(0, 1)

    print(Vector.get_point(a1, b1, a2.normalize(), b2.normalize()))


