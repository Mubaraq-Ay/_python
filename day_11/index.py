# functions.

# A function is a reusable block of code that performs a specific task and can be called whenever it is needed.
# we use def keyword.

# function without parameters.
# function can be declared without parameters.

def generate_full_name():
    first_name = 'mubaraq'
    last_name = 'ayanleke'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
generate_full_name() # calling a function

def add_two_numbers():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)
add_two_numbers()


# function returning a value - part 1

# function return values using the return statement. 
# if a function has no return statement, it returns None.

def generate_full_name():
    first_name = 'mubaraq'
    last_name = 'ayanleke'
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name())


# tasks

def say_hello():
    say_hello = 'hello!'
    print(say_hello)
say_hello()

# 2

def school_name():
    school_name ='oui'
    print(school_name)
school_name()


# 3

def favorite_language():
    fav_language = 'python'
    return fav_language
print(favorite_language())

# 4

def favorite_number():
    favorite_number = 1
    return favorite_number
print(favorite_number())

# 5

def multiply():
    nums = 7 * 9
    return nums
print(multiply())


# 6

 