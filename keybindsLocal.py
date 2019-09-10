from pynput.keyboard import Key, KeyCode, Listener
import json
controlKey=Key.ctrl_l
shiftKey=Key.shift
charKeyUp=Key.up
charKeyDown=Key.down
charKeyLeft=Key.left
charKeyRight=Key.right

standardMoveAmmount=1
fastMoveAmmount=30

def start(label):
	Boost=False
	
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

		move("updown",0-standardMoveAmmount)
	def function_2():

		move("updown",standardMoveAmmount)
	def function_3():

		move("leftright",0-standardMoveAmmount)
	def function_4():

		move("leftright",standardMoveAmmount)

	def function_1_1():
		move("updown",0-fastMoveAmmount)
	def function_2_1():

		move("updown",fastMoveAmmount)
	def function_3_1():

		move("leftright",0-fastMoveAmmount)
	def function_4_1():

		move("leftright",fastMoveAmmount)

	combination_to_function = {
		frozenset([shiftKey , charKeyUp]): function_1,
		frozenset([shiftKey , charKeyDown]): function_2,
		frozenset([shiftKey , charKeyLeft]): function_3,
		frozenset([shiftKey , charKeyRight]): function_4,
		frozenset([controlKey, Key.shift , charKeyUp]): function_1_1,
		frozenset([controlKey, Key.shift , charKeyDown]): function_2_1,
		frozenset([controlKey, Key.shift , charKeyLeft]): function_3_1,
		frozenset([controlKey, Key.shift , charKeyRight]): function_4_1,
	}

	current_keys = set()

	def on_press(key):
		
		current_keys.add(key)
		if frozenset(current_keys) in combination_to_function:
			combination_to_function[frozenset(current_keys)]()

	def on_release(key):
		'''
		if frozenset(current_keys) in combination_to_function:
			save()
		'''
		try:
			current_keys.remove(key)
		except Exception as e:
			print("[WARN] {}".format(e))

	with Listener(on_press=on_press, on_release=on_release) as listener:
		listener.join()