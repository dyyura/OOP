

class Cars:
	def gre(self):
		pass
class Moto(Cars):
	def sre(self,world):
		print(world + '!')
a = Moto()
a.sre('Hello')

class Person:
	name = 'Ivan'
	age = 34
	def __sss(self,name,age):
		self.name = name
		self.age = age
class Student(Person):
	course = 2
a = Student()
a._Person__sss('Isac',24)
a.course = 3
print(a.course)

class Factory:
	def lol(self):
		return 'Engine is ready'
	def bro(self):
		return 'Motor is ready'
q = Factory()
print(q.lol())
print(q.bro())

class Tayota(Factory):
	def wheels(self):
		return 'Wheels are ready'
	def color(self):
		return 'Color is painted'
t = Tayota()
print(t.wheels())
print(t.color())
x = [q.lol(), q.bro(), t.wheels(), t.color()]
print(x) 

class Phone:
	number = '999-999'
	def print_num(self):
		print('Phone number is: ', self.number)
my_num = Phone()
my_num.print_num()


class Water:
	name = 'ASU'
	__code = '2313464'
	def fen(self):
		print('Ring - Ring')
	def __kor(self):
		print('Chin - Chin',self.__code)
asd = Water()
asd._Water__kor()
asd.fen()
print(dir(asd))

class Phone:
        username = 'Baiel'
        __number = '999-999'

        def call(self):
                print('Ring- Ring')
        def __turn_on(self):
                print('Num on:', self.__number)
myphone = Phone()
myphone._Phone__turn_on()
print(dir(myphone)) #dir vidit vse funkcii i atributy