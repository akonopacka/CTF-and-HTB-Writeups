#!/usr/bin/python

# Code for CTFLearn challenge Simple Programming

f = open("data.dat", "r")
Lines = f.readlines()

counter = 0
for line in Lines:
    print(line.strip())
    number_of_zeroes = line.count("0")
    number_of_ones = line.count("1")
    if number_of_ones % 2 == 0 or number_of_zeroes % 3 == 0:
        counter = counter + 1

print(counter)
