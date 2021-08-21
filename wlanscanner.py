import scapy.all as scapy
import sys
import os

pipe = False

if len(sys.argv) > 1:
	if sys.argv[1] == "--pipe":
		pipe = True
		
if pipe != True:
	print("You can also pipe the ips into Portscanner.py(https://github.com/Terraminator/Threaded_Portscanner)")
	print("If you want to do this Portscanner.py must be in the same directory as this file!")
	print("Then type: \"python wlanscanner.py --pipe\"")
	yee = input("If you want to stop this script now type \"yee\")
	if yee == "yee":
		print("Aborting ...")
		sys.exit()
	

request = scapy.ARP()
request.pdst = "192.168.178.1/24"
broadcast = scapy.Ether()
broadcast.dst = "ff:ff:ff:ff:ff:ff"
request_broadcast = broadcast/request
clients = scapy.srp(request_broadcast, timeout = 3, verbose=0)[0]
print("Ip" + " "*32 + "Mac")
ips = ["172.217.16.68"]
for sent,received in clients:
	print(f"{received.psrc}"+" "*18+f"{received.hwdst}")
	ips.append(received.psrc)
	
if pipe:
	if "Portscanner.py" in os.listdir():
		f = open("ips.txt", "a+")
		for ip in ips:
			f.write("\n" + ip)
		f.close()
		os.system("python Portscanner.py")
	else:
		print("Pipe into Portscanner failed!")
		print("Portscanner.py has to be in the same Directory as this File!")
		print("The Code is here: https://github.com/Terraminator/Threaded_Portscanner")
		input("PRESS ENTER TO FINISH")
		sys.exit()