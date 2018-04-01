#!/usr/bin/env python
# coding: utf-8

"""factory_method


*What does this example do?
The code shows a way to localize words in two languages: English and
Greek. "getLocalizer" is the factory method that constructs a
localizer depending on the language chosen. The localizer object will
be an instance from a different class according to the language
localized. However, the main code does not have to worry about which
localizer will be instantiated, since the method "get" will be called
in the same way independently of the language.

感觉这个东西就是封装了原来class里面的东西，然后返回回去，返回一个字典，然后选择
选定的东西。


- 与 builder.py 的不同在于，builder在方法内部做了一些事情，然后返回一个实例这个返回的实例，则是没有做什么事情，直接返回，只不过有相同的借口
- abstract_factory 是有共同的方法；感觉是多了一个 get_localizer 来选择具体的子类


"""



class GreekGetter(object):
    """a simpe localizer a la gettext"""

    def __init__(self):
        self.trans = dict(dog="σκύλος", cat="γάτα")

    def get(self, msgid):
        """ We'll punt if we don't have a tranlation"""
        return self.trans.get(msgid, str(msgid))


class EnglishGetter(object):
    """simple echoes the msg ids"""

    def get(self, msgid):
        return str(msgid)


def get_localizer(language="English"):
    """ The factory method """
    languages = dict(English=EnglishGetter, Greek=GreekGetter)
    return languages[language]()


if __name__ == '__main__':
    # Create our localizers
    e, g = get_localizer(language="English"), get_localizer(language="Greek")
    # Localize some text
    for msgid in "dog parrot cat bear".split():
        print(e.get(msgid), g.get(msgid))
        

"""OUTPUT
('dog', '\xcf\x83\xce\xba\xcf\x8d\xce\xbb\xce\xbf\xcf\x82')
('parrot', 'parrot')
('cat', '\xce\xb3\xce\xac\xcf\x84\xce\xb1')
('bear', 'bear')
"""
