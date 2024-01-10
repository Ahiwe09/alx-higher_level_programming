#!/usr/bin/python3
""" in this module we have a function that checks if an object
is an instance of a class or it's subclass"""


def inherits_from(obj, a_class):
    """ checkss if obj belongs to a_class or it's subclass """
    i = type(obj)
    if i is a_class:
        return False
    if issubclass(i, a_class):
        return True
    return False
