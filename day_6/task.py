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

# find the middle item

middle_index = len(food_stuff_tp) // 2
print(middle_index)

middle_items = food_stuff_tp[middle_index - 1 : middle_index + 1]
print(middle_items)

# slice out the first 3 items

first_three_items = food_stuff_lt[0:3]
print(first_three_items)

last_three_items = food_stuff_lt[-3:]
print(last_three_items)

# delete food tuple

del food_stuff_tp
# print(food_stuff_tp)

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

check_estonia = 'Estonia' in nordic_countries
print(check_estonia)

check_iceland = 'Iceland' in nordic_countries
print(check_iceland)