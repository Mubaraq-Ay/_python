# conditionals

# if condition

# the keyword if is used to check if a condition is true and to execute the block code.

a = 3
if a > 0:
    print('A is a positive number')

# if Else
# if the condition is true, the first block will be executed, if not the else condition will run

a = 3
if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')   

# if Elif else

# we use elif when we have multiple conditions

a = 0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('a is zero')


# short hand

a = 3
print('A is positive') if a > 0 else print('A is negative')


# nested conditions

a = 3
if a > 0:
    if a % 2 == 0:
        print('a is a positive and even integer')
    else:
        print('a is a positive number')
elif a == 0:
    print('a is zero')
else:
    print('a is a negative number')

# we can avoid nested condition by using logical operator and.

# if condition and logical operators

a = 0
if a > 0 and a % 2 == 0:
    print('a is an even and positive integer')
elif a > 0:
    print('a is a positive integer')
elif a == 0:
    print('a is zero')
else:
    print('a is negative')


# if and or logical operators

user = 'james'
access_level = 3
if user == 'admin' or access_level >= 4:
    print('access granted!')
else: 
    print('access denied!')