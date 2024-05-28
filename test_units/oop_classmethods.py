import random

class Hat:
    houses = ['Toshkent', 'Andijon', 'Buxoro']

    @classmethod
    def sort(cls, name):
        print(name, 'is from', random.choice(cls.houses))

Hat.sort('Harry')