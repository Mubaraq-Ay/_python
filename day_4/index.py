# strings. 

# letter = 'p'
# print(letter)
# print(len(letter))

# greeting = 'hello, world!'
# print(greeting)
# print(len(greeting))

# sentence = 'i hope you are enjoying 30 days of python challenge'
# print(sentence)
# print(len(sentence))

# # multiline string

# multiline_string = '''my name is mubaraq and i enjoy coding and solving logical tasks'''
# print(multiline_string)

# multiline_string = """my name is mubaraq and i enjoy coding and solving logical problems."""
# print(multiline_string)

# # concatenation

# first_name = 'mubaraq'
# last_name = 'ayanleke'
# space = ' '

# full_name = first_name + space + last_name
# print(full_name)

# # checking the length of a string using len() built in function

# print(len(first_name))
# print(len(last_name))
# print(len(full_name))
# print(len(first_name) > len(last_name))

# escape sequences in strings

''' \n - new line
    \t - Tab means(8 spaces)
    \\ - back slash
    \' - single quote
    \" - double quote
'''

# print('i hope everyone is enjoying the python challenge. \nAre you?')
# print('Days\tTopics\tExercises') # adding tab space or 4 spaces.
# print('Day 1\t5\t5')
# print('Day 2\t6\t20')
# print('Day 3\t5\t23')
# print('Day 4\t1\t35')

# print('this is a backlash symbol (\\)')
# print('in every programming language it starts with \"hello, world!\"')

# string formatting

# old style formatting ( % operator )

# %s - string
# %d - integers
# %f - floating point numbers
# "%.number of digitsf" - decimal places

# for strings only

# first_name = 'mubaraq'
# last_name = 'ayanleke'
# language = 'python'
# formatted_string = 'I am %s %s. i teach %s' %(first_name, last_name, language)

# print(formatted_string)

# # for strings and numbers

# radius = 10
# pi = 3.14
# area = pi * radius ** 2
# formatted_string = 'the area of circle with a radius %d is %.2f' %(radius, area)

# print(formatted_string)

# python_libraries = ['django', 'flask', 'numpy', 'matplotlib', 'pandas']
# formatted_string = 'the following are python libraries:%s' % (python_libraries)

# print(formatted_string)

# my_name = 'mubaraq'
# age = 18

# formatting_result = "my name is %s and i'm %d years old" % (my_name, age)
# print(formatting_result)

# float_num = 2.33455
# print('to 3d.p: %.3f' % float_num)

# height = 189.66

# print("my name is %s, i'm %d years old, and my height is %.2f"  % (my_name, age, height))

# country = 'Nigeria'
# population = 220000000
# growth_rate = 2.58

# print("%s has a population of %d people with a growth rate of %.2f%%" % (country, population, growth_rate))

# item = 'laptop'
# price = 850.5678
# quantity = 3
# total = quantity * price

# print("item: %s | price: %.2f | quantity: %d | total: %.2f " % (item, price, quantity, total))

# new style (str) it was introduced in python version 3

# first_name = 'mubaraq'
# last_name = 'ayanleke'
# language = 'python'
# formatted_string = 'I am {} {}. i teach {}'.format(first_name, last_name, language)
# print(formatted_string)

# a = 4
# b = 3

# print('{} + {} = {}'.format(a, b, a + b))
# print('{} - {} = {}'.format(a, b, a - b))
# print('{} * {} = {}'.format(a, b, a * b))
# print('{} / {} = {:.2f}'.format(a, b, a / b))
# print('{} % {} = {}'.format(a, b, a % b))
# print('{} // {} = {}'.format(a, b, a // b))
# print('{} ** {} = {}'.format(a, b, a ** b))

# # strings and numbers
# radius = 10
# pi = 3.14
# area = pi * radius ** 2
# formatted_string = 'the area of a circle with a radius {} is {:.2f}.'.format(radius, pi)

# print(formatted_string)

# city = 'lagos'
# temp = 31.4567
# humidity = 78

# result = 'City: {} | Temp: {:.2f}°C | Humidity: {}%'.format(city, temp, humidity)
# print(result)


# student = 'mubaraq'
# score = 87.6789
# total = 100

# rs_log = '{} scored {:.2f} out of {} which is {:.2f}%'.format(student, score, total, score/total * 100)
# print(rs_log)

# a = 15
# b = 4

# total = '{} + {} = {}'.format(a, b, a + b)
# print(total)

# minus = '{} - {} = {}'.format(a, b, a - b)
# print(minus)

# multiply = '{} * {} = {}'.format(a, b, a * b)
# print(multiply)

# divide = '{} / {} = {:.2f}'.format(a, b, a / b)
# print(divide)

# modulus = '{} % {} = {}'.format(a, b, a % b)
# print(modulus)

# floor_division = '{} // {} = {}'.format(a, b, a // b)
# print(floor_division)

# exponential = '{} ** {} = {}'.format(a, b, a ** b)
# print(exponential)


# string interpolation / f-strings (python 3.6+)

# a = 4
# b = 3
# print(f'{a} + {b} = {a + b}')
# print(f'{a} - {b} = {a - b}')
# print(f"{a} * {b} = {a * b}")
# print(f'{a} / {b} = {a / b:.2f}')
# print(f'{a} % {b} = {a % b}')
# print(f'{a} // {b} = {a // b}')
# print(f'{a} ** {b} = {a ** b}')


# # tasks

# name = 'mubaraq'
# age = 18
# city = 'lagos'
# stack = 'python'

# print(f'my name is {name}, i am {age} years old, i live in {city} and i code in {stack}')

# price = 1500.6789
# discount = 10 
# discount_amt = price * (discount / 100)
# final_price = price - discount_amt

# print(f'original price: ${price:.2f} | discout: {discount}% | final price: ${final_price:.2f}')

# first = 'python'
# second = 'programming'

# print(f"'{first}' has {len(first)} characters and '{second}' has {len(second)} characters. \n'{second}' is longer.")


# #tasks

# product = 'macbook pro'
# original_price = 2499.999
# tax_rate = 7.5
# tax_amt = tax_rate / 100 * original_price
# total = original_price + tax_amt

# print(f" Product: {product.capitalize()} | Price: ${original_price:.2f} | Tax: ${tax_amt:.2f} | Total: ${total:.2f}")


# # python strings as sequences of characters
# # In Python, a string is treated as a sequence of characters. That means each character has a position called an index.
 
# # unpacking characters

# language = 'python'
# a,b,c,d,e,f = language
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)

# accessing characters in strings by index

language = 'python'
# first_letter = language[0]
# print(first_letter)
# second_letter = language[1]
# print(second_letter)
# last_index = len(language) - 1
# print(last_index)
# last_letter = language[last_index]
# print(last_letter)

# counting backwards

# last_letter = language[-1]
# print(last_letter)
# second_last = language[-2]
# print(second_last)

# tasks, some are wromg

# word = 'developer'
# first_char = word[0]
# print(first_char)
# last_char = word[-1]
# print(last_char)
# # last_char_len = len(word) - 1 
# # print(last_char_len)  
# # fifth_character = word[4]
# # print(fifth_character)

# name = 'mubaraq'
# # last_three_char = name[(-1, -2)]
# # print(last_three_char)
# # first_three_names = name[{0,1,2}]
# # print(first_three_names)

# a,b,c,d,e,f,g = name
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)
# print(g)

# sentence = 'backend engineering'
# print(sentence[0])
# print(sentence[-1])
# print(sentence[8])
# print(len(sentence))
# print(len(word) - 1) 


# slicing

# language = 'python'
# first_three = language[0:3] # starts at zero index and up to 3 but not include 3
# print(first_three)
# last_three = language[3:6]
# print(last_three)

# # another way
# last_three = language[-3:]
# print(last_three)
# last_three = language[3:]
# print(last_three)

# # reversing a string

# greeting = 'hello, world!'
# print(greeting[::-1])

# skipping while slicing

# language = 'python'

# print(language[0:6:2])
# print(language[::2])
# print(language[::3])


# # tasks

# word = 'engineering'
# print(word[0:4])
# print(word[-4:])
# print(word[3:8])
# print(word[::-1])
# print(word[::2])

# # task 2

# full_name = 'mubaraq ayanleke'
# first_name = full_name[:7]
# print('first name:', first_name)
# last_name = full_name[8:]
# print('last name:', last_name )

# reversed = full_name[::-1]
# print('reversed:', reversed)

# initials = f'{full_name[0].upper()}.{full_name[8].upper()}'
# print(initials)

# # task 3

# sentence = 'backend development is my path'
# print(sentence[0:7])
# print(sentence[-4:])
# print(sentence[8:18])
# print(sentence[::-1])
# print(sentence[::3])


# string methods
# capitalize() - converts the first character of the string to capital letter

# challenge = 'thirty days of python'
# print(challenge.capitalize())

# # count() - counts how many times a character or substring appears

# challenge = 'thirty days of python'
# print(challenge.count('y'))
# print(challenge.count('y', 7, 14))
# print(challenge.count('th'))

# # endswith() - checks if a string ends with a specified ending
# challenge = '30 days of python'
# print(challenge.endswith('on'))
# print(challenge.endswith('tion'))

# # expandtabs() - replaces tab (\t) characters with spaces, tab(8 spaces)

# text = "hello\tworld"
# print(text.expandtabs(5))

# # find() - returns the index of the substring inside a string
 
# challenge = 'thirty days of python'
# print(challenge.find('y'))
# print(challenge.find('th'))

# # rfind() - returns the index of the last occurence of a substring, start from the back

# challenge = 'thirty days of python'
# print(challenge.find('y'))

# tasks

# sentence = 'you cannot end a sentence with because because because is a conjunction'
# index = sentence.find('because')
# last_index = sentence.rfind('because')
# index_conj = sentence.find('conjunction')
# print(index)
# print(last_index)
# print(index_conj)

# # task 2

# email = 'ayanleke.mubaraq@gmail.com'
# index_at = email.find('@')
# print(index_at)

# username_slice = email[:index_at]
# print(username_slice)

# domain = email[index_at + 1:]
# print(domain)

# index_dot = domain.find('.')
# print(index_dot)


# # task 3

# url = 'https://ayanleke.vercel.app'
# index_name = url.find('ayanleke')
# print(index_name)

# index_last = url.rfind('.')
# print(index_last)

# port_url = url.find('ayanleke.vercel.app')
# short_url = url[port_url:]
# print(short_url)


# # format() - formats string into nicer output

# first_name = 'mubaraq'
# last_name = 'ayanleke'
# age = 18
# job = 'software engineer'
# country = 'nigeria'
# sentence = 'i am {} {}. i am {} years old. i am {}. i live in {}'.format(first_name, last_name, age, job, country)

# print(sentence)

# radius = 10
# pi = 3.14

# area = pi * radius ** 2
# result = 'the area of a circle with radius {} is {}'.format(str(radius), str(area))
# print(result)

# # index() - is used to find the position of an item in a string, list, or tuple

# challenge = 'thirty days of python'
# sub_string = 'da'
# print(challenge.index(sub_string))
# # print(challenge.index(sub_string, 9))

# # rindex() - finds position from right to left (default 0 and string length - 1)

# challenge = 'thirty days of python'
# sub_string = 'da'
# print(challenge.rindex(sub_string))
# # print(challenge.rindex(sub_string, 9))
# print(challenge.rindex('on', 8))


# # isalnum() - checks alphanumeric characters

# challenge = 'thirtydayspython'
# print(challenge.isalnum())

# challenge = '30dayspython'
# print(challenge.isalnum())

# challenge = 'thirty days of python'
# print(challenge.isalnum()) # false because space is not an alphanumeric character

# challenge = 'thirty days of python 2019'
# print(challenge.isalnum())


# # isalpha() - checks is all string elements are alphabet characters

# challenge = 'thirty days of python'
# print(challenge.isalpha()) # space is excluded also

# challenge = 'thirtydayspython'
# print(challenge.isalpha())

# challenge = '123'
# print(challenge.isalpha())


# # isdecimal() - checks if all the characters in a string are decimal (0-9, floating numbers not included)

# challenge = 'thirty days of python'
# print(challenge.isdecimal())

# challenge = '221'
# print(challenge.isdecimal())

# challenge = '12 3'
# print(challenge.isdecimal()) # space excluded..


# # isdigit() - checks if all characters in a string are numbers and some other unicode characters for numbers

# challenge = 'thirty'
# print(challenge.isdigit())

# challenge = '30'
# print(challenge.isdigit())

# challenge = '\u00B2'
# print(challenge.isdigit())


# # isnumeric() - checks if all characters are numbers or number related

# num = '10'
# print(num.isnumeric())
# num = '\u00BD'
# print(num.isnumeric())
# num = '10.5'
# print(num.isnumeric())

# isidentifier() - checks for a valid identifier(used as a variable name in python)

# challenge = '30DaysOfPython'
# print(challenge.isidentifier())

# challenge = 'thirty_days_of_python'
# print(challenge.isidentifier())

# # islower() - checks if all alphabet characters in a string are lowercase

# challenge = 'thirty days of python'
# print(challenge.islower())

# challenge = 'thirty dAys of python'
# print(challenge.islower())

# # isupper() - checks if all alphabet characters in the string are uppercase

# challenge = 'thirty days of python'
# print(challenge.isupper())

# challenge = 'THIRTY DAYS OF PYTHON'
# print(challenge.isupper())


# join() - returns a concatenated string

# web_tech = ['html', 'css', 'javascript', 'react']
# result = ' '.join(web_tech)
# print(result)

# web_tech = ['html', 'css', 'javascript', 'react']
# result = '# '.join(web_tech)
# print(result)

# # strip() - removes all given characters starting from the beginning and end of the string

# challenge = 'thirty days of python'
# print(challenge.strip('noth'))

# # replace() - replace substring with a given string

# challenge = 'thirty days of python'
# print(challenge.replace('python', 'coding'))

# # split() - splits the string into a list

# challenge = 'thirty days of python'
# print(challenge.split())

# challenge = 'thirty, days, of, python'
# print(challenge.split(', '))

# # task 1

# date = '21-05-2026'
# parts = date.split('-')

# day = parts[0]
# month = parts[1]
# year = parts[2]
 
# print(day)
# print(month)
# print(year)

# # task 2

# full_name = 'Mubaraq Ayanleke' 
# name_parts = full_name.split(' ')
 

# print(name_parts)

# first_name = name_parts[0]
# print(first_name)

# last_name = name_parts[1]
# print(last_name)

# initials = (f'{first_name[0].upper()}.{last_name[0].upper()}')
# print(initials)

# # task 3

# csv_data = 'Lagos,Nigeria,Africa,Alakuko'
# split_data = csv_data.split(',')

# print(split_data)
# city = split_data[0]
# print('city:', city)

# country = split_data[1]
# print('country:', country)

# continent = split_data[2]
# print('continent:', continent)

# area = split_data[3]
# print('area:', area)


# # swapcase() - converts all uppercase characters to lowercase and all lowercase to lowercase

# challenge = 'Thirty Days Of Python'
# print(challenge.swapcase())

# challenge = 'thirty days of python'
# print(challenge.swapcase())


# # startswith() -  check if a string starts with the specified

# challenge = 'thirty days of python'
# print(challenge.startswith('thirty'))

# challenge = '30 days of python'
# print(challenge.startswith('thirty'))


# exercises

thirty = 'Thirty'
day = 'Days'
of = 'Of'
python = 'Python'
space = ' '

single_string = thirty + space + day + space + of + space + python
print(single_string)


coding = 'Coding'
for_str = 'For'
all = 'All'
space = ' '

concatenated_str = coding + space + for_str + space + all
print(concatenated_str)

company = concatenated_str
print(company)
print(len(company))
print(company.upper())
print(company.lower())

print(company.capitalize())
print(company.title())
print(company.swapcase())

print(company[0])
print(company.find('Coding'))

print(company.replace('Coding', 'Python'))

statement = 'Python for Everyone'
print(statement.replace('All', 'Everyone'))

statement = 'coding for all'
print(statement.split(' '))

companies = 'facebook, google, microsoft, apple, ibm, oracle, amazon'
print(companies.split(', '))

character = 'coding for all'
print(character[:6])
print(character.index('all'))
print('character:', character[10])

statement = 'python for all'
statement_first_part = statement[0]
statement_second_part = statement[1]
statement_third_part = statement[2]

statement_initials = (f'{statement_first_part.upper()}.{statement_second_part.upper()}.{statement_third_part.upper()}')
print(statement_initials)


statement_acronym = 'coding for all'

statement_part_1 = statement_acronym[0]
statement_part_2 = statement_acronym[1]
statement_part_3 = statement_acronym[2]

initials = (f'{statement_part_1.upper()}.{statement_part_2.upper()}.{statement_part_3.upper()}')
print(initials)

print(statement_acronym.index('c'))
print(statement_acronym.index('f'))
print(statement_acronym.rfind('l'))

sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))
print(sentence.rindex('because'))
phrase_slice = sentence.find('because because because')
print(sentence[phrase_slice:54])

stmt = 'Coding For All'
print(stmt.startswith('Coding'))
print(stmt.endswith('coding'))

stmt_2 = '   Coding For All      '
print(stmt_2.strip(' '))

character = '30DaysOfPython'
print(character.isidentifier())

second_character = 'thirty_days_of_python'
print(second_character.isidentifier()) # this obviously


libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result = '# '.join(libraries)

print(result)

sentences = 'I am enjoying this challenge. \nI just wonder what is next.'
print(sentences)

tab_escape = 'Name\tAge\tCountry\tCity\nAsabeneh 250\tFinland\tHelsinki'
print(tab_escape) # didn't put the tab before 250 because of an awkward spacing

radius = 10
area = 3.14 * radius ** 2
print(f'The area of a circle with radius {radius} is {area} meters square.')

a = 8
b = 6

print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')