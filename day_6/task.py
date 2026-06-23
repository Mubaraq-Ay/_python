empty_tuple = ()

brothers = ('wale', 'kunle', 'mubby', 'ola')
sisters = ('sade', 'fola', 'kemi', 'ade')

siblings = brothers + sisters
print(siblings)

print(len(siblings))

# modify the siblings tuple

siblings = list(siblings)
father = 'dami'
mother = 'laide'

family_members = siblings + [father, mother]
family_members = tuple(family_members)
print(family_members)


# level 2

# unpack siblings and parents

*siblings, father, mother = family_members

parents = (father, mother)
print(siblings)
print(parents)


fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
animal_products = ('milk', 'egg', 'ponmo', 'meat', 'fish')

food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

