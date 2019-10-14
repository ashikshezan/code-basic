from datetime import datetime


class Person:
    name = 'shezan'

    def __init__(self):
        self.name = self.name


def debug_info(self):
    results = []
    results.append(f'time: {datetime.now()}')
    results.append(f'Class: {self.__class__.__name__}')
    results.append(f'Id: {hex(id(self))}')

    for k, v in vars(self).items():
        results.append(f'{k}: {v}')
    return results


def debug(cls):
    cls.debug = debug_info
    return cls


p = Person()
debug(Person)
print(p.debug())
