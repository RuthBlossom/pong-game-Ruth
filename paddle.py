from turtle import Turtle


class Paddle(Turtle):
	def __init__(self, position):
		super().__init__()
		self.shape("square")
		self.color("white")
		self.shapesize(stretch_wid=5, stretch_len=1)
		self.penup()
		self.goto(position)

	# remember that methods always have a first attribute as the self.
	# replace this paddle. with self. so that it's actually referring to the object
	# that's created from this class to get its Y coordinate or get its X coordinate.

	def go_up(self):
		new_y = self.ycor() + 20
		self.goto(self.xcor(), new_y)

	def go_down(self):
		new_y = self.ycor() - 20
		self.goto(self.xcor(), new_y)
