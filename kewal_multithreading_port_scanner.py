import queue
import socket
import threading

ip_address = '192.168.56.1'
q = queue.Queue()


def banner(ip):  # Banner
    print("-" * 100)
    print(f"[*] Scanning {ip}")
    print("-" * 100)


for i in range(1, 1001):  # Storing 1000 ports in our queue
    q.put(i)


def scan():  # Defining scan option
    while not q.empty():
        protocol_name = 'tcp'
        port = q.get()
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.connect((ip_address, port))
                service = socket.getservbyport(port, protocol_name)
                print(f"[+] Port {port} :: {service}")
            except:
                pass
        q.task_done()


for i in range(100):  # Create number of threads we want to see
    t = threading.Thread(target=scan, daemon=True)
    t.start()

banner(ip_address)
q.join()
print("-"*50)
print("Finished scanning")
