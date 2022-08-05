#!/usr/bin/python3
"""

A model that contains a Base class to manage
the id attribute of all classes that extend
from Base and avoid duplicate the same code.

"""

from os import path
import json
import os.path
import turtle


class Base:
    """
    ...
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        ...
        """

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + '.json'

        with open(filename, mode='w', encoding='utf-8') as f:
            if list_objs is None:
                return f.write(cls.to_json_string(None))

            json_attrs = []

            for elem in list_objs:
                json_attrs.append(elem.to_dictionary())

            return f.write(cls.to_json_string(json_attrs))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == 'Square':
            dummy = cls(3)

        if cls.__name__ == 'Rectangle':
            dummy = cls(3, 3)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + '.json'

        if path.exists(filename) is False:
            return []

        with open(filename, mode='r', encoding='utf-8') as f:
            objs = cls.from_json_string(f.read())
            instances = []

            for elem in objs:
                instances.append(cls.create(**elem))

            return instances
    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw shapes using turtle module"""

        turtle.setheading(0)
        turtle.penup()
        for obj in list_rectangles + list_squares:
            turtle.setposition(obj.x, obj.y)
            turtle.begin_fill()
            turtle.forward(obj.width)
            turtle.left(90)
            turtle.forward(obj.height)
            turtle.left(90)
            turtle.forward(obj.width)
            turtle.left(90)
            turtle.forward(obj.height)
            turtle.left(90)
            turtle.end_fill()

    @classmethod
    def create(cls, **dictionary):
        """Method to raeturn a new instance of a
        class from an attribute dictionary
        """
        if cls.__name__ == "Rectangle":
            obj = cls(1, 1)
        elif cls.__name__ == "Square":
            obj = cls(1)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """method to load a list of instances from a JSON file"""

        if not os.path.exists(cls.__name__ + '.json'):
            return []
        with open(cls.__name__ + '.json', 'rt') as file:
            objects = cls.from_json_string(file.read())
        return [cls.create(**d) for d in objects]

    @classmethod
    def save_to_file(cls, list_objs):
        """Method to save a JSON sting to a file"""

        if list_objs is None:
            list_objs = []
        list_objs = [b.to_dictionary() for b in list_objs]
        list_objs = cls.to_json_string(list_objs)
        with open(cls.__name__ + ".json", "wt") as myFile:
            myFile.write(list_objs)

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON string representation of 'list_dictionaries
        Args:
            list_dictionaries: A list of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) < 1:
            return "[]"
        else:
            return json.dumps(list_dictionaries)