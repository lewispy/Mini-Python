from turtle import Screen


class Console:
	def __init__(self):
		self.console = Screen()
		self.console.title("US State Game")
		self.console.setup(width=725, height=491)
		self.console.bgpic("blank_states_img.gif")
		self.prompt = "Enter a state in the US"
		self.user_text = None

	def exit_console(self):
		self.console.exitonclick()

	def text_prompt(self, num):
		self.user_text = self.console.textinput(
			title=f"{num}/50 states correct",
			prompt=self.prompt
		).title()
		return self.user_text
