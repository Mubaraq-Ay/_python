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