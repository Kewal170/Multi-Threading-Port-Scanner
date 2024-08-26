import queue
import socket
import threading
import logging
from colorama import Fore, Style, init

# Configuration
IP_ADDRESS = '192.168.137.1'
PORT_RANGE = range(1, 1001)  # Ports to scan
NUM_THREADS = 50  # Number of threads to use
VERBOSE = False  # Disable verbose mode to only show open ports

# Initialize colorama
init(autoreset=True)

# Set up logging
logging.basicConfig(filename='scan_results.log', level=logging.INFO, format='%(message)s')

# Queue for managing ports
q = queue.Queue()

def banner(ip):
    """Display a banner with the IP address being scanned."""
    print(Fore.CYAN + "-" * 100)
    print(Fore.GREEN + f"[*] Scanning {ip}")
    print(Fore.CYAN + "-" * 100)

def scan_port(port):
    """Check if a port is open and return service information."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)  # Set a timeout to avoid long hangs
            s.connect((IP_ADDRESS, port))
            service = socket.getservbyport(port, 'tcp')
            return port, service
    except (socket.timeout, ConnectionRefusedError, OSError):
        return port, None

def worker():
    """Thread worker function to process ports."""
    while True:
        port = q.get()
        if port is None:
            break
        port, service = scan_port(port)
        if service:
            message = f"[+] Port {port} :: {service}"
            print(Fore.GREEN + message)
            logging.info(message)
        q.task_done()

def main():
    """Main function to set up threads and start scanning."""
    # Fill the queue with ports
    for port in PORT_RANGE:
        q.put(port)

    # Start threads
    threads = []
    for _ in range(NUM_THREADS):
        t = threading.Thread(target=worker)
        t.start()
        threads.append(t)

    # Wait for all ports to be processed
    q.join()

    # Stop workers
    for _ in range(NUM_THREADS):
        q.put(None)
    for t in threads:
        t.join()

    print(Fore.CYAN + "-" * 50)
    print(Fore.YELLOW + "Finished scanning")
    print(Fore.YELLOW + "Results are saved in 'scan_results.log'")

if __name__ == "__main__":
    banner(IP_ADDRESS)
    main()
