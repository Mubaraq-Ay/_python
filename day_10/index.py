# loops are used to execute a block of code repeatedly instead of writing same code over and over.
# python has two main loops.
# for loop and while loop.

# while loop
# this is used to execute a block of statements repeatedly until a given condition is satisfied.

count = 0

while count < 5:
    print(count)
    count = count + 1


# while else
# A while...else statement is a loop where the else block executes only if the while loop finishes normally (without a break).

count = 0

while count < 5:
    print(count)
    count += 1
else:
    print(count)

# mini tasks
# 1

number = 1

while number < 11:
    print(number)
    number += 1
else:
    print('counting done!')

# 2

count_down = 10

while count_down > 0:
    print(count_down)
    count_down -= 1
else:
    print('liftoff! 🚀')

# 3

num = 0

while num <= 30:
    print(num)
    num += 3
else:
    print('reached 30!')


# break and continue - part 1
# we use break when we'd like to get out or stop the loop.

count = 0

while count < 5:
    print(count)
    count += 1
    if count == 3:
        break

# continue - we can skip the current iteration and continue with the next.

count = 0

while count < 5:
    if count == 3:
        count += 1
        continue
    print(count)
    count += 1


# mini tasks

# 1

numbers = 0

while numbers <= 20:
    print(numbers)
    numbers += 1
    if numbers == 14:
        break


# 2

numbers = 1
 
while numbers <= 10:
       if numbers % 2 == 0:
        numbers += 1
        continue
       
       print(numbers)
       numbers += 1
        
        