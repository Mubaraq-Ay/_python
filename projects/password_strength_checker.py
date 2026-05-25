password = input('Enter your password: ')
characters = len(password)
password_length = characters > 8
password_number = '0' in password or '1' in password or '2' in password or '3' in password or '4' in password or '5' in password or '6' in password or '7' in password or '8' in password or '9' in password
password_rating = password_length and password_number

print('=========================')
print('\tPASSWORD')
print('=========================')
print(f'Characters: {characters}')
print(f'Is your password longer than 8 charaters: {password_length}')
print(f'Does your password contains any number: {password_number}')
print(f'Password rating: {password_rating}')

# messy, but will soon learn cleaner ways