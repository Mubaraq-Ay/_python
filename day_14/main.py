# higher order functions
# functions are not just things that run code. they're values like number or string , we can pass them around, store them and hand them to other functions.

# A function can take one or more functions as parameters
# A function can be returned as a result of another function
# A function can be modified
# A function can be assigned to a variable

# function as a parameter.

def sum_numbers(nums):  # normal function
    return sum(nums)    # a sad function abusing the built-in sum function :<

def highest_order_function(f, lst):
    summation = f(lst)
    return summation
result = highest_order_function(sum_numbers, [1,2,3,4,5])
print(result)

def greet(): # a normal function.
    print('hello')

def run(func):
    func()

run(greet)

# function as a return value
