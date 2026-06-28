# exercises

# user_details = int(input('enter your age: '))
# years = 18 - user_details

# if user_details >= 18:
#     print('you are old enough to drive.')
# elif user_details < 18:
#     print(f'ypu need {years} more years to drive.')
# else:
#     print('invalid age entered')

   

# my_age = 18
# your_age = int(input('enter your age: '))
# age_gap = your_age - my_age

# if your_age > my_age:
#     print(f'you are {age_gap} years older than me')
# elif my_age == your_age:
#     print('we are age mates g.')
# else:
#     print(f'you are {abs(age_gap)} years younger than me') 


# 3

# a = int(input('enter a number: '))
# b = int(input('enter a number: '))

# if a > b:
#     print('a is greater than b')
# elif a < b:
#     print('a is smaller than b')
# else:
#     print('a is equal to b')


# level 2

# students grading

# scores = int(input('enter your score: '))

# if scores >= 90:
#     print('a')
# elif scores >= 80:
#     print('b')
# elif scores >= 70:
#     print('c')
# elif scores >= 60:
#     print('d')
# elif scores >= 0:
#     print('f')
# else:
#     print('score not found!')


# season checker
# season_input = input('Enter a month to know what season it is: ').lower()
# winter_months = ['december','january', 'february']
# autumn_months = ['september', 'october', 'november']
# summer_months = ['june', 'july', 'august']
# spring_months = ['march', 'april', 'may']

# if season_input in winter_months:
#     print('Winter')
# elif season_input in autumn_months:
#     print('Autumn')
# elif season_input in summer_months:
#     print('Summer')
# elif season_input in spring_months:
#     print('Spring')
# else:
#     print('enter a valid month!')



# fruits = ['banana', 'orange', 'mango', 'lemon']

# add_fruit = input('enter a fruit: ').lower()

# if add_fruit in fruits:
#     print('That fruit already exist in the list')
# else:
#     fruits.append(add_fruit)
#     print(f'added! updated list {fruits}')


# level 3

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

if 'skills' in person:
    skills = (person['skills']) 
    mid = len('skills') // 2
    print(skills[mid])

if 'skills' in person:
    if 'Python' in person['skills']:
        print('this person knows python')
    else:
        print('this person does not know python')



skills = person['skills']

if 'JavaScript' in skills and 'React' in skills and len(skills) == 2:
    print("He is a front end developer")

elif 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
    print("He is a backend developer")

elif 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
    print("He is a fullstack developer")

else:
    print("unknown title")

if person['is_married'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")