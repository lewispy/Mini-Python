from turtle import Turtle


class Writer(Turtle):  # The class that writes player's text input on console
	def __init__(self):
		super().__init__()
		self.penup()
		self.hideturtle()
		self.color("blue")

	def write_to(self, x, y, state):
		self.goto(x, y)
		self.write(
			f"{state}",
			align="center",
			font=("Arial", 9, "normal")
		)
