# it  is best to define variables in the smallest scope they will be needed in.
egg_count = 0
# it is global variable


def buy_eggs2():
    # we can access the global variable in local scope
    return egg_count+12


def buy_eggs():
    # we cannot change global variable in local scope
    # function assumes the egg_count being referred to is the global variable.
    egg_count += 12 # purchase a dozen eggs


#  If we try to change or reassign this global variable, however, as we do in this code, we get an error.
#  Python doesn't allow functions to modify variables that aren't in the function's scope.
print(buy_eggs2())

def one():
    """function to test variable scopes

    INPUT:

    OUTPUT:
    None: default output of any function"""
    # here new local variable is created, we are not referencing global variable, it is still 0
    egg_count = 21
    print(egg_count)


one()
print(egg_count)
print(one())


# lambda expression

# lambda_function_name = lambda arguments: expression_that_is_evaluated_and_returned

# You can use lambda expressions to create anonymous functions. That is, functions that don’t have a name.
# They are helpful for creating quick functions that aren’t needed later in your code.
# This can be especially useful for higher order functions, or functions that take in other functions as arguments.

miltiple = lambda x, y: (x*y) ** 2
print(miltiple(2, 3))

# map and filters are high order function which take function as argument and iterable

numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]
# map() is a higher-order built-in function that takes a function and iterable as inputs,
# and returns an iterator that applies the function to each element of the iterable.

average = lambda ls: sum(ls) / len(ls)
print(list(map(average, numbers)))

# filter() is a higher-order built-in function that takes a function and iterable as inputs and
# returns an iterator with the elements from the iterable for which the function returns True.
cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]
word_count = lambda st: len(st) < 10
print(list(filter(word_count, cities)))



# Iterables are objects that can return one of their elements at a time, such as a list.
# Many of the built-in functions we’ve used so far, like 'enumerate,' return an iterator.
# An iterator is an object that represents a stream of data.
# This is different from a list, which is also an iterable, but not an iterator because it is not a stream of data.

# Generators are a simple way to create iterators using functions.
# You can also define iterators using classes, which you can read more about here.

# if yeild is there in function expression, then it is generator

# Generator Expressions

# Here's a cool concept that combines generators and list comprehensions!
# You can actually create a generator in the same way you'd normally write a list comprehension,
# except with parentheses instead of square brackets. For example:

sq_list = [x**2 for x in range(10)]  # this produces a list of squares

sq_iterator = (x**2 for x in range(10))  # this produces an iterator of squares

menu = {"ok":"This", "okt":"That"}
inp = "Ok"
if inp.upper() in (name.upper() for name in menu.keys()):
    print ("found")

print(menu["Ok"])


