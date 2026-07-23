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