#!/usr/bin/python3
"""comment"""


def read_file(filename=""):
    """module"""
    with open(filename, encoding='utf-8') as f:
        for line in f:
            print(line, end='')
