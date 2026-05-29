# list
# there are four collection data types in python;
# list - stores multiple items in order, it is changeable
# tuple - same as list but it is unchangeable
# set - stores unique items only
# dictionary - stores data in key:value pairs (like json)

# list built in function
lst = list()

empty_list = list()
print(len(empty_list))

# using square brackets

lst = []

empty_list = []
print(len(empty_list))

# Lists with initial values. We use len() to find the length of a list

fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['tomato', 'potato', 'cabbage', 'onion', 'carrot']
animal_products = ['milk', 'meat', 'butter', 'yoghurt']
web_techs = ['html', 'css' ,'js', 'react', 'redux', 'node', 'mongodb']
countries = ['finland', 'estonia', 'denmark', 'sweden', 'norway']

print('Fruits:', fruits)
print('Number of fruits:', len(fruits))

print('Vegetables:', vegetables)
print('Number of vegetables:', len(vegetables))

print('Animal products:', animal_products)
print('Number of animal products:', len(animal_products))

print('Web techs:', web_techs)
print('Number of web technologies:', len(web_techs))

print('Countries:', countries)
print('Number of countries:', len(countries))

# lists can have items of different data types

lst = ['Asabeneh', 250, True, {'country':'finland', 'city':'helsinki'}] # this contains different data types

# accessing list items using positive indexing

# index starts from 0

fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[0]
print(first_fruit)

second_fruit = fruits[1]
print(second_fruit)

last_fruit = fruits[3]
print(last_fruit)

# last index, 

last_index = len(fruits) - 1
last_fruit = fruits[last_index]

print(last_index)
print(last_fruit)
print(fruits)

# accessing list items using negative indexing

fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[-4]
second_fruit = fruits[-2]
last_fruit = fruits[-1]

print(first_fruit)
print(second_fruit)
print(last_fruit)
