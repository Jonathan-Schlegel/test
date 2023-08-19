class Shape:
	def __init__(self, side1, side2):
		self.side1 = side1
		self.side2 = side2

	def get_area(self):
		return self.side1 * self.side2

	def __str__(self):
		return f'The area of this {self.__class__.__name__} is: {self.get_area()}'
	
class Rectangle(Shape):
	pass


class Square(Rectangle):
	def __init__(self, side):
		super().__init__(side, side)


print(Rectangle(2, 3).__str__())
print(Square(2).__str__())