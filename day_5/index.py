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