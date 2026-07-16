# level 1
# 1

# iterate 0 - 10 using for loop
for number in range(11):
    print(number)

# iterate 0 - 10 using while loop
number = 0
while number <= 10:
    print(number)
    number += 1

# 2

# iterate 10 - 0 using for loop.
for number in range(10, -1, -1):
    print(number)

# iterate 10 - 0 using while loop.

number = 10
while number <= 0:
    print(number)
    number -= 1

# 3

count = 0

for triangle in range(7):
    count += 1
    print('#' * count)

# shorter version
for triangle in range(8, 1):
    print('#' * triangle)

# 4
# nested loops.

for row in range(8):
    for column in range(8):
     print('#', end=' ')
    print()
   

# 5.

for numbers in range(11):
    print(f'{numbers} x {numbers} = {numbers ** 2}')

# 6.

languages = ['Python', 'Numpy','Pandas','Django', 'Flask']

for language in languages:
    print(language)

# 7. 

# print only even numbers from 0 -100
for numbers in range(101):
    if numbers % 2 == 0:
        print(numbers)

# 8

# print only odd numbers from 0 - 100
for numbers in range(101):
    if numbers % 2 == 1:
        print(numbers)


# level 2

# 1

# sum of 0 - 100, using for loop.
# for numbers in range(101):
#     print(numbers)

# 



