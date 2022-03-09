# general scripting
# finally: Before Python leaves this try statement, it will run the code in this finally block under any conditions,
# even if it's ending the program. E.g., if Python ran into an error while running code in the except or else block,
# this finally block will still be executed before stopping the program.
# Other situations that can cause differences:

#  If an exception is thrown inside the except block.
#  If an exception is thrown in run_code1() but it's not a TypeError.
#  Other control flow statements such as continue and break statements.

# typically used to close the file

try:
    #ok = input('give number')
    num = 200/0
except Exception as e:
    print("Exception :{}".format(e))

try:
    ok = int("ten")
except ValueError:
    print("error")
except:
    print('Other error')

# opening file without 'w', if file is not present error is thrown FileNotFoundError
# opening with 'w', file is created if not present
f = open('text.txt', 'w')
# write will delete all previous content of file, use append to append file
f.write("Hello here !!")
f.close()  # sure to close file immedietly after use. if not closed,
# after some time you will not be able to open new file
# there is limit to number of file that can kept open in OS
# also closing will free up any system resources taken up by the file.
# lets check limit
files = []
# OSError: [Errno 24] Too many open files: 'text.txt'   for 8188 files
# so we can only keep open upto 8189 file in prgramme simultaneously
count = 0

'''
for i in range(10000):
    files.append(open('text.txt', 'r'))
    print("File opened: {}".format(count+1))
    files.append(open('text.txt', 'r'))
    print("File opened: {}".format(count+2))
    files.append(open('text.txt', 'r'))
    print("File opened: {}".format(count+3))
    count += 3
    print("loop :{}".format(i)) '''

f = open('text.txt', 'r')
file_data = f.read()
f.close()
# after closing file immediately, we can still use file_data
print(file_data)

# Python provides a special syntax that auto-closes a file for you once you're finished using it.
with open('text.txt', 'r') as f:
    f_data = f.read()

# after end of with use cannot use f object but we can still have f_data
print(f_data)

with open('text.txt', 'w') as f:
    f.write("We're the knights of the round table\nWe dance whenever we're able")

with open('text.txt', 'r') as f:
    print(f.read(4))
    print(f.read(5))
    print(f.read())

with open("text.txt") as f:
    for line in f:
        print(line)

""" most used modules here from Python Standard Library
    csv: very convenient for reading and writing csv files
    collections: useful extensions of the usual data types including OrderedDict, defaultdict and namedtuple
    random: generates pseudo-random numbers, shuffles sequences randomly and chooses random items
    string: more functions on strings. This module also contains useful collections of letters like string.digits 
        (a string containing all characters which are valid digits).
    re: pattern-matching in strings via regular expressions
    math: some standard mathematical functions
    os: interacting with operating systems
    os.path: submodule of os for manipulating path names
    sys: work directly with the Python interpreter
    json: good for reading and writing json files (good for web work)
"""

# when we import module, module is taken as object of type module
# from module_name import object1, object2
# we can directly access the object without referencing module

# requirements.txt should include all of dependencies with version
# pip install -r requirements.txt
# here everything from requirement.txt got installed in this private venv environment.

""" Useful Third-Party Packages

    IPython - A better interactive Python interpreter
    requests - Provides easy to use methods to make web requests. Useful for accessing web APIs.
    Flask - a lightweight framework for making web applications and APIs.
    Django - A more featureful framework for making web applications. Django is particularly good for designing complex,
        content heavy, web applications.
    Beautiful Soup - Used to parse HTML and extract information from it. Great for web scraping.
    pytest - extends Python's builtin assertions and unittest module.
    PyYAML - For reading and writing YAML files.
    NumPy - The fundamental package for scientific computing with Python. It contains among other things a powerful 
        N-dimensional array object and useful linear algebra capabilities.
    pandas - A library containing high-performance, data structures and data analysis tools. In particular, 
        pandas provides dataframes!
    matplotlib - a 2D plotting library which produces publication quality figures in a variety of hardcopy formats 
        and interactive environments.
    ggplot - Another 2D plotting library, based on R's ggplot2 library.
    Pillow - The Python Imaging Library adds image processing capabilities to your Python interpreter.
    pyglet - A cross-platform application framework intended for game development.
    Pygame - A set of Python modules designed for writing games.
    pytz - World Timezone Definitions for Python
"""

# following pytz library is not installed globally in python3, but installed here locally only.based on requirements.txt
# creating virtual env for this project

from datetime import datetime
import pytz

utc = pytz.utc
ist = pytz.timezone('Asia/Kolkata')
print(utc.__class__, ist.__class__)

now = datetime.now(tz=utc)
ist_now = now.astimezone(ist)

print(now)
print(ist_now)


