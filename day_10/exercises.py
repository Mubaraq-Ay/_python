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
    
