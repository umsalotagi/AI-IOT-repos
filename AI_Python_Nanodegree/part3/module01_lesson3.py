
weight = 70
height = 172

if 18.5 <= weight / height**2 < 25:
    print("BMI is considered 'normal'")

unsubscribed = False
location = 'USA'
if (not unsubscribed) and (location == "USA" or location == "CAN"):
    print("send email")


# Here are most of the built-in objects that are considered False in Python:
#    constants defined to be false: None and False
#    zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
#    empty sequences and collections: '"", (), [], {}, set(), range(0)
# use the truth value of objects

one = None
two = []
error = 0

if not one:
    print("None is False")
if not two:
    print("empty list is False")
if not error:
    print("zero value is False. errors are not seen")


# An iterable is an object that can return one of its elements at a time.
# This can include sequence types, such as strings, lists, and tuples,
# as well as non-sequence types, such as dictionaries and files.

# range() is a built-in function used to create an iterable sequence of numbers.
# You will frequently use range() with a for loop to repeat an action a certain number of times.
# range(start=0, stop, step=1)

# creating a list
cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
capitalisezCity = []
for city in cities:
    capitalisezCity.append(city.title())
print(capitalisezCity)

# Modifying a list is a bit more involved, and requires the use of the range() function.
for index in range(len(cities)):
    cities[index] = cities[index].title()
print(cities)

for num in range(5, 31, 5):
    print(num)

for num in range(1, 31):
    if num % 5 == 0:
        print(num)

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

for index in range(len(names)):
    names[index] = names[index].lower().replace(" ", "_")

print(names)

tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0
for token in tokens:
    if token.startswith("<") and token.endswith(">"):
        count += 1
print(count)

print(list(range(0, -5, -1)))



result = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']
for item, quantity in basket_items.items():
    if item in fruits:
        result += quantity
print(result)


card_deck = [4, 11, 8, 5, 13, 2, 8, 10]
hand = []
while sum(hand) <=17:
    hand.append(card_deck.pop())
    print(sum(hand))
print(hand)


number = 6
product, current = 1, 1

while current <= number:
    product *= current
    print(current, product)
    current += 1
print(product)


print("\n\n\nZIP and ENUMERATE")
# zip and enumerate are useful built-in functions that can come in handy when dealing with loops.
# zip returns an iterator that combines multiple iterables into one sequence of tuples.
# Each tuple contains the elements in that position from all the iterables.
letters = ['a', 'b', 'c']
nums = [1, 2, 3]
# list of tuples
list_tuples = list(zip(nums, letters))
print(list_tuples)

for num, letter in zip(nums, letters):
    print("{} and {} output".format(num, letter))

# unzip
new_nums, new_letter = zip(*list_tuples)
print(new_nums, new_letter)

# enumerate is a built in function that returns an iterator of tuples containing indices and values of a list.
# You'll often use this when you want the index along with each element of an iterable in a loop.
letters = ['a', 'b', 'c', 'd', 'e']
for i, l in enumerate(letters):
    print(i, l)


x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []

for x, y, z, label in zip(x_coord, y_coord, z_coord, labels):
    points.append("{}: {}, {}, {}".format(label, x, y, z))

print(points)

sample_tuple = 10, 20, 30
print(sample_tuple)
x, y, z = sample_tuple
print(x, y, z)

cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]
cast_dictionary = dict(zip(cast_names, cast_heights))
print(cast_dictionary)

cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))
names, heights = zip(*cast)
print(names, heights)

# transpose a matrix
data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))
# using tuple for matrix as it is closely related data ...
data_transpose = tuple(zip(*data))
print(list(data_transpose))

cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]

for i, cas in enumerate(cast):
    cast[i] += " " + str(heights[i])

print(cast)

ok = ""
ok.lower().split()

# list comprehensions to create new list easily with single line
names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]
first_names = [name.lower().split(" ")[0] for name in names]
print(first_names)

# first 20 multiples of 3
multiples_3 = [num*3 for num in range(1, 21)]
print(multiples_3)

scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }
passed = [name for name, score in scores.items() if score >= 65]
print(passed)

"""
Mutable -> liable to change. (chanchal, badalnyayogya)

Mutable data types : list, set, dictionary               | Immutable data types: boolean, int, float, tuple, string 
mutable data type can be changed after they are created  | cant be changed after they are created
passed to function as pointer to original object         | Are passed to function as copy of original object
changes thaqt happen to pointer in function              | changed happen to this copy within function don't 
change the original object                               | affect original value

Data created inside function no longer available inside ram once we are outside function
"""

