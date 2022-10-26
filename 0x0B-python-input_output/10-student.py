#!/usr/bin/python3
"""A class Student that defines a student."""


class Student:
    """Defining the Student class."""

    def __init__(self, first_name, last_name, age):
    """Initialize a new student."""
        self.first_name = first_name
	self.last_name = last_name
	self.age = age

    def to_json(self, attrs=None):
        """ Getting a dict representation of the student."""
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
