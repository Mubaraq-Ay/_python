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

def check_season(month):
   autumn_months = ['january', 'february', 'march']
   winter_months = ['april', 'may', 'june']
   spring_months = ['july', 'august', 'september']
   summer_months = ['october', 'november', 'december']
   month = month.lower()
   if month in autumn_months:
       return 'autumn'
   elif month in winter_months:
       return 'winter'
   elif month in spring_months:
       return 'spring'
   elif month in summer_months:
       return 'summer'
   
print(check_season('March'))

# calculate slope
def calculate_slope(y2, y1, x2, x1):
    m = (y2 - y1) / (x2 - x1)
    return m
print(calculate_slope(2, 3, 4, 5))

# solve quadratic equation
def solve_quadratic_eqn(a, b, c):
      discriminant = (b ** 2 - 4 * a * c)** 0.5 
      x1 = (-b + discriminant) /  (2 * a)
      x2 = (-b - discriminant) / (2 * a)
      return x1, x2
print(solve_quadratic_eqn(1,-5,6))

def print_list(my_list):
    for i in my_list:
        print(i)

my_list = ['bmw', 'porsche', 'mercedes', 'toyota']
print_list(my_list)

# reverse list

def reverse_list(my_array):
    for i in my_array:
        print(i)
    
reverse_list(reversed([1,2,4,5,6,7]))

# capitalize list items.
def capitalize_list_items(my_list):
    new_list = []
    for i in my_list:
        new_list.append(i.capitalize())
    return new_list

print(capitalize_list_items(['man', 'man']))


def add_item(my_list,item):
    my_list.append(item)
    return my_list
print(add_item([1], 't'))
