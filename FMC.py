import os
import time
import sys

logo = """
█▀ █▄ ▄█ ▄▀▀
█▀ █ ▀ █ ▀▄▄
"""
Version = "Version 1.0"

terminal_launched = True
print(logo)
print(Version)
print("")
print("[1]	")
print("[2]	")
print("[3]	Setting")
print("------------")
print("[4]	exit")
terminal_name = "> "
user_command = ""

while terminal_launched:
	user_command = input(f"{terminal_name} ")

	if user_command == "1":
		print("coming soon")
	
	elif user_command == "2":
		print("coming soon")

	elif user_command == "3":
		print("-------------------------------------")
		print("Created by chocolatine_FR")
		print("\
-------------------------------------\n\
LIST OF AVAILABLE COMMANDS\n\
-------------------------------------\n\
4 or S : Close Terminal\n\
-------------------------------------")
	elif user_command == "4":
		terminal_launched = False

	elif user_command == "s":
		terminal_launched = False

	else:
		print("Commande introuvable...")