
import subprocess
import socket
import re

def ping(host):
    result = subprocess.run(
        ["ping", "-n", "4", "-w", "2000", host],
        capture_output=True,
        text=True
    )

    output = result.stdout
    print(output)

    if result.returncode == 0:
        print("Status: Host is reachable")
    else:
        print("Status: Ping failed")

    times = re.findall(r"time[=<](\d+)ms", output, re.IGNORECASE)

    if times:
        average = sum(int(t) for t in times) / len(times)
        print(f"Average response time: {average:.2f} ms")
    else:
        print("No successful ping response times found.")

def check_dns(domain):
    try:
        ip = socket.gethostbyname(domain)
        print(f"DNS working: {domain} -> {ip}")
    except socket.gaierror:
        print("DNS lookup failed.")

print("=== NETWORK DIAGNOSTICS TOOL ===")

while True:
    print("\n1. Ping a host")
    print("2. Check DNS")
    print("3. Check internet connectivity")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        host = input("Enter IP address or domain: ").strip()
        if host:
            ping(host)
        else:
            print("Host cannot be empty.")

    elif choice == "2":
        domain = input("Enter domain name: ").strip()
        if domain:
            check_dns(domain)
        else:
            print("Domain cannot be empty.")

    elif choice == "3":
        print("\nChecking internet connectivity...")
        ping("8.8.8.8")
        check_dns("google.com")

    elif choice == "4":
        print("Exiting Network Diagnostics Tool.")
        break

    else:
        print("Invalid choice. Try again.")
