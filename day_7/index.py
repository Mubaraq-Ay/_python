# sets

# set is a collection of unordered and un-indexed distinct elements

fruits = {'banana', 'orange', 'mango', 'lemon'}

# finding length of a set

print(len(fruits))

# accessing items in a set
fruits = {'banana', 'orange', 'mango', 'lemon'}
print('does mango exist in fruits?', 'mango' in fruits)

# adding items to a set, we use add()

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.add('lime')

print(fruits)

# we add multiple items using update()

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')

fruits.update(vegetables)
print(fruits)

# removing items from set.
# we can use remove(), discard(), and pop(), but pop() removes a random item

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.remove('banana')

print(fruits)
fruits.discard('mango')

print(fruits)

fruits.pop()
print(fruits)

# to know the removed item
fruits = {'banana', 'orange', 'mango', 'lemon'}
removed_item = fruits.pop() 

print(removed_item)

# clearing items in a set
# we use clear()

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear()

print(fruits)

# deleting a set

fruits = {'banana', 'orange', 'mango', 'lemon'}
del fruits

# print(fruits)

# converting list to set

fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
fruits = set(fruits)

print(fruits)


# joining set
# we use union

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
print(fruits.union(vegetables))
# or
print(fruits | vegetables)

# finding intersection items
# Intersection returns a set of items which are in both the sets or using & symbol. 

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}

intercept = whole_numbers.intersection(even_numbers)

print(intercept)

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}

print(python.intersection(dragon))

# checking subset and superset
# A set can be a subset or super set of other sets:

# Subset: issubset()
# Super set: issuperset

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}

print(whole_numbers.issuperset(even_numbers))
print(whole_numbers.issubset(even_numbers))

print(even_numbers.issubset(whole_numbers))
print(even_numbers.issuperset(whole_numbers))

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}

print(python.issuperset(dragon))
print(python.issubset(dragon))

print(dragon.issubset(python))


# checking the difference between two sets
# we can use the minus symbol (-)

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}

print(whole_numbers.difference(even_numbers))

python = {'p', 'y', 't', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}

print(python.difference(dragon))
print(dragon.difference(python))

# print(dragon - python)

# difference_update(), this modifies the set directly

A = {1, 2, 3, 4, 5, 7}
B = {3, 4, 6, 7, 8}

A.difference_update(B)

print(A)   
print(B)  



