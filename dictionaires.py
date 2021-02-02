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
