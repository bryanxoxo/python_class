the_count = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
stocks = ["AAPL", "GOOG", "TSLA"]
random_things = ["Puppies", 55, "Anthony Weiner", 1/2, ["Oh no", "A list inside a list"]]

# This for-loop goes through a list
for number in the_count: 
	print("this is count", number)

#same as the above

for stock in stocks:
	print("Stock Ticker:", stock)


# we can go through mised lists too
# I called it i (short for item, since i Don't know what's in it)
for i in random_things:
	print("here's a random thing:", i)


#we can also build lists, first let's start with an empty one. 
people = []
people.append("Bryan")
people.append("Lauren")
people.append("Fry")
people.append("Frankie")

print(people)

people.remove("Frankie")
print(people)

for person in people:
	print("Person is", person)


for number in the_count:
	print("this is count", number)


#here's how we access elements of a list
animals = ['bear', 'tiger', 'penguin', 'zebra']
first_animal = animals[0]
third_andimal = animals[2]

print(first_animal)
print(third_andimal)


print("There are this many things:", len(random_things))

print("things is a:", type(random_things))

another_list = random_things[-1]
print(another_list)
print(type(another_list))

another_list_first = another_list[0]
print(another_list_first)




