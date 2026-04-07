#!/usr/bin/env python3
"""
network_scan.py
A simple Python script to scan a range of IP addresses to see which hosts are up.
Designed for educational purposes (TryHackMe lab example).
"""

import subprocess
import ipaddress

def ping_host(ip):
    """Ping a host to see if it is up"""
    try:
        output = subprocess.check_output(
            ["ping", "-c", "1", "-W", "1", str(ip)],
            stderr=subprocess.DEVNULL,
            universal_newlines=True
        )
        return True
    except subprocess.CalledProcessError:
        return False

def scan_network(network):
    """Scan all hosts in a given network"""
    print(f"Scanning network: {network}")
    live_hosts = []
    for ip in ipaddress.IPv4Network(network):
        if ping_host(ip):
            print(f"[+] Host is up: {ip}")
            live_hosts.append(str(ip))
        else:
            print(f"[-] Host is down: {ip}")
    print(f"\nScan complete! Live hosts: {live_hosts}")

if __name__ == "__main__":
    network = input("Enter network (e.g., 192.168.1.0/24): ")
    scan_network(network)