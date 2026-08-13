# Regular Expressions - RegEx
# regex is a pattern used to search for, match or validate specific text patterns in data.
# to use regex in python, we import the regex module which is re.

import re
# after importing the module, we can use it to detect or find patterns.

# methods in re module.

'''
    We use regex character sets and symbols to describe 
    the pattern we're looking for in a string.
'''

# re.match()   # → "Does it start here?"
# re.search()  # → "Is it anywhere?"
# re.findall() # → "Give me ALL matches. returns a list btw."
# re.split()   # → "Cut it at the matches."
# re.sub()     # → "Replace the matches."

# match.
# syntax - re.match(substring, string, re.I)

import re

txt = 'i love to teach python and javascript'
# returns an object with span, and match.

# re.I disables python case sensitive stuff.
match = re.match('i love to teach', txt, re.I)
print(match)

# span is the start and end positions of matched text in the string.
span = match.span()
print(span)

# find out the start and stop position from the span
start, end = span
print(start, end)

substring = txt[start:end]
print(substring)

# 1

txt = 'python is fun and python is powerful.'

match = re.match('python is fun', txt, re.I)
print(match)

span = match.span()
print(span)

start, end = span
print(start, end)

substring = txt[start:end]
print(substring)

# 2

txt = 'PYTHON is fun'

match = re.match('python', txt, re.I)
print(match)

span = match.span()
print(span)

start, end = span
print(start, end)

substring = txt[start:end]
print(substring)

# 3

txt = 'i love Python'

match = re.search('python', txt, re.I) # added ignore case, still didnt work.
print(match)

# 4

txt = 'Hello, my name is Mubaraq'

match = re.match('hello', txt, re.I)
print(match)

start, end = match.span()
print(start, end)

substring = txt[start:end]
print(substring)

# 5

txt = 'i am learning python'

match = re.match('i am learning', txt, re.I)
span = match.span()
start, end = span

substring = txt[start:end]


print(f'''
    match: {match}
    span: {span}
    start: {start}
    end: {end}
    substring: {substring}
''')

txt = 'i love Python and i also love javascript.'

search = re.search('python', txt, re.I)
print(search)

span = search.span()
print(span)

start, end = span
print(start, end)

substring = txt[start:end]
print(substring)

# search

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

match = re.search('first', txt, re.I)
print(match)

span = match.span()
print(span)

start, end = span
print(start, end)

substring = txt[start:end]
print(substring)


# findall() - returns all the matches as a list.

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

matches = re.findall('language', txt, re.I)
print(matches)

# since we are using both lowercase and uppercase letters

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

matches = re.findall('Python|python', txt)
print(matches)

# or

matches = re.findall('[Pp]ython', txt)
print(matches)


# replace a substring

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

match_replaced = re.sub('Python|python', 'Javascript', txt, flags=re.I)
print(match_replaced)

# or
match_replaced = re.sub('[Pp]ython', 'Javascript', txt, flags=re.I)
print(match_replaced)


txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing.
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs.
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

matches = re.sub('%', '', txt)
print(matches)


# splitting text using regex split

txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''

print(re.split('\n', txt))


# writing regex patterns

# to declare a string variable we use single or double quotes. to declare a regex variable r

regex_pattern = r'apple'
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
matches = re.findall(regex_pattern, txt)
print(matches)


# to make case insensitive adding flag
matches = re.findall(regex_pattern, txt, re.I)
print(matches)

# or we can use set of character method.

regex_pattern = r'[Aa]pple'  # means the first letter could be A or a
matches = re.findall(regex_pattern, txt)
print(matches)



# square bracket.

# looking for apple and banana.
regex_pattern = r'[Aa]pple | [Bb]anana'
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
matches = re.findall(regex_pattern, txt)
print(matches)


# escape character (\) in regex

regex_pattern = r'\d' # -> d is a special character which means digits.
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches)

# one or more times (+)

regex_pattern = r'\d+' # the + mean one or more times - it grabs the digits at once instead of one by one.
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches)

# period (.)

regex_pattern = r'[a].' # this square bracket means a, and the . means grab the character after it.
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)

# zero or more times (*)
# this pattern may not occur or occur many times.

regex_pattern = r'[a].*'
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)

# zero or one time (?)
# the pattern may not occur or it may occur once.

txt = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail.'''
regex_pattern = r'[Ee]-?mail' # ? means that '-' is optional
matches = re.findall(regex_pattern, txt)
print(matches)

# quantifier in regex.
# we can specify the length of the substring we are looking for in a text using curlyy bracket.

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{4}'
matches = re.findall(regex_pattern, txt)
print(matches)

# can accept multiple lengths
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{1,4}' # no spacing between them.
matches = re.findall(regex_pattern, txt)
print(matches)

# cart
# means the match must start at the beginning of the string.

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'^This'
matches = re.findall(regex_pattern, txt)
print(matches)

# negation
# means not this (pass the regex in the square bracket)

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'[^A-Za-z ]+'
matches = re.findall(regex_pattern, txt)
print(matches)