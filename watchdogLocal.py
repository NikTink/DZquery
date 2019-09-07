from time import sleep
from watchgod import watch
import json

def start(label):
	def reload_label(label):
		with open('./config/config.json') as json_file:
			config = json.load(json_file)
		label.master.geometry("+"+config["config"]["PfromSide"]+"+"+config["config"]["PfromTop"])
		label.config(bg=config["config"]["BGColour"])
		label.config(fg=config["config"]["TextColour"])
		label.master.wm_attributes("-transparentcolor", config["config"]["BGColour"])
		
	for changes in watch("./config/"):
		reload_label(label)