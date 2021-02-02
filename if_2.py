answer = input("Do you want to hear a joke?")

affirmative_answer = ["Yes", "yes", "yeah", "y", "Y", "sure", "go for it"]
negative_responses = ["No", "no", "n", "N", "nah", "no thanks", "no thank you", "nah brah"]

if "y" in answer.lower(): 
	print("I'm against picketing, but I don't know how to show it.")
	# Mitch Hedburg (RIP)
elif "n" in answer.lower():
	print("Fine.")
else:
	print("I don't understand.")
