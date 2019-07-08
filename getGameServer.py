#responsible for sniffing the DayZ client UDP-traffic at port 2304
from scapy.all import *
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

def getServerIp():
	packet=sniff(filter='udp and port 2304', count=1)
	dstIP=packet[0][IP].dst
	dstPORT=packet[0][UDP].dport
	return([str(dstIP),int(dstPORT)])
	
if __name__ == '__main__':
	print(getServerIp())
	input("press enter to continue...")
