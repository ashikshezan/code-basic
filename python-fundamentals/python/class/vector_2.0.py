# File name: vector_2.0.py
# Author: ashikshezan
# Date created: 7th January 2021
# Python Version: 3.9

from typing import Generator, Iterable


class Vector:
    instance_count = 0  # class vairable

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

        Vector.instance_count += 1  # updating the instance count

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"

    def __str__(self) -> str:
        return str(tuple(self))

    def __hash__(self) -> int:
        '''
        Making the object hashable so that, "is" operator can be used
        '''
        return hash(self.x) ^ hash(self.y)

    def __iter__(self) -> Generator:
        '''
        To do something like this: 
            v = Vectior(1,2)
            tuple(v)
        '''
        return (i for i in (self.x, self.y))

    def __eq__(self, o: "Vector") -> bool:
        "To check equality of 2 Vector instace by comparing ther value pair"
        return tuple(self) == tuple(o)

    def __abs__(self):
        import math
        "Returns a float value -> sqrt(x*x + y*y)"
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other: "Vector") -> "Vector":
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scaler: float) -> "Vector":
        x = self.x * scaler
        y = self.y * scaler
        return Vector(x, y)


v1 = Vector(3, 4)
v2 = Vector(3, 4)
print(v1*1)
