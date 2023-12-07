#!/usr/bin/python3

def search_replace(my_list, search, replace):
    output = []
    for item in my_list:
        if item == search:
            output.append(replace)
        else:
            output.append(item)

    return output
