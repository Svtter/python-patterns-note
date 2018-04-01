#!/usr/bin/env python
# coding: utf-8

"""
使用工厂模式以及原型来创建新的实例（如果创建实例十分昂贵）
"""

class Prototype(object):

	value = 'default'

	def clone(self, **attrs):
		"""
		clone a prototype and update inner attributes dictionary
		__class__ 是指类本身，即A

		可以使用 obj.__dict__.update(attrs) 来更新类中的变量

		"""

		obj = self.__class__()
		obj.__dict__.update(attrs)
		return obj


class PrototypeDispatcher(object):
	"""docstring for PrototypeDispatcher"""
	def __init__(self):
		self._objects = {}

	def get_objects(self):
		"""Get all objects"""
		return self._objects

	def register_object(self, name, obj):
		"""Register an object"""
		self._objects[name] = obj

	def unregister_object(self, name):
		del self._objects[name]
		

def main():
	import ipdb
	ipdb.set_trace()

	dispatcher = PrototypeDispatcher()
	prototype = Prototype()

	d = prototype.clone()
	a = prototype.clone(value='a-value', category='a')
	b = prototype.clone(value='b-value', is_checked=True)
	dispatcher.register_object('objecta', a)
	dispatcher.register_object('objectb', b)
	dispatcher.register_object('default', d)
	print([{n: p.value} for n, p in dispatcher.get_objects().items()])


if __name__ == '__main__':
	main()



"""
OUTPUT:

[{'objectb': 'b-value'}, {'default': 'default'}, {'objecta': 'a-value'}]
"""