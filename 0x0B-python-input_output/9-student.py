#!/usr/bin/python3
""" A class that defines a student."""


class Student:
""" Defining a class name Student.
    Args:
        first_name(str): The first name 
        last_name(str): The last name
        age(int): The age
"""
    def __init__(self,first_name, last_name, age):
        self.first_name = first_name
	self.last_name = last_name
	self.age = age

    def to_json(self):
        return self.__dict__
