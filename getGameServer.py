#responsible for sniffing the DayZ client UDP-traffic at port 2304
from scapy.all import *
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

def getServerIp():
	try:
		packet=sniff(filter='udp and port 2304', count=1)
		dstIP=packet[0][IP].dst
		dstPORT=packet[0][UDP].dport
		return([str(dstIP),int(dstPORT)])
	except Exception as e:
		#print ("\n[ERROR] "+str(e))
		if "winpcap" in str(e):
			print ("\n[ERROR] Sniffing packets is not available: WINPCAP is not installed.")
		else:
			print(e)
		input("Press enter to continue..")
		os._exit(0)
		return(["false",0000])
		
		
		
	

	
if __name__ == '__main__':
	print(getServerIp())
	input("press enter to continue...")
