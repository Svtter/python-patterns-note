#!/usr/bin/env python
# coding: utf-8

"""
:UNFINISH:

TODO: understand __get__ method.

PS: 这个GET方法我没有看懂啊，这么炫技。。。

__get__方法的调用过程


*TL;DR80
Separates presentation, application processing, and data management functions.
"""

class Data(object):
    """ Data Store Class """

    test = ['test']

    products = {
        'milk': {'price': 1.50, 'quantity': 10},
        'eggs': {'price': 0.20, 'quantity': 100},
        'cheese': {'price': 2.00, 'quantity': 10}
    }

    # what does the klas for?
    def __get__(self, obj, klas):
        print("Fetching from Data Store")
        return {'products': self.products}


class BusinessLogic(object):
    """ Business logic holding data store instances. """

    data = Data()

    def product_list(self):
        return self.data['products'].keys()

    def product_information(self, product):
        return self.data['products'].get(product, None)


class Ui(object):
    """ UI interaction class """

    def __init__(self):
        self.business_logic = BusinessLogic()

    def get_product_list(self):
        print('PRODUCT LIST:')
        for product in self.business_logic.product_list():
            print(product)

        print('')

    def get_production_information(self, product):
        product_info = self.business_logic.product_information(product)
        if product_info:
            print('PRODUCTION INFORMATION:')
            print('Name {0}, Price: {1:.2f}, Quantity: {2:}'.format(
                product.title(), product_info.get('price', 0),
                product_info.get('quantity', 0)
            ))
        else:
            print('That product "{0}" does not exist in the records.'.format(
                product
            ))


class Test(object):
    data = Data()
    def __init__(self):
        import dis
        def test():
            print(self.data['products'])
        dis.dis(test)


def main():
    ui = Ui()
    ui.get_product_list()
    ui.get_production_information('cheese')
    ui.get_production_information('eggs')
    ui.get_production_information('milk')
    ui.get_production_information('apepas')

    test = Test()


if __name__ == '__main__':
    main()


"""
OUTPUT:

PRODUCT LIST:
Fetching from Data Store
eggs
milk
cheese

Fetching from Data Store
PRODUCTION INFORMATION:
Name Cheese, Price: 2.00, Quantity: 10
Fetching from Data Store
PRODUCTION INFORMATION:
Name Eggs, Price: 0.20, Quantity: 100
Fetching from Data Store
PRODUCTION INFORMATION:
Name Milk, Price: 1.50, Quantity: 10
Fetching from Data Store
That product "apepas" does not exist in the records.
"""
