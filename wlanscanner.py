import scapy.all as scapy
import sys
import os

pipe = False
def banner():
	os.system("color a")
	print(r"""\



____    __    ____  __          ___      .__   __.      _______.  ______     ___      .__   __. .__   __.  _______ .______      
\   \  /  \  /   / |  |        /   \     |  \ |  |     /       | /      |   /   \     |  \ |  | |  \ |  | |   ____||   _  \     
 \   \/    \/   /  |  |       /  ^  \    |   \|  |    |   (----`|  ,----'  /  ^  \    |   \|  | |   \|  | |  |__   |  |_)  |    
  \            /   |  |      /  /_\  \   |  . `  |     \   \    |  |      /  /_\  \   |  . `  | |  . `  | |   __|  |      /     
   \    /\    /    |  `----./  _____  \  |  |\   | .----)   |   |  `----./  _____  \  |  |\   | |  |\   | |  |____ |  |\  \----.
    \__/  \__/     |_______/__/     \__\ |__| \__| |_______/     \______/__/     \__\ |__| \__| |__| \__| |_______|| _| `._____|
                                                                                                                                


                                                                                        

					""")
if len(sys.argv) > 1:
	if sys.argv[1] == "--pipe":
		pipe = True
		
banner()

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
ips = []
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