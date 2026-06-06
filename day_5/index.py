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

# fruits = ['banana', 'orange', 'mango', 'lemon']
# vegetables = ['tomato', 'potato', 'cabbage', 'onion', 'carrot']
# animal_products = ['milk', 'meat', 'butter', 'yoghurt']
# web_techs = ['html', 'css' ,'js', 'react', 'redux', 'node', 'mongodb']
# countries = ['finland', 'estonia', 'denmark', 'sweden', 'norway']

# print('Fruits:', fruits)
# print('Number of fruits:', len(fruits))

# print('Vegetables:', vegetables)
# print('Number of vegetables:', len(vegetables))

# print('Animal products:', animal_products)
# print('Number of animal products:', len(animal_products))

# print('Web techs:', web_techs)
# print('Number of web technologies:', len(web_techs))

# print('Countries:', countries)
# print('Number of countries:', len(countries))

# # lists can have items of different data types

# lst = ['Asabeneh', 250, True, {'country':'finland', 'city':'helsinki'}] # this contains different data types

# # accessing list items using positive indexing

# # index starts from 0

# fruits = ['banana', 'orange', 'mango', 'lemon']
# first_fruit = fruits[0]
# print(first_fruit)

# second_fruit = fruits[1]
# print(second_fruit)

# last_fruit = fruits[3]
# print(last_fruit)

# # last index, 

# last_index = len(fruits) - 1
# last_fruit = fruits[last_index]

# print(last_index)
# print(last_fruit)
# print(fruits)

# # accessing list items using negative indexing

# fruits = ['banana', 'orange', 'mango', 'lemon']
# first_fruit = fruits[-4]
# second_fruit = fruits[-2]
# last_fruit = fruits[-1]

# print(first_fruit)
# print(second_fruit)
# print(last_fruit)

# unpacking list items

lst = ['item1', 'item2', 'item3', '1tem4', 'item5']
first_item, second_item, third_item, *rest = lst

print(first_item)
print(second_item)
print(third_item)
print(rest)

fruits = ['banana', 'orange', 'mango', 'lemon', 'lime', 'apple']
first_fruit, second_fruit, third_fruit, *rest = fruits

print(first_fruit)
print(second_fruit)
print(third_fruit)
print(rest)

first, second, third, *rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(first)
print(second)
print(third)
print(rest)
print(tenth)

countries =['germany', 'france', 'belgium', 'sweden', 'denmark', 'finland', 'norway', 'iceland', 'estonia']
gr, fr, bg, * scandic, es = countries

print(gr)
print(fr)
print(bg)
print(scandic)
print(es)

# slicing items from a list

# positive indexing - we can specify a range of positive indexes by specifying the start, end and step. the return value would be a new list

fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4]
print(all_fruits)

all_fruits = fruits[0:]
print(all_fruits)

orange_and_mango = fruits[1:3]
print(orange_and_mango)

orange_mango_lemon = fruits[1:]
print(orange_mango_lemon)

orange_and_lemon = fruits[::2]
print(orange_and_lemon)


# negative indexing - we can specify a range of negative indexes by specifing the start, stop and end. the return value would be a new list

fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[-4:]
print(all_fruits)
orange_and_mango = fruits[-3:-1]
print(orange_and_mango)

orange_mango_lemon = fruits[-3:]
print(orange_mango_lemon)

reversed_fruits = fruits[::-1]
print(reversed_fruits)

# tasks

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

first_three_numbers = numbers[0:3]
print(first_three_numbers)

last_three_numbers = numbers[-3:]
print(last_three_numbers)

three_to_seven = numbers[3:8]
print(three_to_seven)

second_number = numbers[::2]
print(second_number)

reversed_numbers = numbers[::-1]
print(reversed_numbers)

thirty_to_sixty = numbers[2:6]
print(thirty_to_sixty)


# task 2

countries = ['Nigeria', 'Ghana', 'Kenya', 'Egypt', 'Morocco', 'Ethiopia', 'Tanzania']

first_country = countries[0]
print(first_country)

last_country = countries[-1]
print(last_country)

first_three_countries = countries[0:3]
print(first_three_countries)

last_three_countries = countries[-3:]
print(last_three_countries)

every_countries = countries[::2]
print(every_countries)

reversed_countries = countries[::-1]
print(reversed_countries)


# task 3

stack = ['Python', 'Linux', 'Docker', 'AWS', 'Terraform', 'Kubernetes', 'CI/CD']

current_stage = stack[0]
print(current_stage)

end_goal = stack[-1]
print(end_goal)

devops_tools = stack[2:]
print(devops_tools)

first_two_items_reversed = stack[0:2][::-1]
print(first_two_items_reversed)

all_stack_except_last = stack[:-1]
print(all_stack_except_last)


subjects = ['Maths', 'English', 'Physics', 'Chemistry', 'Python']
scores = [85, 72, 90, 68, 95]

first_subject = subjects[0]
first_score = scores[0]
print(f'First subject and its score: {first_subject}, {first_score}')

last_subject = subjects[-1]
last_score = scores[-1]
print(f'Last subject and score is: {last_subject}, {last_score}')


first_three_subjects = subjects[0:3]
print(first_three_subjects)

last_two_subjects = subjects[-2:]
last_two_scores = scores[-2:]
print(f'{last_two_subjects}, {last_two_scores}')

subjects_reversed = subjects[::-1]
print(subjects_reversed)

best_score = scores[-1]
print(best_score)

# modifying list

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'avocado'
print(fruits)

fruits[1] = 'apple'
print(fruits)

last_index = len(fruits) - 1
fruits[last_index] = 'lime'
print(fruits)

# checking items in a list

fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)

does_exist = 'lime' in fruits
print(does_exist)

# adding items to a list
# to add an item to an existing list, we use append()

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('pear')
print(fruits)
fruits.append('lime')
print(fruits)

# inserting items into a list
# we use insert(), it takes two args, the index and the item

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'melon')
print(fruits)
fruits.insert(3, 'apple')
print(fruits)

# removing items from a list
# we use remove()

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.remove('banana')
print(fruits)
fruits.remove('lemon')
print(fruits)

# removing items using pop
# we use pop()
# The pop() method removes the specified index, (or the last item if index is not specified):

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()
print(fruits) # removes the last index because the index is not specified
fruits.pop(2)
print(fruits)

# removing items using del
# del 
# The del keyword removes the specified index and it can also be used to delete items within index range.
# It can also delete the list completely

fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[0]
print(fruits)
del fruits[1]
print(fruits)
del fruits[1:3]
print(fruits)
del fruits
# print(fruits) # deletes the list completely

# clearing list items
# clear() , empties the list

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits)

# copying a list
# copy()

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print(fruits_copy) 

# joining lists
# there are several ways to concatenate two or more lists in python:
# plus operator (+) 

# syntax 
# list3 = list1 + list2

positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5, -4, -3, -2, -1]

integers = negative_numbers + zero + positive_numbers
print(integers)

fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']

fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)