#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
一句话来概括，就是做到能少改代码

这个模式就是把其中一个变量的接口抽象了两层，一层是类，另一层是API。
设计其实可以很复杂，把类的层次写的很深，就可以让调用的灵活性很大。
同时把握灵活性和规范非常重要。

"""


# ConcreteImplementor 1/2
class DrawingAPI1(object):

    def draw_circle(self, x, y, radius):
        print('API1.circle at {}:{} radius {}'.format(x, y, radius))

# ConcreteImplementor 2/2
class DrawingAPI2(object):

    def draw_circle(self, x, y, radius):
        print('API2.circle at {}:{} radius {}'.format(x, y, radius))


# Refind Abstraction
class CircleShape(object):

    def __init__(self, x, y, radius, drawing_api):
        self._x = x
        self._y = y
        self._radius = radius
        self._drawing_api = drawing_api


    # low-level i.e. Implementation specific
    def draw(self):
        self._drawing_api.draw_circle(self._x, self._y, self._radius)

    # high_level i.e. Abstraction specific
    def scale(self, pct):
        self._radius *= pct


def main():
    shapes = (
        CircleShape(1, 2, 3, DrawingAPI1()),
        CircleShape(1, 2, 3, DrawingAPI2())
        )

    for shape in shapes:
        shape.scale(2.5)
        shape.draw()


if __name__ == '__main__':
    main()


"""
OUPTUT:

API1.circle at 1:2 radius 7.5
API2.circle at 5:7 radius 27.5
"""
