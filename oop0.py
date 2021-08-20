# OOP ()
# 1.nasledovanie = roditelskyi, dochernyi class
# 2.inkapsulaciya = public,private class 
# 3.poliformizm = beret luboi metod iz roditelskogo classa, mojno ispolzovat' beskonechno
# 4.abstrakciya =  

# class Animal:
# 	def voice(self):
# 		print('sound')
# class Dog():
# 	def voice(slef):
# 		print('woof woof')
# class Cat():
# 	def voice(self):
# 		print('meow meow')
# a = Animal()
# d = Cat()
# c = Dog()
# farm = [d,c]

# for i in (c,d,a):
# 	i.voice()

# class Country:
# 	def capital(self):
# 		print('language')
# 	def language(self):
# 		print('capital')
# class USA(Country):
# 	def capital(self):
# 		print('Washington')
# 	def language(self):
# 		print('English')

# class Italy(Country):
# 	def capital(self):
# 		print('Rome')
# 	def language(self):
# 		print('Italian')
# obj_count = Country()
# obj_usa = USA()
# obj_it = Italy()
# for i in (obj_count,obj_it,obj_usa):
# 	i.language()
# 	i.capital()

class Buildings:
	def door(self):
		pass
	def window(self):
		pass
	def roof(self):
		pass
class Elitka():
	def door(self):
		print('domofon')
	def window(self):
		print('plastikovye')
	def roof(self):
		print('cherepica')
class Dom():
	def door(self):
		print('derevyannaya')
	def window(self):
		print('plastikovaya')
	def roof(self):
		print('shifer')
f = Elitka()
g = Dom()
for i in (f,g):
	i.door()
	i.window()
	i.roof()

class Robot:
	def arms(self):
		pass
	def legs(self):
		pass
class Human():
	def arms(self):
		print('slabye')
	def legs(self):
		print('bystrye')
class Animal():
	def arms(self):
		print('srednie')
	def legs(self):
		print('normalnye')
r = Human()
r.arms()
r.legs()
h = Animal()
h.arms()
h.legs()