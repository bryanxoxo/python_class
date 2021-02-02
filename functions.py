# FUNCTIONS
# a function can only return one thing. however you can return a list or a dictionary to get around this.
# * You can call a function inside a function
# * Typically functions will be defined up top, and all other functions will be used later in the code.
# * Functions look like variables, but you can see that they are functions by the parenthasis i.e. greet()

def greet(name):
    return f"Hey {name}!"

print(greet('Bryan'))
print(greet('Chris'))

def concatenate(word_one, word_two):
    return word_one + word_two

print(concatenate('Dick', 'Nixon'))

def age_in_dog_years(age):
    result = age * 7
    return result


print(age_in_dog_years(34))

print(concatenate(word_two='Mattan', word_one="bryan"))

name = "Bryan"

def print_diff_name():
	name = "chris"
	#print(name)

print(name)
print_diff_name()
print(name)
