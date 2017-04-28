 #!/usr/bin/python
#Title: Network Devices and Firewall Rules Vizualization Tool
#Author: Daniel Zielinski

import sys, os

def ip_parsing():
	ip_addr = raw_input("Please eneter the IP address: ")
	os.system("nmap --min-rate 1000 " + ip_addr)
	#os.system("nmap -A --min-rate 1000 --open --reason " + ip_addr)

