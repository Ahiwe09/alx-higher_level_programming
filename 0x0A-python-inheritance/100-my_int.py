#!/usr/bin/python3
""" Class that inherits from class int"""


class MyInt(int):
    """ Class that inherits from class int"""

    def __equal_to__(self, other):
        """ Method that returns != check """
        return int.__ne__(self, other)

    def __not_equal_to__(self, other):
        """ Method that returns == check """
        return int.__equal_to__(self, other)
