import sys

def readlines_file(file_name):
    with open(file_name,'r') as file:
        return file.readlines()

file_name = sys.argv[1:2]

lines = readlines_file('thermo.txt')

temp = ''.join(lines[-1])

print(temp)
