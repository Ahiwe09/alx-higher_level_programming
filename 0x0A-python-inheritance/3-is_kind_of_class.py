#!/usr/bin/python3
""" in this module we have a function that checks if an object
is an instance of a class or it's subclass"""


def is_kind_of_class(obj, a_class):
    """ checkss if obj belongs to a_class or it's subclass """
    i = type(obj)
    if i is a_class:
        return True
    if issubclass(i, a_class):
        return True
    return False
