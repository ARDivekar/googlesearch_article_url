## Source: http://stackoverflow.com/a/42360496/4900327 , made some modifications
class MetaEnum(type):
	def __new__(meta, subclass_name, bases, attrs):
		## This is called when we define the subclass (where we use the `class` keyword).
		## attrs is a dictionary of all the attributes passed when defining a class.
		for attr in attrs:
			if not attr.startswith("__") and not callable(attr) and str(attrs[attr]) != str(attr):
				raise AttributeError("In the definition of class `%s`, class variable `%s` cannot be set to \"%s\", it must be \"%s\""%(subclass_name, attr, attrs[attr], attr))
		return super().__new__(meta, subclass_name, bases, attrs)

	def __setattr__(subclass, attr, value):
		# print("Setting `%s` to %s"%(attr, value))
		if str(attr) != str(value):
			raise AttributeError("In the definition of class `%s`, class variable `%s` cannot be set to \"%s\", it must be \"%s\""%(subclass.__name__, attr, value, attr))
		return super().__setattr__(attr, value)


	def __iter__(self):		## Source: http://stackoverflow.com/a/5434478/4900327 , made some modifications.
		class_vars = []
		for attr in dir(self):
			if not attr.startswith("__") and not callable(attr):
				yield attr		## this allows us to return a generator which we can iterate over, I think

	def list(subclass):		## Convenience method.
		return [x for x in subclass]



class StrictEnum(metaclass=MetaEnum):
	'''	StrictEnums are classes which subclass this class.
		Only enums parameters set with an identical paramter_name = "parameter_name" pair will be allowed, both as class variables or otherwise

		Example usage:
			class SearchEngines(Enum):
				Google = "Google"
				Yahoo = "Yahho"			## will raise AttributeError
			SearchEngines.Yandex = "Yandex"
			SearchEngines.Bing = "Bong" ## will raise an AttributeError
			SearchEngines.Google  		## will return 'Google'
			SearchEngines.Yandex  		## will return 'Yandex'
			SearchEngines.list()  		## will return ['Google', 'Yandex']
			obj = SearchEngines() 		## will raise TypeError
			"Google" in SearchEngines	## will return True
			"Google" in SearchEngines.list()	## will return True
			"AltVista" in SearchEngines	## will return False
	'''
	def __init__(self):		## Prevent creation of an object of StrictEnum
		raise TypeError  	## Source: https://docs.python.org/2/library/exceptions.html#exceptions.TypeError

class SearchEngines(StrictEnum):
	Google = "Google"
	Bing = "Bing"

class ProxyTypes(StrictEnum):
	Socks5 = "Socks5"

class ProxyBrowsers(StrictEnum):
	PhantomJS = "PhantomJS"
