# 2
# class Airplane:
# 	def __init__(self,make,model,year,max_speed,odometer,is_flying,take_off,fly,land):
# 		self.make = make
# 		self.model = model
# 		self.year = year
# 		self.max_speed = max_speed
# 		self.odometer = odometer
# 		self.is_flying = is_flying
# 		self.take_off = take_off
# 		self.fly = fly 	
# 		self.land = land
# 	def povedenie(self):
# 		print(self.make ,  self.model, self.year,  self.max_speed,  self.odometer,self.is_flying,self.take_off, self.fly, self.land)
# a = Airplane('tu 155','jet','2015','2020km/h','24 bar','False','взлёт','летать','приземлятся')
# a.povedenie() 

# 7
# Steve = Student("Steven Schultz", 23, "English")
# Johnny = Student("Jonathan Rosenberg", 24, "Biology")
# Penny = Student("Penelope Meramveliotakis", 21, "Physics")
# print(Steve)
# <name: Steven Schultz, age: 23, major: English>
# ﻿
# print(Johnny)
# <name: Jonathan Rosenberg, age: 24, major: Biology>

# class Student: 
# 	def __init__(self,name,lastname,age,objects): 
# 		self.name = name
# 		self.lastname = lastname
# 		self.age = age
# 		self.objects = objects
# 	def disp(self):
# 		print(self.name, self.lastname, self.age, self.objects)

# Steve = Student("Steven",'Shultz' , 23, "English")
# Johny = Student("Jonathan","Rosenberg", 24 , "Biology")
# Penny = Student("Penelope","Meramveliotakis", 21 , "Physics")
# Steve.disp()
# Johny.disp()
# Penny.disp()



# class House:
# 	def __init__(self,typehouse,areahouse):
# 		self.typehouse = typehouse
# 		self.areahouse = areahouse
# 	def get_house(self):
# 		self.totalarea = 0
# 		self.furnitures = {
# 		'bad ' : 4,
# 		'gardirob' : 2,
# 		'table': 1.5
# 		 }
# 	for value in self.furnitures.values():
# 		self.totalarea += value
# 	print('type of house',self.typehouse,' main area:',self.areahouse,'\n',self.furnitures.keys(),'\n','last area',self.areahouse - self.totalarea)
# c = House('apartment',80)
# b.get_house()


# class Car:
#     def call(self):
#       print('Автомобиль заведен')

# class Calls:   
#     def call(self):
#       print('Автомобиль заглушен')

# class Date:
#     def call(self):
#       print('2003')

# class Type:
#     def call(self):
#       print('Универсал')

# class Color:
#     def call(self):
#       print('Серый')

# car1 = Car()
# car2 = Calls()
# car3 = Date()
# car4 = Type()
# car5 = Color()
# a = [car1,car2,car3,car4,car5]
# for i in a:
#     i.call()


class MoneyFmt:
  def __init__(self, value = 0.0):
    self.value = float(value)
  def update(self, value = None):
    self.value = value
  def str(self):
    if self.value >= 0:
      return '${:,.2f}'.format(self.value)
    else:
      return '-${:,.2f}'.format(-self.value)
  def repr(self):
    print(self.value)
    return f'{self.value}'

cash = MoneyFmt()
class MoneyFmt:
  def init(self, value = 0.0):
    self.value = float(value)
  def update(self, value = None):
    self.value = value
  def str(self):
    if self.value >= 0:
      return '${:,.2f}'.format(self.value)
    else:
      return '-${:,.2f}'.format(-self.value)
  def repr(self):
    print(self.value)
    return f'{self.value}'

cash = MoneyFmt()

from AlphaMoney import MoneyFmt
def dollarize():

  cash = MoneyFmt(12345678.021)
  repr(cash)
  print(cash)
  cash.update(100000.4567)
  repr(cash)
  print(cash)
  cash.update(-0.3)
  repr(cash)
  print(cash)
  a1 = eval(input('Введите число и я переведу его в доллоровое значение: '))
  cash.update(a1)
  print(cash)

  a2 = input("Если хотите повторить процедуру введите '1' , для выхода введите Enter: ")
  while a2 == '1':
    a3 = eval(input('Введите число: \n'))
    cash.update(a3)
    print(cash)
dollarize()