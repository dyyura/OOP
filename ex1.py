class Student():
	def get_student_info(self,name,lastname,department,year_of_entrance):
		return f'{name} {lastname} поступил в {year_of_entrance} на факультет {department}'
a = Student()
print(a.get_student_info('Вася', 'Иванов','программирование','2017'))
