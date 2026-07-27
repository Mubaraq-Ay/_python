# generate a six-digit character.
import string
from random import choice, randint

def random_user_id():
    otp = string.ascii_letters + string.digits
    rand = ''

    for i in range(6):
         rand += choice(otp)
    return rand
       
print(random_user_id())

# random password.

def random_password():
     password = string.ascii_letters + string.digits
     random_pass = ''

     for i in range(8):
         random_pass += choice(password)
     return random_pass
print(random_password())

# just doing this to test smt
def pass_with_characters():
     password = string.ascii_letters + string.digits + string.punctuation
     rand = ''

     for i in range(12):
        rand += choice(password)
     return rand
print(pass_with_characters())

# 2
def coin_tosses():
    outcome = 'HT'
    rs = ''

    for i in range(10):
        rs += choice(outcome)
    return rs
print(coin_tosses())

# generate random plates.
def random_chars(pool, length):
    result = ''

    for i in range(length):
        result += choice(pool)

    return result

def random_plate():
    letters = random_chars(string.ascii_uppercase, 2)
    numbers = random_chars(string.digits, 3)
    last_letters = random_chars(string.ascii_uppercase, 2)

    return f'{letters}-{numbers}-{last_letters}'
print(random_plate())

# nigerian version
def rand_char(pool, length):
    result = ''

    for i in range(length):
        result += choice(pool)
    return result

def plates():
    letters = rand_char(string.ascii_uppercase, 3)
    numbers = rand_char(string.digits, 3)
    last_letters = rand_char(string.ascii_uppercase, 2)

    return f'{letters}-{numbers}-{last_letters}'
print(plates())


def user_id_gen_by_user():
    number_of_char = int(input('enter the number of chaacters you want: '))
    num_of_ids = int(input("how many id's do you want to generate?: "))
    rands = string.ascii_letters + string.digits

    for i in range(num_of_ids):
        result = ''
        for i in range(number_of_char):
         result += choice(rands)
        print(result)
user_id_gen_by_user()

# rgb color gen
def rgb_color_gen():
    return f"rgb({randint(0,255)},{randint(0,255)},{randint(0,255)})"

print(rgb_color_gen()) 