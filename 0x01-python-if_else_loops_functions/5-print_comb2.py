#!/usr/bin/python3

output = ""

for number in range(99):
    if number < 10:
        output += "0{:d}, ".format(number)
    else:
        output += "{:d}, ".format(number)

print("{:s}".format(output), end="")
print("{:d}".format(99))

