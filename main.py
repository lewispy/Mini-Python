from console import Console
from updater import Updater
from writer import Writer
import pandas as pd

# Define global variables
x_val = None
y_val = None
ENTERING = True
NUM = 0
filled_states = []

# Instantiate required objects
console = Console()
writer = Writer()
updater = Updater()

# Read US States Data
df = pd.read_csv("50_states.csv")
df_dict = df.to_dict()  # Convert data to dictionary
state_list = list(df_dict["state"].values())  # Convert state entry to list

# Start the loop for entering the US States
while ENTERING:
	if len(filled_states) == len(state_list):
		updater.state_status(val=2, state=None)
		ENTERING = False  # Loop should end if all the US states have been correctly entered
	elif len(filled_states) < len(state_list):
		user_state = console.text_prompt(NUM)
		if user_state in state_list:
			updater.state_status(val=None, state=None)
			if user_state not in filled_states:
				for key, value in df_dict["state"].items():
					if value == user_state:
						x_val = df_dict["x"][key]
						y_val = df_dict["y"][key]
				writer.write_to(x=x_val, y=y_val, state=user_state)
				filled_states.append(user_state)
				NUM += 1
				if NUM > 0:
					console.prompt = "Enter another US state"
			else:
				updater.state_status(val=1, state=user_state)
		else:
			updater.state_status(val=0, state=user_state)
			missed_states = [{
						"state": state,
						"x": df[df["state"] == state]["x"].values[0],
						"y": df[df["state"] == state]["y"].values[0]
					} for state in state_list if state not in filled_states]
			missed_states_df = pd.DataFrame(missed_states).rename(columns={"state":"missed states"})
			missed_states_df.to_csv("missed_states.csv", index=False)
			ENTERING = False

console.exit_console()
