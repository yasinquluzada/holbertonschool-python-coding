#!/usr/bin/python3
"""Defines a Square with validated size and an area method."""


class Square:
    """Represent a square defined by its side length."""

    def __init__(self, size=0):
        """Initialize the square with an optional validated size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2
