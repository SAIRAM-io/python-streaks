# create empty dictionary
my_dict = {}

# dictionary (key : value) pair
my_dict = {1: 'red', 2: 'green', 3: 'blue'}
print(my_dict)

my_dict = {'name': 'Ram', 1: ['red', 'green']}
print(my_dict)

# using dict()
my_dict = dict({1: 'red', 2: 'green', 3: 'blue'})
print(my_dict)

# Accessing Elements
# indexing
my_dict = {'name': 'Ram', 1: ['red', 'green']}
print(my_dict['name'])
print(my_dict['age'])               # throw an error

# get() method
my_dict = {'name': 'Ram', 1: ['red', 'green']}
print(my_dict.get('name'))
print(my_dict.get('age'))               # returns None

# adding new key:value
my_dict = {'name': 'Ram', 1: ['red', 'green']}
my_dict['age'] = 23
print(my_dict)

# Update an element
my_dict = {'name': 'Ram', 1: ['red', 'green']}
my_dict[1] = 'something'
print(my_dict)

# Remove an element
my_dict = {1: 'red', 2: 'green', 3: 'blue'}
my_dict.pop(1)          # removes element with key=1
my_dict.popitem()       # removes random key:value pair
print(my_dict)

# List all keys and values
my_dict = {1: 'red', 2: 'green', 3: 'blue'}
print(list(my_dict.keys()))
print(list(my_dict.values()))

# dictionary to list
my_dict = {1: 'red', 2: 'green', 3: 'blue'}
print(list(my_dict))			# only returns keys
print(list(my_dict.items()))

# dictionary comprehension
my_dict = {i: i+100 for i in range(10)}
print(my_dict)

# dictionary and membership operator
my_dict = {1: 'red', 2: 'green', 3: 'blue'}
print(1 in my_dict)                 # True
print('red' in my_dict)             # False
print('red' in my_dict.values())    # True



