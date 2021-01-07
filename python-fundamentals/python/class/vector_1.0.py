from math import hypot


class Vector:
    number_of_vector_instances = 0  # class vairable

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

        # updating the instance count
        Vector.number_of_vector_instances += 1

    def __repr__(self):
        # return "Vector({}, {})".format(self.x, self.y)
        return "Vector(%r, %r)" % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scaler):
        x = self.x * scaler
        y = self.y * scaler
        return Vector(x, y)


v1 = Vector(1, 2)

print(hash(v1))
