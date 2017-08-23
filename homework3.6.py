# -*- coding: utf-8 -*-
class Animal:
    legs = None
    food = 0
    kind = None

    def __init__(self, food, kind):
        self.food = food
        self.kind = kind

    def feed(self, value):
        self.food += value

    def wake_up(self):
        print('I\'m not sleep!')

    def speak(self):
        animal_dict = {'cow': 'muu', 'goat': 'bee', 'sheep': 'bee',
                       'duck': 'krya', 'goose': 'ga', 'chicken': 'ko'}
        print(animal_dict[self.kind])


class Mammal(Animal):
    legs = 4


class Birds(Animal):
    legs = 2

burenka = Mammal(0, 'cow')
burenka.speak()
print(burenka.legs)
