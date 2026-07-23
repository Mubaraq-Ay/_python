import os

print(os.getcwd())

# navigation.

os.chdir(r'C:\Users\Admin\Desktop\python\day_12')
print(os.getcwd())

os.mkdir('practice')
print(os.listdir())
os.rmdir('practice')
print(os.listdir())

# create directory
os.mkdir('Backend_project')
# change to the directory
os.chdir(r'Backend_project')
# pwd
print(os.getcwd())

 
