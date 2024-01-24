from turtle import Turtle


class Updater(Turtle):  # A turtle class to write player notifications to console
	def __init__(self):
		super().__init__()
		self.penup()
		self.hideturtle()
		self.color("red")

	def state_status(self, val, state):
		self.goto(0, 0)
		if val == 0:
			self.clear()
			self.write(
				f"Sorry! No such state '{state}' in the US.",
				align="center",
				font=("Courier", 16, "bold")
			)  # The player should be notified that there is no such state in the US
		elif val == 1:
			self.write(
				f"{state} already guessed. Please guess another state.",
				align="center",
				font=("Courier", 16, "bold")
			)  # The player should be told that the state has been guessed already
		elif val == 2:
			self.color("green")
			self.write(
				f"CONGRATS! YOU GUESSED ALL US STATES.",
				align="center",
				font=("Courier", 18, "bold")
			)  # The player should be informed that all states have been correctly guessed
		else:
			self.clear()
