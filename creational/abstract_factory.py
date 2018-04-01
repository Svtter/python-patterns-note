#!/usr/bin/env python
# coding: utf-8


"""

感觉这个模式就是在原来类的基础上再做一层封装，然后就可以替换里面的东西，
这就是所谓的抽象工厂模式

"""

import random

class PetShop(object):

    """a pet shop / just like a factory"""

    def __init__(self, animal_factory=None):
        """ pet_factory is our abstract factory. we can set it at will"""
        self.pet_factory = animal_factory

    def show_pet(self):
        """Creates and shows a pet using abstract factory"""

        pet = self.pet_factory()
        print("We have a lovely {}".format(pet))
        print("It says {}".format(pet.speak()))


class Dog(object):

    def speak(self):
        return "woof"

    def __str__(self):
        return "Dog"


class Cat(object):

    def speak(self):
        return "meow"

    def __str__(self):
        return "Cat"

def random_animal():
    """Let's be dynamic!"""
    return random.choice([Dog, Cat])()


if __name__ == '__main__':

    # A shop that sells only cats
    cat_shop = PetShop(Cat)
    cat_shop.show_pet()
    print("")

    # A shop that sells random animals
    shop = PetShop(random_animal)
    for i in range(3):
        shop.show_pet()
        print("=" * 20)


"""
## OUTPUT ##
We have a lovely Cat
It says meow

We have a lovely Cat
It says meow
====================
We have a lovely Cat
It says meow
====================
We have a lovely Dog
It says woof
====================
"""
