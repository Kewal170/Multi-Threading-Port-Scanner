import socket
import threading
import queue

ip_address = '<ip address>'
q = queue.Queue()


def banner(ip_address): # Banner
	print("-"*100)
	print("Scanning {}".format(ip_address))
	print("-"*100)

for i in range(1,501): # Storing 500 ports in our queue
	q.put(i)

def scan(): # Defining scan option
	while not q.empty():
		protocolname = 'tcp'
		port = q.get()
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
			try:
				s.connect((ip_address,port))
				SERVICE = socket.getservbyport(port, protocolname)
				# print("Port: %s => service name: %s" %(port, SERVICE) 
				print(f"[+] Port {port} :: {SERVICE}")
			except:
				pass
		q.task_done()

for i in range(50): # Create number of threads we want to see
	t = threading.Thread(target=scan, daemon=True)
	t.start()

banner(ip_address)
q.join()
print("Finished scanning")
