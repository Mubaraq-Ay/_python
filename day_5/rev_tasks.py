fruits = ['mango', 'banana', 'apple', 'orange', 'grape']

first_fruit = fruits[0]
print(first_fruit)

first_three = fruits[0:3]
print(first_three)


last_fruit = fruits[-1]
print(last_fruit)

fruits.append('kiwi')
print(fruits)

fruits.sort()
print(fruits)

reversed_list = fruits[::-1]
print(reversed_list)

if_exists = 'apple' in fruits
print(if_exists)

index_of = fruits.index('apple')
print(index_of)

fruits.remove('banana')

print(fruits)

