#!/usr/bin/python3
"""module"""


def append_write(filename="", text=""):
    """comment """
    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)
