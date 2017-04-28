 	
 #!/usr/bin/python
#Title: Network Devices and Firewall Rules Vizualization Tool
#Author: Daniel Zielinski

#Import modules to run the script
import sys, os
import config_parsing
import ip_parsing

#Main definition - constant 	
menu_actions = {}

#Main Menu Code
def main_menu():
	
	print "Network Devices and  Firewall Rules Visualization Tool\n"
	print "Main Menu\n"
	print "1. Parse Configs Files\n"
	print "2. Live Network Vizualization\n"
	print "3. Exit\n"
	choice = raw_input (" >> ")
	exec_menu(choice)

	return

#Execute menu
def exec_menu(choice):	

	os.system('clear'),;
	ch = choice.lower()
	if ch == '' :
		menu_actions['main_menu']()
	else:
		try:
			menu_actions[ch]()
		except KeyError:
			print "Invalid selection, please choose numbers betweeen 1 to 3\n"
			menu_actions['main_menu']()
	return 

def config_parsing_menu_choice():
	config_parsing.file_parsing()
	sys.exit()

def live_scanning_menu():
	ip_parsing.ip_parsing()
	sys.exit()

def exit_program():
	sys.exit()


#Menu Definitions
menu_actions = {
	'main menu': main_menu,
	'1': config_parsing_menu_choice,
	'2': live_scanning_menu,
	'3': exit_program,
}

#Main Program
if __name__ == "__main__":
	main_menu()
