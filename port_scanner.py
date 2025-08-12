import socket
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

# Banner
print("="*50)
print("      Port Scanner Tool - 2024 Edition")
print("="*50)

# User input
target = input("Enter the target IP or domain: ").strip()
port_start = int(input("Enter start port: "))
port_end = int(input("Enter end port: "))

# Resolve target
try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Error: Unable to resolve hostname.")
    exit()

# Display scan info
print(f"\nScanning Target: {target} ({target_ip})")
print(f"Scanning from port {port_start} to {port_end}")
print("Scan started at:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print("-"*50)

# Function to scan a single port
def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((target_ip, port))
        if result == 0:
            try:
                banner = s.recv(1024).decode().strip()
            except:
                banner = "No banner"
            print(f"[OPEN] Port {port} - {banner}")
        s.close()
    except KeyboardInterrupt:
        print("\nScan aborted by user.")
        exit()
    except Exception:
        pass

# Use multi-threading for speed
with ThreadPoolExecutor(max_workers=100) as executor:
    for port in range(port_start, port_end + 1):
        executor.submit(scan_port, port)

print("\nScan completed at:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print("="*50)
