#!/usr/bin/python3
"""This module defines a Square class with a private size attribute."""


class Square:
    """Square defines a square by storing its size privately."""

    def __init__(self, size):
        """Initialize a new Square instance with a given size."""
        self.__size = size
