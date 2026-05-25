full_name = input('Enter your full name: ')
name_parts = full_name.split()

first_name = name_parts[0]
last_name = name_parts[1]

initials = (f'{first_name[0].upper()}.{last_name[0].upper()}')
clean_name = full_name.replace(' ', '')
characters = len(clean_name)
 

print('===========================')
print('\tNAME CARD')
print('===========================')
print(f'Full Name:  {full_name}')
print(f'First Name: {first_name}')
print(f'Last Name:  {last_name}')
print(f'Initials:   {initials}')
print(f'Characters: {characters}')
print('============================')