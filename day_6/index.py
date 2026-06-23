# tuples
# tuple is a collection of different data types which is ordered and immutable.

fruits = ('banana', 'orange', 'mango', 'lemon')

first_fruit = fruits[0]
second_fruit = fruits[1]

last_index = len(fruits) - 1
last_fruits = fruits[last_index]

print(last_fruits)

# negative indexing

fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[-4]
second_fruit = fruits[-3]
last_fruits = fruits[-1]

# slicing tuples

all_fruits = fruits[0:]
print(all_fruits)

orange_mango = fruits[1:3]
print(orange_mango)

orange_to_the_rest = fruits[1:]
print(orange_to_the_rest)


# range of negative indexes

all_fruits = fruits[-4:]
print(all_fruits)

orange_mango = fruits[-3:-1]
print(orange_mango)

orange_to_the_rest = fruits[-3:]
print(orange_to_the_rest)


# changing tuples to list

fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)

fruits[0] = 'apple'
print(fruits)

fruits = tuple(fruits)
print(fruits)

# checking an item in a tuple

fruits = ('banana', 'orange', 'mango', 'lemon')

print('orange' in fruits)
print('apple' in fruits)


# joining tuples
# we can join 2 or more tuples using the + operator.

fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')

fruit_and_vegetables = fruits + vegetables
print(fruit_and_vegetables)


# deleting tuples
# it is not possible to remove a single item in a tuple, but we can use del to delete the entire tuple


fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits

print(fruits)