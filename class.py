# class person:
# 	name = 'Aktan'
# 	age = 21

# 	def set(self)
# 		self.name = name
# 		self.age = age


# artur = person()
# self.
# artur.name = 'Toxa'
# print(artur.name)


class Car:
	# SOZDAEM ATRIBUT (peremennye)
	name = 'Mercedes-Benz'
	model = 'Maybach'
	klass = '222'
    # SOZDAEM METOD (def - method not function) KLASSA
	def start(self,name, klass):
		self.klass = '223'
		self.name = 'BMW'
		return ('engine car')
	def stop(self):
		return ('stop car')
car_a = Car() # vyzyvaem class
# DLYA PROSMOSTRA EKZEMPLYARA CLASSA
print(car_a.model)			
print()