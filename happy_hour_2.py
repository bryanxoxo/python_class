import random

bars = ["Shoolbred's",
        "The Wren",
        "The Scratcher",
        "ACME",
        "Blind Barber"]

people = ["Mattan",
          "Chris",
          "that person you forgot to text back",
          "Kanye West",
          "Samuel L. Jackson",
          "Jibblets"]
then = ["Go fuck yourself.",
		"Play with some ducks.",
		"Be a smelly horse.",
		"sumo wreslte them.",
		"Watch Star Wars."]

random_bar = random.choice(bars)
random_person = random.choice(people)
random_person2 = random.choice(people)
random_then = random.choice(then)

print(f"How about you go to {random_bar} with {random_person} & {random_person2}, then {random_then}")
