# File name: vector_2.0.py
# Author: ashikshezan
# Date created: 9th January 2021
# Python Version: 3.9

from __future__ import annotations
from typing import Iterable, Iterator
from array import array
from reprlib import repr
import math


class Vector:
    typcode = 'd'

    '''
    A multi-dimentional Vectior Class

    atrributes are read only. can only be intitialized. 
    '''
    instance_count = 0  # class vairable

    def __init__(self, values: Iterable):
        '''
        creating an actual arrray like C language. 
        Typecode is like the size of each memory cell.
        Here typecode is d which means double and the memory size is 8byte
        '''
        self.__values = array(self.typcode, values)
        Vector.instance_count += 1  # updating the instance count

    def __repr__(self) -> str:
        repr_value = repr(self.__values)  # 1
        repr_value = repr_value[repr_value.find('['): -1]
        return f'Vector{repr_value}'
        # 1. The repr library function gives a fancy way to represent a long object
        # a = Vector(range(100))
        # to get this type or representation -> array('d', [0.0, 1.0, 2.0, 3.0, 4.0, ...])

    def __str__(self) -> str:
        return str(tuple(self))

    def __hash__(self) -> int:
        '''
        Making the object hashable so that, "is" operator can be used
        '''
        pass

    def __iter__(self) -> Iterator:
        '''
        To do something like this: 
            v = Vectior([1,2])
            tuple(v)
        '''
        return iter(self.__values)

    def __getitem__(self, index):
        return self.__values[index]

    def __len__(self):
        return len(self.__values)

    def __eq__(self, o: Vector) -> bool:
        "To check equality of 2 Vector instace by comparing ther value pair"
        return tuple(self) == tuple(o)

    def __abs__(self):
        "Returns a float value -> sqrt(x*x + y*y + z*z + ...)"
        return math.sqrt(sum(n * n for n in self.__values))

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other: Vector) -> Vector:
        pass

    def __mul__(self, scaler: float) -> Vector:
        pass


a = Vector(range(100))

print(len(a))
