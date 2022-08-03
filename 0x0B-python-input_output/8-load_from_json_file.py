#!/usr/bin/python3
"""Comment"""


from json import loads


def load_from_json_file(filename):
    """Module"""
    with open(filename, encoding='utf-8') as f:
        return loads(f.read())
