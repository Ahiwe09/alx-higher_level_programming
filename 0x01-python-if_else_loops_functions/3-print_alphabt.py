#!/usr/bin/python3

output = ""
for i in range(97, 123):
    if chr(i)!= "q" and chr(i) != "e":
        output += chr(i)

print("{:s}".format(output), end="")
