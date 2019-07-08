import requests
import json

def getIpPort(addrport):
	addr=addrport[0]
	port=addrport[1]
	url="https://api.steampowered.com/ISteamApps/GetServersAtAddress/v1/?addr={}".format(addr)
	r = requests.get(url)
	
	if r.status_code == 200:
		dict=json.loads(r.content.decode())
		for member in dict["response"]["servers"]:
			if int(member["gameport"])==port:
				return(member["addr"].split(":")[0],int(member["addr"].split(":")[1]))
		
	else:
		return("[ERROR] "+r.status_code)
		

if __name__ == '__main__':
	IP=input("IP: ")
	PORT=int(input("PORT: "))
	print(getIpPort(IP,PORT))
	input("press enter to continue...")