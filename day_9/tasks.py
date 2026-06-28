# exercises

user_details = int(input('enter your age: '))
years = 18 - user_details

if user_details >= 18:
    print('you are old enough to drive.')
elif user_details < 18:
    print(f'ypu need {years} more years to drive.')
else:
    print('invalid age entered')

   

    