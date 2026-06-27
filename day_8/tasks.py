# exercises


dog = {}

dog['name'] = 'ekuke'
dog['color'] = 'brown'
dog['breed'] = 'local dog'
dog['legs'] = 4
dog['age'] = 3

print(dog)


student = {
    'first_name': 'mubaraq',
    'last_name': 'ayanleke',
    'gender': 'male',
    'age': 18,
    'marital_status': 'single',
    'skills': ['critical thinking', 'problem solving', 'backend engineering'],
    'country': 'nigeria',
    'city': 'lagos',
    'address': 'califonia'
}

print(len(student))

skills = student['skills']
print(skills)
print(type(skills))

student['skills'].append('php')
student['skills'].append('aws')
print(skills)

keys = list(student.keys())
print(keys)

values = list(student.values())
print(values)

student_list = student.items()
print(student_list)

student.pop('age')
print(student)

del student
