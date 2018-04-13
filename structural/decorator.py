#!/usr/bin/env python
# coding: utf-8

from __future__ import print_function

"""
动态的添加一个新的特性，但不改变其表示；

它于继承不同，是因为新的特征只被加入到特定的对象，而不是整个子类

"""

class TextTag(object):
    """Represents a base text tag"""

    def __init__(self, text):
        self._text =text

    def render(self):
        return self._text


class BoldWrapper(TextTag):
    """Wraps a tag in <b>"""
    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return "<b>{}<b>".format(self._wrapped.render())


class ItalicWrapper(TextTag):
    """Wraps a tag in <i>"""
    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return "<i>{}</i>".format(self._wrapped.render())


if __name__ == '__main__':
    simple_hello = TextTag("hello, world!")
    special_hello = ItalicWrapper(BoldWrapper(simple_hello))
    print("before:", simple_hello.render())
    print("after:", special_hello.render())


"""
OUTPUT:

before: hello, world!
after: <i><b>hello, world!<b></i>

"""