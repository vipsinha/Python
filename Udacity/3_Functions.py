'''
Quiz: Population Density Function
Write a function named population_density that takes two arguments, 
population and land_area, and returns a population density calculated 
from those values. I've included two test cases that you can use to 
verify that your function works correctly. Once you've written your 
function, use the Test Run button to test your code.
'''
# write your function here
def population_density(population,land_area):
    pop_den = population/land_area
    return pop_den



# test cases for your function
test1 = population_density(10, 1)
expected_result1 = 10
print("expected result: {}, actual result: {}".format(expected_result1, test1))

test2 = population_density(864816, 121.4)
expected_result2 = 7123.6902801
print("expected result: {}, actual result: {}".format(expected_result2, test2))

'''
Notice that we can still access the value of the global variable 
word within this function. However, the value of a global variable 
can not be modified inside the function. If you want to modify that 
variable's value inside this function, it should be passed in as an argument.
'''
# This works fine
word = "hello"

def some_function():
    print(word)

some_function()

"""
ambda Expressions
You can use lambda expressions to create anonymous functions. 
That is, functions that don’t have a name. They are helpful for 
creating quick functions that aren’t needed later in your code. 
This can be especially useful for higher order functions, or functions 
that take in other functions as arguments.

With a lambda expression, this function:
"""
def multiply(x, y):
    return x * y
'''
can be reduced to:
'''
multiply = lambda x, y: x * y

'''
Quiz: Lambda with Map
map() is a higher-order built-in function that takes a function and iterable as inputs, and returns an iterator that applies the function to each element of the iterable. The code below uses map() to find the mean of each list in numbers to create the list averages. Give it a test run to see what happens.

Rewrite this code to be more concise by replacing the mean function with a lambda expression defined within the call to map().
'''
numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]
'''
def mean(num_list):
    return sum(num_list) / len(num_list)
'''
mean = lambda num_list: sum(num_list) / len(num_list)

averages = list(map(mean, numbers))
print(averages)