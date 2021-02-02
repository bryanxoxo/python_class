# states = ['NY', 'PA', 'CA']
# states = ['New York', 'Pennsylvania', 'California']
# states = ['New York', 'NY', 'Pennsylvania', 'PA', 'California', 'CA']

states = {'NY': 'New York', 'PA': 'Pennsylvania', 'CA': 'California'}

print(states['NY'])

# print(states['FL'])

people = ["Bryan", "Lauren"]

print(type(states))
print(type(people))

print(states.get('FL', 'Not Found'))
print(states.get('NY', 'Not Found'))


#print(states.keys())
#print(states.values())

#states['FL'] = 'Florida'
#print(states)

user = {'Name': 'Bryan', 'Height': '6\'1\"', 'Shoe Size': 9, 'Hair': 'Redish-Brown'}

print("Hi", user['Name'])
print(user['Name'], "your Height is:", user['Height'])

# DICTIONAIRE AND LISTS CAN BE INSIDE OF EACH OTHER!

animal_sounds = {
    "cat": ["meow", "purr"],
    "dog": ["woof", "bark"],
    "fox": []
}

bryan = {'Name': 'Bryan', 'Height': '6\'1\"', 'Shoe Size': 9, 'Hair': 'Redish-Brown'}
chris = {'Name': 'Chris', 'Height': '5\'11\"', 'Shoe Size': 12, 'Hair': 'Black'}
emily = {'Name': 'Emily', 'Height': '5\'3\"', 'Shoe Size': 7.5, 'Hair': 'Blonde'}

people = [bryan, chris, emily]

print(people)

for get_user_info in people:
    print(get_user_info.get('Height'))
