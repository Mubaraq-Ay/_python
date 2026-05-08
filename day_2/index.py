# Variables in Python
# first_name = 'Asabeneh'
# last_name = 'Yetayeh'
# country = 'Finland'
# city = 'Helsinki'
# age = 250
# is_married = True
# skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
# person_info = {
#    'firstname':'Asabeneh',
#    'lastname':'Yetayeh',
#    'country':'Finland',
#    'city':'Helsinki'
#    }

# Printing the values stored in the variables

# print('First name:', first_name)
# print('First name length:', len(first_name))
# print('Last name: ', last_name)
# print('Last name length: ', len(last_name))
# print('Country: ', country)
# print('City: ', city)
# print('Age: ', age)
# print('Married: ', is_married)
# print('Skills: ', skills)
# print('Person information: ', person_info)

#multiple variable in a line.

# first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

# print(first_name, last_name, country, age, is_married)
# print('First name:', first_name)
# print('Last name: ', last_name)
# print('Country: ', country)
# print('Age: ', age)
# print('Married: ', is_married)

# first_name = input('what is your name: ')
# age = input('how old are you? ')

# print(first_name)
# print(age)


# # data types

# # Different python data types
# # Let's declare variables with various data types

# first_name = 'Asabeneh'     # str
# last_name = 'Yetayeh'       # str
# country = 'Finland'         # str
# city= 'Helsinki'            # str
# age = 250                   # int, it is not my real age, don't worry about it

# # Printing out types
# print(type('Asabeneh'))          # str
# print(type(first_name))          # str
# print(type(10))                  # int
# print(type(3.14))                # float
# print(type(1 + 1j))              # complex
# print(type(True))                # bool
# print(type([1, 2, 3, 4]))        # list
# print(type({'name':'Asabeneh'})) # dict
# print(type((1,2)))               # tuple
# print(type(zip([1,2],[3,4])))    # zip

# Casting: Converting one data type to another data type.
 
 #int to float
num_int = 10
print('num_int', num_int)

num_float = float(num_int)
print(num_float)

#float to in

gravity = 9.81
print(int(gravity)) # recall, it rounds down ( floor )

#int to str

num_int = 11
num_str = str(num_int)

print(num_str)

print(type(num_str))

# str to int or float

num_str = '10.8'
num_float = float(num_str)
num_int = int(num_float)

print(num_int)
print(num_float)

# str to list

first_name = 'mubaraq'
to_list = list(first_name)

print(to_list)

# numbers
# integers, float and complex numbers


