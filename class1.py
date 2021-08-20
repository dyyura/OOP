# class Notebook:
# 	def __init__(self,model_name):
# 		self.model = model_name
# 		self.character = []
# 		self.proccesor = ()
# 		self.ram = ()
# 		self.video_card = ()
# 		self.hdd = ()
# 		self.ssd = ()
# 		self.motherboar = ()
# 		self.display_size = ()

# 	def proccesor(self):
# 		self.character.append('Core i5')

# 	def ram(self):
# 		self.character.append('8 gb')
# 	def video_card(self):
# 		self.character.append('2 gb')
# 	def hdd(self):
# 		self.character.append('400 gb')
# 	def ssd(self):
# 		self.character.append('128 gb')
# 	def motherboar(self):
# 		self.character.append('HZ')
# 	def display_size(self):
# 		self.character.append('15 D')

# notebook = Notebook(model_name = 'Packard Bell')
# print(notebook.model)
# print(notebook.character)

class Laptop:
	def __init__(self, model_name):
		self.model = model_name
		self.harakteristiki = []
		self.processor()
		self.ram()
		self.video_card()
		self.hdd()
		self.ssd()
		self.motherboard()
		self.display_size()

	def processor(self):
		self.harakteristiki.append('Core i5')

	def ram(self):
		self.harakteristiki.append('8 gb')
	def video_card(self):
		self.harakteristiki.append('2 gb')

	def hdd(self):
		self.harakteristiki.append('400 gb')

	def motherboard(self):
		self.harakteristiki.append('hz')

	def display_size(self):
		self.harakteristiki.append('15 d')
	def ssd(self):
		self.harakteristiki.append('128 gb')


laptop = Laptop(model_name='Packard Bell')
print(laptop.model)
print(laptop.harakteristiki)