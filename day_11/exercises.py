def add_two_numbers(a, b):
    total = a + b
    return total
print(add_two_numbers(3, 1))

# write a function that calculates the area of a circle.
def area_of_circle(pi, r):
    area = pi * r ** 2
    return(area)
print(area_of_circle(3.142, 3))

def add_all_nums(*nums):
    for num in nums:
        if not isinstance(num, (int, float)):
            return 'All arguments must be numbers..'
        
    return sum(nums)
print(add_all_nums(1,2,4,'ld'))

def convert_celcius_to_fahrenheit(c):
    conversion = str((c * 9/5) + 32) + ' °F'
    return conversion
print(convert_celcius_to_fahrenheit(3))