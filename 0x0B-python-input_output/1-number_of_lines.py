#!/usr/bin/python3
"""comment """


def number_of_lines(filename=""):
    """Module"""
    with open(filename, encoding='utf-8') as f:
        return len(f.readlines())
