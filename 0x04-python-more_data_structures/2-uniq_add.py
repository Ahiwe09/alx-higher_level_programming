#!/usr/bin/python3

def uniq_add(my_list=[]):
    output_list = []
    for i in my_list:
        if i not in output_list:
            output_list.append(i)
        continue
    return sum(output_list)
