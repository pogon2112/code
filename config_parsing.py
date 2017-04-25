#!/usr/bin/python
#Title: Network Devices and Firewall Rules Vizualization Tool
#Author: Daniel Zielinski

#Import modules
import sys, os

def file_parsing():
	filename = raw_input("Enter the name of the file or the path to the file: ")
	w = 'access-list'
	with open(filename) as f:
		found = False
		for line in f:
			if w in line:
				print(line)
				found = True
		if not found: 
			print "Something is wrong"

#class fierwall(object):
	#def __init__(self):
		#self.text = text
	#class interface(object):
	#	interface = "init"
	#	def __init__(self):
	#		self.text = text 
	#	class rule(object):
	#		def __init__(self):
	#			self.text = text
	#		interface = "int"
	#		rule = "rule"
