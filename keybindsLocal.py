from pynput.keyboard import Key, KeyCode, Listener
import json
controlKey=Key.shift
charKeyUp='i'
charKeyDown='k'
charKeyLeft='j'
charKeyRight='l'


# Your functions

def start(label):
	
	def load():
		with open('./config/config.json') as json_file:
			config = json.load(json_file)
	load()
	def move(dir,ammount):
		with open('./config/config.json') as json_file:
			config = json.load(json_file)
		if dir=="updown":
			config["config"]["PfromTop"] = str(int(config["config"]["PfromTop"])+ammount)
			label.master.geometry("+"+config["config"]["PfromSide"]+"+"+config["config"]["PfromTop"])
		if dir=="leftright":
			config["config"]["PfromSide"] = str(int(config["config"]["PfromSide"])+ammount)
			label.master.geometry("+"+config["config"]["PfromSide"]+"+"+config["config"]["PfromTop"])
		with open('./config/config.json', 'w') as outfile:
			json.dump(config, outfile)
	def save():
		pass
	def function_1():
		move("updown",0-1)
	def function_2():
		move("updown",1)
	def function_3():
		move("leftright",0-1)
	def function_4():
		move("leftright",1)

	# Create a mapping of keys to function (use frozenset as sets are not hashable - so they can't be used as keys)
	combination_to_function = {
		frozenset([Key.shift , Key.up]): function_1, # No `()` after function_1 because we want to pass the function, not the value of the function
		frozenset([Key.shift , Key.down]): function_2,
		frozenset([Key.shift , Key.left]): function_3,
		frozenset([Key.shift , Key.right]): function_4,
	}

	# Currently pressed keys
	current_keys = set()

	def on_press(key):
		# When a key is pressed, add it to the set we are keeping track of and check if this set is in the dictionary
		current_keys.add(key)
		if frozenset(current_keys) in combination_to_function:
			# If the current set of keys are in the mapping, execute the function
			combination_to_function[frozenset(current_keys)]()

	def on_release(key):
		'''
		if frozenset(current_keys) in combination_to_function:
			save()
		'''
		# When a key is released, remove it from the set of keys we are keeping track of
		current_keys.remove(key)

	with Listener(on_press=on_press, on_release=on_release) as listener:
		listener.join()