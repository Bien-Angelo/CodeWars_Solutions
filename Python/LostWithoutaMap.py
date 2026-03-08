#!/usr/bin/env python3

"""
Given an array of integers, return a new array with each value doubled.

For example:

[1, 2, 3] --> [2, 4, 6]
"""
def maps(a):
    new_array = []
    for x in a:
        new_array.append(x * 2)
    return new_array
