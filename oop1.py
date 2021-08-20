# colors = {
# "black": {
# "category": "hue",
# "type": "primary",
# "code": {
# "rgba": [255,255,255,1],
# "hex": "#000"
# }
# },
# "white": {
# "category": "value",
# "code": {
# "rgba": [0,0,0,1],
# "hex": "#FFF"
# }
# },
# "red": {
# "category": "hue",
# "type": "primary",
# "code": {
# "rgba": [255,0,0,1],
# "hex": "#FF0"
# }
# },
# "blue": {
# "category": "hue",
# "type": "primary",
# "code": {
# "rgba": [0,0,255,1],
# "hex": "#00F"
# }
# },
# "yellow": {
# "category": "hue",
# "type": "primary",
# "code": {
# "rgba": [255,255,0,1],
# "hex": "#FF0"
# }
# },
# "green": {
# "category": "hue",
# "type": "secondary",
# "code": {
# "rgba": [0,255,0,1],
# "hex": "#0F0"
# }
# }
# }

class Dog:
	name = 'Oscar'
	noise = 'Woof'
	def namenoise(self):
		print(self.name + ' Says ' + self.noise + " " + self.noise )
d = Dog()
d.namenoise()


class Phone:
	model = 'Samsung'
	color = 'Black'
	def svm(self):
		print('Heeey,I have found', self.model + ' What color ?' ' is' ,self.color )
f = Phone()
f.svm()


class Car:
	def __init__(self,color,model,name):
		self.color = color
		self.model = model
		self.name = name
	def toto(self):
		print('This car is mine: ', self.color, self.model, self.name)
h = Car('Black', 'Mercedes-Benz', 222)
h.toto()
