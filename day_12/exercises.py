# generate a six-digit character.
import string
from random import choice

def random_user_id():
    otp = string.ascii_letters + string.digits
    rand = ''

    for i in range(6):
         rand += choice(otp)
    return rand
       
print(random_user_id())

