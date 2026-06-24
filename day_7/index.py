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