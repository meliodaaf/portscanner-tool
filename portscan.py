#!/usr/bin/env python3

# Usage: 
# Single target, single port -->#./portscan.py --target 192.168.1.1 --port 80
# Multiple targets and port range --> #./portscan.py --target 192.168.1.1,192.168.1.10 --port 80-100

import socket
import argparse
import sys

parser = argparse.ArgumentParser(description="Scan Ports for IP addresses")
parser.add_argument('--target', metavar='', required=True, help="Host to be targetted for scanning.")
parser.add_argument('--port', metavar='', required=True, help="Range of ports to be scanned.")

args = parser.parse_args()

target = args.target
ports = args.port

def main():

    if ',' in target:
        print("[*] Scanning multiple targets...")
        for ip_addr in target.split(","):
            scan_port(ip_addr.strip(' '), ports)
    else:
        scan_port(target, ports)


def scan_connect(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((target, port))

        if result == 0:
            print(f"[+]Port {port} is OPEN.")
        else:
            pass
        sock.close()

    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit()

    except socket.error:
        print("Could not connect to server.")
        sys.exit()


def scan_port(target, ports):
    print(f"\nScanning {target}:")
    if '-' in ports:
        t_ports = ports.split("-")
        for port in range(int(t_ports[0]), int(t_ports[1]) + 1):
            scan_connect(target, port)
    else:
        port = int(ports)
        scan_connect(target, port)


if __name__ == '__main__': main()

