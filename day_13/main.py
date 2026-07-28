# list comprehension
# a list comprehension is a shorter way of writing a for loop when you want to create a new list.

# example 1
# changing a string to a list of characters.
# one way

language = 'python'
lst = list(language)
print(type(lst))
print(lst)

# second way - using list comprehension.
lst = [i for i in language]
print(type(lst))
print(lst)

# example 2
# generating a list of numbers

numbers = [i for i in range(11)]
print(numbers)

# it is possible to do mathematical operations during iteration
squares = [i * i for i in range(11)]
print(squares)

# it is also possible to make a list of tuples.
numbers = [(i, i * i) for i in range(11)]
print(numbers)

# list comprehension can br combined with if expression.
# generating even numbers

even_numbers = [i for i in range(21) if i % 2 == 0]
print(even_numbers)

# generating odd numbers
odd_numbers = [i for i in range(21) if i % 2 != 0]
print(odd_numbers)

# filter numbers: let's filter out positive even numbers from the list below
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = [i for i in numbers if i % 2 == 0 and i > 0]
print(positive_even_numbers)

# flattening a two dimensional array.
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [number for row in list_of_lists for number in row]
print(flattened_list)