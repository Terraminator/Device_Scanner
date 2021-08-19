import scapy.all as scapy
request = scapy.ARP()
request.pdst = "192.168.178.1/24"
broadcast = scapy.Ether()
broadcast.dst = "ff:ff:ff:ff:ff:ff"
request_broadcast = broadcast/request
clients = scapy.srp(request_broadcast, timeout = 3, verbose=0)[0]
print("Ip" + " "*32 + "Mac")
for sent,received in clients:
	print(f"{received.psrc}"+" "*18+f"{received.hwdst}")