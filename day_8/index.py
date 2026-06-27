# dictionary

# a dictionary is a collection of unordered, modifiable(mutable) paired (key:value) data type.

person = {
    'first_name': 'mubaraq',
    'last_name': 'ayanleke',
    'age': 18,
    'country': 'nigeria',
    'is_married': True,
    'skills': ['python', 'linux', 'mongodb', 'node', 'aws'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# dictionary length

print(len(person))

# accessing dictionary items

# we can access dictionary items by referring its key name

print(person['first_name'])
print(person['age'])
print(person['skills'][0])
print(person['address']['street'])
# print(person['city'])

# Accessing an item by key name raises an error if the key does not exist. 
# To avoid this error first we have to check if a key exist or we can use the get method. 
# The get method returns None, which is a NoneType object data type, if the key does not exist.

print(person.get('first_name'))
print(person.get('skills'))
print(person.get('skills')[0])
print(person.get('city')) # returns none


# adding items to a dictionary

person = {
    'first_name': 'mubaraq',
    'last_name': 'ayanleke',
    'age': 18,
    'country': 'nigeria',
    'is_married': True,
    'skills': ['python', 'linux', 'mongodb', 'node', 'aws'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

person['job_title'] = 'software engineer'
person['skills'].append('devops')

print(person)


# modifying items in a dictionary

person = {
    'first_name': 'mubaraq',
    'last_name': 'ayanleke',
    'age': 18,
    'country': 'nigeria',
    'is_married': True,
    'skills': ['python', 'linux', 'mongodb', 'node', 'aws'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

person['first_name'] = 'Ayoub'
person['age'] = 334

print(person)


