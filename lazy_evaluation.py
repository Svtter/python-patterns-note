#!/usr/bin/env python
# coding: utf-8


"""
惰性求值特性

里面还包含了一些 Python 的方法，参考价值比较高

"""

from __future__ import print_function
import functools

class lazy_property(object):

    def __init__(self, function):
        self.function = function
        functools.update_wrapper(self, function)

    def __get__(self, obj, type_):
        if obj is None:
            return self
        
        val = self.function(obj)
        obj.__dict__[self.function.__name__] = val
        return val


def lazy_property2(fn):
    """延迟装饰器
    
    Arguments:
        fn {function} -- 类方法传递
    
    Returns:
        function -- 类方法
    """

    attr = '_lazy__' + fn.__name__


    @property
    def _lazy__property(self):
        if not hasattr(self, attr):
            setattr(self, attr, fn(self))
        return getattr(self, attr)
    
    return _lazy__property


class Person(object):

    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation
        self.call_count2 = 0

    @lazy_property
    def relatives(self):
        # Get all relatives, let's assume that it costs much time
        relatives = "Many relatives."
        return relatives

    @lazy_property2
    def parents(self):
        self.call_count2 += 1
        return "Father and mother"


def main():
    Jhon = Person('Jhon', 'Coder')
    print(u"Name: {0}    Occupation: {1}".format(Jhon.name, Jhon.occupation))
    print(u"Before we access `relatives`:")
    print(Jhon.__dict__)
    print(u"Jhon's relatives: {0}".format(Jhon.relatives))
    print(u"After we've accessed `relatives`:")
    print(Jhon.__dict__)
    print(Jhon.parents)
    print(Jhon.__dict__)
    print(Jhon.parents)
    print(Jhon.call_count2)

if __name__ == '__main__':
    main()

    