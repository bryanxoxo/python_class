answer = input("Do you want to hear a joke?").casefold()

if answer.lower() == "yes":
	print("I'm against picketing, but I don't know how to show it.")
	# Mitch Hedburg (RIP)
elif answer.lower() == "no":
	print("Fine.")
else:
	print("I don't understand.")
