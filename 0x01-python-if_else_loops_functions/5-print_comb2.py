#!/usr/bin/python3

output = ""
'#'built output by using string format to fill-up the strings.
for number in range(99):
    if number < 10:
        output += "0{:d}, ".format(number)
    else:
        output += "{:d}, ".format(number)
'#'print from 0 to 98.
print("{:s}".format(output), end="")
'#'and print 99.
print("{:d}".format(99))

