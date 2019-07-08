print("loading...")
import getGameServer, getInfo, getIpPort, time, socket, sys, json, tkinter, win32api, win32con, pywintypes, threading, os
from ctypes import *


data={
  "config": {
	"updateRate": 60,
	"PfromTop": "1000",
	"PfromSide": "1760",
	"TextColour": "green",
	"BGColour": "black"
  }
}
exists = os.path.isfile('config.json')
if exists==False:
	print("config.json missing... creating")
	with open('config.json', 'w') as outfile:
		json.dump(data, outfile)



print("system prepared")

STD_OUTPUT_HANDLE = -11
 
class COORD(Structure):
	pass
 
COORD._fields_ = [("X", c_short), ("Y", c_short)]
 
def print_at(r, c, s):
	h = windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
	windll.kernel32.SetConsoleCursorPosition(h, COORD(c, r))
 
	c = s.encode("windows-1252")
	windll.kernel32.WriteConsoleA(h, c_char_p(c), len(c), None, None)


def get_ip():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	try:
		# doesn't even have to be reachable
		s.connect(('10.255.255.255', 1))
		IP = s.getsockname()[0]
	except:
		IP = '127.0.0.1'
		#should never end up here!!
		print("OOPS! SOMETHING WENT WRONG!")
	finally:
		s.close()
	return IP
sys.stdout.write("waiting for server connection...	 ")
sys.stdout.flush()
localip= str(get_ip())
IPPORT=[localip,2304]
IPPORTref=[localip,2304]

while IPPORT==IPPORTref:
	IPPORT=getGameServer.getServerIp()

sys.stdout.write("Server found at {} \n".format(IPPORT))
sys.stdout.flush()
QUERYIPPORT=None
retryTime=60
while QUERYIPPORT==None:
	
	QUERYIPPORT=getIpPort.getIpPort(IPPORT)
	if QUERYIPPORT==None:
		print_at(3,0,"failed to get query-port... retrying in {} seconds".format(str(retryTime)))
		for sec in range(1,retryTime):
			time.sleep(1)
			print_at(3,28,"retrying in {} seconds ".format(retryTime-sec))
print("Queryport {} found... beginning scans".format(QUERYIPPORT[1]))
global i
i=0

def refreshStats(label):
	while True:
		if QUERYIPPORT!=None:
			with open('config.json') as json_file:
				data = json.load(json_file)
			
			global i
			i+=1
			info=getInfo.GetInfo(QUERYIPPORT)
			print_at(6,0,"Players: {}/{} \nTime:	{}\n {}".format(info["Players"], info["MaxPlayers"], (info["Tags"].split(","))[-1], i))
			label.config(text="Players: {}/{} \n  Time:	 {}".format(info["Players"], info["MaxPlayers"], (info["Tags"].split(","))[-1]))
		else:
			print("query port not found")
		time.sleep(data["config"]["updateRate"])
def refStarter(label):
	t=threading.Thread(target=refreshStats, args=(label,))
	t.start()

label = tkinter.Label(text='Loading...', font=('verdana ','16'), fg=data["config"]["TextColour"], bg=data["config"]["BGColour"])
label.master.overrideredirect(True)
with open('config.json') as json_file:
				data = json.load(json_file)
label.master.geometry("+"+data["config"]["PfromSide"]+"+"+data["config"]["PfromTop"])
label.master.lift()
label.master.wm_attributes("-topmost", True)
label.master.wm_attributes("-disabled", True)
label.master.wm_attributes("-transparentcolor", data["config"]["BGColour"])
label.after(1 ,refStarter(label))
hWindow = pywintypes.HANDLE(int(label.master.frame(), 16))
exStyle = win32con.WS_EX_COMPOSITED | win32con.WS_EX_LAYERED | win32con.WS_EX_NOACTIVATE | win32con.WS_EX_TOPMOST | win32con.WS_EX_TRANSPARENT
win32api.SetWindowLong(hWindow, win32con.GWL_EXSTYLE, exStyle)
label.pack()
label.mainloop()
