# while loop

count = 0

while count < 5:
    print(count)
    count += 1

# 1

numbers = 1

while numbers <= 20:
    print(numbers)
    numbers += 1

# 2

countdown = 15

while countdown >= 1:
    print(countdown)
    countdown -= 1
else:
    print('Blast off! 🚀')

# print 1 - 10

numbs = 1

while numbs <= 10:
    print(numbs)
    numbs += 1

# print from 10 -1

reverse_countdown = 15

while reverse_countdown >= 1:
    print(reverse_countdown)
    reverse_countdown -= 1


# numbers 2 -20

numbers = 2

while numbers <= 20:
    print(numbers)
    numbers += 1

# while...else


count = 0
while count < 5:
    print(count)
    count += 1
else:
    print('ok')

# tasks

numbers = 1

while numbers <= 10:
    print(numbers)
    numbers += 1
else:
    print('finished counting!')

# 2

numbers = 2

while numbers <= 20:
    print(numbers)
    numbers += 2

else:
    print('done')

# count down

countdown = 10

while countdown >= 1:
    print(countdown)
    countdown -= 1
else:
    print('blast off!')


# multiples of 3

multiples = 3

while multiples <= 30:
    print(multiples)
    multiples += 3
else:
    print('finished')

# square of numbers

squares = 1

while squares <= 5:
    print(squares ** 2)
    squares += 1
else:
    print('done')


# sum of numbers
total = 0
numbers = 1

while numbers <= 10:
    total += numbers
    numbers += 1
    print(total)
else:
    print('calculation complete')

# countdown loop

countdown = int(input('enter a number: '))

while countdown >= 1:
    print(countdown)
    countdown -= 1
else:
    print('done')


# skip counting

count = 5

while count <= 30:
    print(count)
    count += 5
else:
    print('finished')



# asking a number

numbers = 0

while numbers >= 0:
    numbers = int(input('enter a number: '))
    if numbers >= 0:
     print(numbers)
else:
    print('negative number entered, stopping')