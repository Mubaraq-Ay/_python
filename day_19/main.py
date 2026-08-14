# file handling.

# file handling is an important part of programming that allows us to 
# create, read, update and delete files.
# We use the built-in open() function to work with files.

# syntax
# open('filename', mode)

'''
    r - read
    w - write → creates if missing, overwrites if it exists
    a - append  → creates if missing, adds to the end
    x - create → creates only, errors if it already exist

    t - text
    b - binary
'''


# opening files for reading.
# the default mode for opening a file is reading. we dont need to specify 'r' or 'rt'

f = open('../reading_file_example.txt')
print(f) 

txt = f.read()
print(type(txt))
print(txt)
f.close()

# instead of printing all the text, print the furst 10 characters of the text file.

f = open('../reading_file_example.txt')
txt = f.read(10)
print(type(txt))
print(txt)


# readline() - prints the first line of the file.

f = open('../reading_file_example.txt')
line = f.readline()
print(type(line))
print(line)

# readlines -  read all the text line by line and returns a list of lines.

f = open('../reading_file_example.txt')
lines = f.readlines()
print(type(lines))
print(lines)
f.close()

# another way to get all the lines as a list is using splitlines()

f = open('../reading_file_example.txt')
lines = f.read().splitlines()
print(type(lines))
print(lines)
f.close()

# new way of closing a file.

with open('../reading_file_example.txt') as f:
    lines = f.read().splitlines()
    print(type(lines))
    print(lines)


# opening files for writing and updating
# to write an existing file, we must add mode as a parameter to the open() function.

'''
    a - append - will append to the end of the file. if file does not exist it creates a new file.
    w - write - will overwrite any existing content, if the file does not exist it creates.
'''

with open('../reading_file_example.txt', 'a') as f:
    f.write('this is the appended text')

# this method creates a new file if the file does not exist
with open('../reading_file_example.txt', 'w') as f:
    f.write('this is a newly created file') # if file exist sef, it clears everything there and upload what is here.


# deleting files
# we use os module if we want to remove a file ;)

import os

if os.path.exists('../reading_file_example.txt'):
    os.remove('../reading_file_example.txt')
else:
    print('this file does not exist.')