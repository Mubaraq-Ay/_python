# # while loop

# count = 0

# while count < 5:
#     print(count)
#     count += 1

# # 1

# numbers = 1

# while numbers <= 20:
#     print(numbers)
#     numbers += 1

# # 2

# countdown = 15

# while countdown >= 1:
#     print(countdown)
#     countdown -= 1
# else:
#     print('Blast off! 🚀')

# # print 1 - 10

# numbs = 1

# while numbs <= 10:
#     print(numbs)
#     numbs += 1

# # print from 10 -1

# reverse_countdown = 15

# while reverse_countdown >= 1:
#     print(reverse_countdown)
#     reverse_countdown -= 1


# # numbers 2 -20

# numbers = 2

# while numbers <= 20:
#     print(numbers)
#     numbers += 1

# # while...else


# count = 0
# while count < 5:
#     print(count)
#     count += 1
# else:
#     print('ok')

# # tasks

# numbers = 1

# while numbers <= 10:
#     print(numbers)
#     numbers += 1
# else:
#     print('finished counting!')

# # 2

# numbers = 2

# while numbers <= 20:
#     print(numbers)
#     numbers += 2

# else:
#     print('done')

# # count down

# countdown = 10

# while countdown >= 1:
#     print(countdown)
#     countdown -= 1
# else:
#     print('blast off!')


# # multiples of 3

# multiples = 3

# while multiples <= 30:
#     print(multiples)
#     multiples += 3
# else:
#     print('finished')

# # square of numbers

# squares = 1

# while squares <= 5:
#     print(squares ** 2)
#     squares += 1
# else:
#     print('done')


# # sum of numbers
# total = 0
# numbers = 1

# while numbers <= 10:
#     total += numbers
#     numbers += 1
#     print(total)
# else:
#     print('calculation complete')

# # countdown loop

# countdown = int(input('enter a number: '))

# while countdown >= 1:
#     print(countdown)
#     countdown -= 1
# else:
#     print('done')


# # skip counting

# count = 5

# while count <= 30:
#     print(count)
#     count += 5
# else:
#     print('finished')



# # asking a number

# numbers = 0

# while numbers >= 0:
#     numbers = int(input('enter a number: '))
#     if numbers >= 0:
#      print(numbers)
# else:
#     print('negative number entered, stopping')


# break

# count = 0

# while count < 5:
#     print(count)
#     count += 1
#     if count == 3:
#         break

# break tasks

# numbers = 1

# while numbers <= 10:
#     print(numbers)
#     numbers += 1
#     if numbers == 7:
#         break

# task 2

# numbers = 1

# while numbers <= 10:
#     print(numbers)
#     numbers += 1


#     if numbers > 5 and numbers % 2 == 0: 
#         print(numbers)
#         break

# multiples of 5

# multiples = 5

# while multiples <= 25:
#     print(multiples)
#     multiples += 5

# # countdown from 10

# countdown = 10

# while countdown >= 1:
#     print(countdown)
#     countdown -= 1

#     if countdown == 4:
#         break

# user guess

# number = 8

# while True:
#     user_number = int(input('guess the number: '))
#     if user_number != number:
#         print('wrong')
#     else:
#         print('correct')
#         break


# password 

# correct_password = 'python'

# while True:
#     password = input('enter the password: ')
#     if password == correct_password:
#         print('access granted')

#         break
#     print('access denied')

# keep adding

# total = 0

# while True:
#     number = int(input('enter number: '))
#     total = number + total # i wrote this but cant really explain this line
#     if number == 0:
#         print(f'total = {total}')
#         break

# count attempts

# attempts = 0
# secret_number = 9

# while True:
#     user_input = int(input('guess number: '))
#     attempts += 1
#     if user_input == 9:
#         print('correct!')
#         print(f'Attempts: {attempts}')
#         break

#     print('wrong')

    # task 9 - 1,2,3,4
    # task 10 - 1,2,3,4,6
    
# count = 0

# while count < 4:
#     print(count)
#     count += 1
#     break
# else:
#     print("Finished")


# continue

count = 0

while count < 5:
    if count == 3:
        count += 1
        continue
    print(count)
    count += 1


# task 1

numbers = 1

while numbers <= 10:
    if numbers == 5:
        numbers += 1
        continue
    print(numbers)
    numbers += 1

# 2

numbers = 1

while numbers <= 10:
    if numbers % 2 == 0:
        numbers += 1
        continue
    print(numbers)
    numbers += 1

# 3
# skip the multiples of 3

multiples = 1

while multiples <= 15:
    if multiples % 3 == 0:
        multiples += 1
        continue
    print(multiples)
    multiples += 1

# 4
# skip a range.

# numbers = 1

# while numbers <= 10:
#     if 4 <= numbers <= 6:
#         numbers += 1
#         continue
#     print(numbers)
#     numbers += 1

# # countdown 

# countdown = 10

# while countdown >= 1:
#     if countdown == 7:
#         countdown -= 1
#         continue
#     print(countdown)
#     countdown -= 1

# # user input


# while True:
#     user_input = int(input('enter number: '))
#     if user_input == 0:
#         break
#     if user_input > 0:
#         print(f'you entered: {user_input}')
        


# # # password.

# correct_password = 'python'

# while True:
#     password = input('enter password: ')
#     if password == '':
#         continue
#     if password != correct_password:
#         print('wrong password.')
#     else:
#         print('welcome')
#         break


# guessing game

# secret_number = 8

# while True:
#     user_input = int(input('enter number: '))
#     if user_input < 1 or user_input > 10:
#      print('please enter a number between one and 10')
#      continue
#     if user_input == secret_number:
#         print('correct')
#         break
#     else:
#         print('wrong try again')
         

# for loops


numbers = [0, 1, 2, 3, 4, 5]
for number in numbers:
    print(number)


# tasks.

fruits = ["Apple", "Banana", "Orange"]

for fruit in fruits:
    print(fruit)


# 2

names = ["Ali", "Aisha", "Mubaraq", "Yusuf"]

for name in names:
    print(f'hello, {name}')

# 3

numbers = [2, 4, 6, 8, 10]

for number in numbers:
    print(number ** 2)

# 4

# using for loop on list

words = ["python", "fastapi", "docker"]

for word in words:
    print(word.upper())

# using for loop on string.

language = 'Python'
for letter in language:
    print(letter)

for i in range(len(language)):
    print(i, language[i])


# using for loop on tuple

numbers = (1, 2, 3, 4, 5)
for number in numbers:
    print(number)

