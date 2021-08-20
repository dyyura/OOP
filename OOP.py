# from Nasledovanie import Person	# importiruem classy iz raznyh deictoriy

# # class Person:
# # 	name = 'Aidar'
# # 	def display(self):
# # 		print('Hey, are you ',self.name)
# # c = Person()
# # c.display()
# # s = Person()
# # s.name = 'Ramil'
# # s.display()
# # d = Person()
# # d.name = 'Kirill'
# # d.display()

#  # __init__ # magic element 



# # class Person: # Создаем класс задаем ему Нзавание
# #         def init(self, name , surname): #Используем функцию используем мет>
# # #Его вызывает Python при создании нового экземпляра этого класса
# #                 self.name = name #вызываем определенный аргумент
# #                 self.surname = surname # Тут также
# #         def display(self): #С помощью метода мы наследуемся и принимаем  опред>
# #                 print("Привет меня зовут", self.name, 'возрраст', self.surname>
# # # Нащ аргумент который будет присвоеен к нашему значению 
# # p = Person("Нурмамат", 17)  #Тут мы присвоили к переменной p наш класс который>
# # <й переменной  и он будет выводить наш принт
# # p.display()


# # class Person: 
# # 	def __init__(self, name, surname, age):
# # 		self.name =  name 
# # 		self.surname = surname
# # 		self.age = age
# # 	def display(self):
# # 		print('Hey my name is', self.name,'surname ', self.surname,' age',self.age)
# # c = Person('Aidar','Anarkulov',21)
# # c.display()
 
class Animal:
    def sep(self):
        print(' sound... ')
class Cat(Animal):
    def kow(self):
        print(' meow meow, wake up')
class Dog(Animal):
    def row(self):
        print(' woof woof, wake up')

a = Cat()
a.sep()
a.kow()
a = Dog()
a.sep()
a.row()

class House: 
    def mom(self):
        print('big')
class Room(House):
    def seo(self):
        print(' luxury kitchen')
class Garden(House):
    def lol(self):
        print(' green grass ')
class Bathroom(House):
    def pip(self):
        print(' smart toilet ')
c = Room()
c.mom()
c.seo()
c = Garden()
c.mom()
c.lol()
c = Bathroom()
c.mom()
c.pip()


class Desk:
    def __init__(self,cholk,rag,color):
        self.cholk = cholk
        self.rag = rag
        self.color = color
    def xex(self):
        print('red',self.cholk + 'dirty', self.rag + 'white', self.color)
d = Desk ('cholk, ','rag,','color desk')
d.xex()