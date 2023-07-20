import os

path = 'py/output.txt'

f = open(path, 'r')
file = f.readlines()
file = file[2:-1]
for f in file:
    f = f[5:]
    farr = f.split(" ")
    directory = farr[0][1: len(farr[0]) - 2]
    name = farr[1][1:len(farr[1]) - 3]
    if name.endswith('jp'):
        name = name + 'g'
    directory = directory.split('/')
    old_name = directory[-1]
    directory = directory[:-1]
    new_directory = '/'
    for d in directory:
        new_directory = new_directory + d + '/'
    os.rename(os.path.join(new_directory, name), os.path.join(new_directory, old_name))
