import random

#Our Star Wars Event
SWEvent = ["The Battle at Geonosis",
				"Gordula the Hutt's birthday party",
				"Darth Maul's battle in the Naboo Recator Core",
				"Empereror Palpatine oath of office",
				"Obi-Wan's Knighting Ceremony"]

#our random_character
SWCharacter = ["Leia Organa",
				  "Luke Sykwalker",
				  "Darth Vader",
				  "Sy Snoodles",
				  "Boba Fett"]

SexAct = ["BlowJob",
			"RimJob",
			"Handy",
			"Full blown Intercourse"]

random_event = random.choice(SWEvent)
random_character = random.choice(SWCharacter)
random_sexact = random.choice(SexAct)

print(f"I'm telling you...I totally saw {random_character} getting a {random_sexact} at {random_event}.")
