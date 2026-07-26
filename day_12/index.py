# modules.
# a module is a file containing a set of codes/functions which can be included in an application.

# creating a module.
# to create a module, we write the code in a python script and save it as a .py file.


# importing a module
# we use the import keyword and the file name only.

import mymodule
print(mymodule.generate_full_name('mubaraq', 'ayanleke'))

# importing functions from a module.

from mymodule import generate_full_name, sum_two_nums, person, gravity
print(generate_full_name('mubaraq', 'ay'))
print(sum_two_nums(1,9))
mass = 100
weight = mass * gravity
print(weight)
print(person['firstname'])

# import function from a module and renaming.
# during importing we can rename the module.

from mymodule import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g
print(fullname('mubby', 'jr'))
print(total(1,9))
mass = 100
weight = mass * g
print(weight)
print(p)
print(p['firstname'])

# import built-in modules.
# Built-in modules are ready-made Python modules that come with Python

# os module.
# this is a built-in python module used to interact with the operating system such as creating, deleting, renaming and accessing file and folders.

# import the module
import os
# creating a directory
os.mkdir('hello')
# changing the current directory
os.chdir(r"C:\Users\Admin\Desktop\python\day_12")
# get the current working directory
print(os.getcwd())
# removing directory
os.rmdir('hello') 


# sys module.
# this is a built-in module that provides access to python' runtime evnironment, such as command-line arguments and interpreter information.

# argv - argument vector
# sys.argv[0] - is the name of the script, so it's always on index 0 in the list.
import sys
print(sys.argv[0], sys.argv[1], sys.argv[2])
# format() is basically like f-string
print('welcome {}. Enjoy {} challenge!'.format(sys.argv[1], sys.argv[2]))

#  - wrote this f-string to confirm.
print(f'hello, {sys.argv[1]}. enjoy {sys.argv[2]} challenge')

print("1. Total items in sys.argv:", len(sys.argv))
print("2. the actual sys.argv list:", sys.argv)

# use quotes to make the terminal treat the entire string as an argument.

# sys.path tells python where to search for modules.
print(sys.path)


import mymodule

print(dir(mymodule))

# to exit sys
#  we use sys.exit()

print('start')

# sys.exit()

print('end')

# to know the largest integer variable it takes
# we use sys.maxsize
print(sys.maxsize)

# to know the version of python you are using, 
# we use sys.version

print(sys.version)