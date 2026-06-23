empty_tuple = ()

brothers = ('wale', 'kunle', 'mubby', 'ola')
sisters = ('sade', 'fola', 'kemi', 'ade')

siblings = brothers + sisters
print(siblings)

print(len(siblings))

# modify the siblings tuple

siblings = list(siblings)
siblings[0] = 'dami'
siblings[1] = 'laide'

family_members = siblings
print(family_members)

family_members = tuple(family_members)
print(family_members)

