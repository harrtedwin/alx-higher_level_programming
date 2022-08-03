#!/usr/bin/python3
"""Comment"""


def write_file(filename="", text=""):
    """Module"""
    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)
