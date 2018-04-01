#!/usr/bin/env python
# coding: utf-8


"""

builder

每个类有同样的方法，只是给出了不同的具体的类

每个类都实现了抽象类

"""

def construct_building(builder):
    builder.new_building()
    builder.build_floor()
    builder.build_size()
    return builder.building


# Abstract Builder
class Builder(object):

    def __init__(self):
        self.building = None

    def new_building(self):
        self.building = Building()

    def build_floor(self):
        raise NotImplementedError

    def build_size(self):
        raise NotImplementedError

# Concrete Builder
class BuilderHouse(Builder):

    def build_floor(self):
        self.building.floor = 'One'

    def build_size(self):
        self.building.size = 'Big'


class BuilderFlat(Builder):
    """docstring for BuilderFlat"""

    def build_floor(self):
        self.building.floor = 'More than One'

    def build_size(self):
        self.building.size = 'Small'


# Product
class Building(object):
    """docstring for Building"""
    def __init__(self):
        self.floor = None
        self.size = None

    def __repr__(self):
        return 'Floor: {0.floor} | Size: {0.size}'.format(self)

# Client 
if __name__ == '__main__':
    building = construct_building(BuilderHouse())
    print(building)
    building = construct_building(BuilderFlat())
    print(building)


"""
OUTPUT
Floor: One | Size: Big
Floor: More than One | Size: Small
"""
