
print("Hi")

# ** gives exponentiation
# // Divides and run down to the nearest integer
# for

print("Exponentiation 3**2 :", 3**2)
print("Divides and rounds down 7//3 :", 7//3)
print("Boolean :", 34 < 45)
age = 14
is_teen = age < 20 and age > 12
print("is teen:", is_teen)

# every logical operators returns either True or False


# here
# scientific way of representing 4.44e8 is 4.44 * 10 ** 8
reservoir_volume = 4.445e8
print(reservoir_volume.__class__)
print(reservoir_volume)
rainfall = 5e6
rainfall = 0.9*rainfall
reservoir_volume *= 0.9  # reservoir_volume = reservoir_volume*0.9
reservoir_volume += rainfall
reservoir_volume *= 1.05
reservoir_volume *= .95
reservoir_volume -= 2.5e5
print(reservoir_volume)



sf_population, sf_area = 864816, 231.89
rio_population, rio_area = 6453682, 486.5

san_francisco_pop_density = sf_population/sf_area
rio_de_janeiro_pop_density = rio_population/rio_area

if san_francisco_pop_density < rio_de_janeiro_pop_density:
    print("populTION DENSITY OF SAN FARCISO IS GREATER")
else:
    print("smaller ...")

mon_sales = "121"
tues_sales = "105"
wed_sales = "110"
thurs_sales = "98"
fri_sales = "95"
total_sales = int(mon_sales) + int(tues_sales) + int(wed_sales) + int(thurs_sales) + int(fri_sales)
print("{} This is total sale".format(total_sales))

# immutable order series : String noted by "" or ''
message = 'This is secreate "message",'
print(message*2)  # duplication String
# string only support + and *
print("length", len(message), type(message))
print("String", type(str(is_teen)))

# function are very similar to operator (+, -, *)
# methods are fucntions that belong to a object
print(message.title())
print("one fish. Blue fish. red fish, fishy".count('fish'))
print(37.5.__class__)
one = 'Tthis is first string.'
two = 24.3
print("This is %s data for string format" % one)

# instead of %s , %d this new format method is less confusing and more productive
print("This is {} new data {}".format(one, two))

# Data structures are containers that organize and group data types together in different ways.
# list : mutable ordered sequence
one = ['one', 'two', 'three']
print(one[-1])
list_of_random_things = [1, 3.4, 'a string', True]
# in python range, lower bound is inclusive and upper bound is exclusive

months = ['jan', 'feb', 'mar', 'apr', 'may', 'june', 'july', 'aug', 'sep', 'oct', 'nov', 'dec']
# python slicing to access subsequence of list
print(months[3:6], " second quarter")
print(months[9:], "last quarter")
# list are types such as string, flat, int are more similar to String , both support len, index, slicing
# slicing returns list
# membership operator in , not in
print('membership operator:', 'jan' in months, 'sunday' in months, 'ok' in 'This is not thatok')

# list can be modify, String cannot
# MUTABILITY: if an object can changes its values after it has been created
# list is mutable and ordered (index work properly), add, remove, sort, change its one of index value
# ** Order** is about whether the position of an element in the object can be used to access the element.
months[0] = 'dec'
print("modified list", months)

s = "This is string"
# s[2] = 'L'  #ERROR:  TypeError: 'str' object does not support item assignment


# mutable and immutable behaves very different in assignment
ls = 'This is a string'
lm = ls
ls = "ok"
print(ls, lm)

# work on list
le = ["This", "is", "a", "string", "I", "dont"]
# following are functions of list, min for String list return first element if sorted, aplhabeticaly first
# python is case sensitive
print(min(le))
print(max(le))
print(sorted(le, reverse=True))
print(len(le))

lk = le
le[0] = "Changed"
print(lk, le)
# here both for lk and le first element got changed in "Changed", because these are mutable,
# this does not happen for String


le.append("last")  # add element to last in list
print(le)
print("-".join(le))  # returns a string consisting of the list elements joined by a separator string.

# Tuples are used to store related piece of information (co-ordinates, lattitude, longi) etc.
# ordered and immutable sequence of elements
# two or more values that are so closely related that they were always be used together

location = 10.4557, 8.9990
longitude, lattitude = location
print(location)

cordinates = (2, 4, 6)
print(cordinates, cordinates[1])


# A set is a data type for mutable unordered collections of unique elements.
# One application of a set is to quickly remove duplicates from a list.
# union , intersection are easy to perform with sets and much faster
numbers = [2, 4, 6, 1, 8, 1, 3, 0, 1, 5]
print(len(numbers))
x = set(numbers)
print(x, len(x), 2 in numbers)
# meaning of append is to add at the end, in ordered series(list) there is last element so we can perform append
# in case of unordered series (set), there is no last element, so we cannot append, we need to add element to it
# element is added at any location, we cannot access set with index and also we cannot pop (remove) with index
# we cannot do x[3] for set
x.add(9)
x.remove(5)
print(sorted(x, reverse=True))
print(x)


# Dictionary stores pairs of element key,value
print("\n\nDICTIONARY")
elements = {"hydrogen": 1, "helium": 2, "carbon": 6}
print(elements["helium"])  # print the value mapped to "helium"
elements['oxygen'] = 8
print(elements, 'carbon' in elements, elements.get('iron'))
n = elements.get('iron')

# Keyword 	Operator
# is 	evaluates if both sides have the same identity
# is not 	evaluates if both sides have different identities

print(n is None, n is not None)

newdata = {'Shanghai': 178, 'Istanbul': 13.3, 'Karachi': 13.0, 'Mumbai': 12.5}
print(newdata['Shanghai'])


a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == b)
print(a is b)
print(a == c)
print(a is c)  # returns False

animals = {'dogs': [20, 10, 15, 8, 32, 15], 'cats': [3,4,2,8,2,4], 'rabbits': [2, 3, 3], 'fish': [0.3, 0.5, 0.8, 0.3, 1]}

print(animals['fish'], animals['dogs'][3])
# print(animals[3])  # will return error(KeyError) as dictionary is unordered, cannot use index on it.

oneMore = {'tomato': 'red', 'orange': 'orange', 'cherry': 'red', 'banana': 'yellow'}
print(oneMore.keys(), oneMore.values())  # there are not lists
print(oneMore.items())  # dictionary items of tuple, these are not list of tuples , so we can access it easily
for x, y in oneMore.items():
    print(x, y)
for x in oneMore.keys():
    print(x)

oneMore['banana'] = 'green or yellow'
print(oneMore)

# COMPOUND DATA STRUCTURES
# dictionary items can be viewed as documents, we can create embedded doc,
# means we can create dictionaries of dictionary
elements = {"hydrogen": {"number": 1,
                         "weight": 1.00794,
                         "symbol": "H"},
              "helium": {"number": 2,
                         "weight": 4.002602,
                         "symbol": "He"}}
oxygen = {"number":8,"weight":15.999,"symbol":"O"}  # create a new oxygen dictionary
elements["oxygen"] = oxygen  # assign 'oxygen' as a key to the elements dictionary
print('elements = ', elements)
helium = elements["helium"]  # get the helium dictionary
hydrogen_weight = elements["hydrogen"]["weight"]  # get hydrogen's weight
print("hydrogen_weight", hydrogen_weight)

# adding property in gas
elements['helium']['is_noble_gas'] = True
elements['hydrogen']['is_noble_gas'] = True
print(elements)
print(sorted(elements))


# SHORT MEANING
# MUTABILITY: if an object can changes its values after it has been created

# if x is data structure (collection)
# ordered        ->     can access by x[0], x[6]
# mutable        ->     sort, add, remove its element
# order and mutable -> add, remove by index (change by index , append, pop etc)  x[2] = 'new value'

# list -> ordered and mutable
# String -> ordered and immutable
# set -> unordered and mutable
# tuple -> ordered and immutable
# dictionary -> unordered and mutable

# also there is change in way it behaves in assignment see line: 99
