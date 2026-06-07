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

# joining, using extend()

num1 = [0, 1, 2, 3]
num2 = [4, 5, 6]

num1.extend(num2)
print('Numbers:', num1)

negative_numbers = [-5, -4, -3, -2, -1]
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]

negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)

print('Integers:', negative_numbers)

fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']

fruits.extend(vegetables)
print('fruits and vegetables:', fruits)


# counting items in a list
# The count() method returns the number of times an item appears in a list:

fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))

ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))

# finding index of an item 
# The index() method returns the index of an item in the list:

fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))

ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24)) # prints the first occurence.


# reversing a list
#  reverse(), reverses the order of the list

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits)

ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages)

# sorting list items

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
print(fruits)

fruits.sort(reverse=True)
print(fruits)

ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages)

ages.sort(reverse=True)
print(ages)

# using sorted(), returns the ordered list without modifying the original list

fruits = ['banana', 'orange', 'mango', 'lemon']
print(sorted(fruits))

# reverse order

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits = sorted(fruits, reverse=True)

print(fruits)


# tasks

empty_list = []

cars = ['bmw', 'mercedes', 'byd', 'changan', 'honda', 'kia', 'hyundai']
print(len(cars))

first_car = cars[0]
print(first_car)

middle_car = cars[len(cars) // 2]
print(middle_car)

last_car = cars[-1]
print(last_car)

mixed_data_types = ['mubaraq', 18, 192, 'single', 'interstellar']
print(mixed_data_types)
print(len(mixed_data_types))

it_companies = ['facebook', 'google', 'microsoft', 'apple', 'ibm', 'oracle', 'amazon']
print(it_companies)
print(len(it_companies))

first_company = it_companies[0]
print(first_company)

middle_company = len(it_companies) // 2
it_companies.pop(middle_company)
print(it_companies)

last_company = it_companies[-1]
print(last_company)

it_companies.pop()
print(it_companies)

it_companies.append('meta')
print(it_companies)

it_companies.insert(3, 'tesla')
print(it_companies) # couldn,t do it dynamically

it_companies[2] = it_companies[2].upper()
print(it_companies)


result = '#; '.join(it_companies)
print(result)

does_exist = 'meta' in it_companies
print(does_exist)

it_companies.sort()
print(it_companies)

it_companies.reverse()
print(it_companies)

first_three_companies = it_companies[0:3] 
print(first_three_companies)

last_three_companies = it_companies[-3:]
print(last_three_companies)

middle_company = it_companies[len(it_companies) // 2]
print(middle_company)

first_company = it_companies.pop(0)
print(first_company)
print(it_companies)

middle_company = len(it_companies) // 2
it_companies.pop(middle_company)
print(it_companies)

last_company = it_companies.pop(-1)
print(last_company)

it_companies.clear()
print(it_companies)

# del it_companies
# print(it_companies)

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

full_stack = front_end + back_end
print(full_stack)

full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print(full_stack)

# exercises level 2

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
print(ages)

maximum_age = max(ages)
print(maximum_age)

minimum_age = min(ages)
print(minimum_age)

ages.append(maximum_age)
print(ages)

ages.append(minimum_age)
print(ages)

ages.sort()

mid = len(ages) // 2
median = (ages[mid - 1] + ages[mid]) / 2 
print(median)

average = sum(ages) / len(ages) # didn't use floor division
print(average)

age_range = maximum_age - minimum_age
print(age_range)

compare_value = (abs(minimum_age - average), abs(maximum_age - average))
print(compare_value)

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
];

middle_country = len(countries) // 2
print(countries[middle_country])  

countries_list = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
china, russia, usa, *scandic = countries_list

print(china)    # China
print(russia)   # Russia
print(usa)      # USA
print(scandic)  # ['Finland', 'Sweden', 'Norway', 'Denmark']

mid = len(countries) // 2
first_half = countries[:mid]
second_half = countries[mid:]

print(f'first half: {len(first_half)} countries')
print(f'second half: {len(second_half)} countries')