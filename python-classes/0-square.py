#!/usr/bin/python3
"""This module defines a basic Square class with a private size attribute."""


class Square:
    """Square defines a square by storing its size as a private attribute."""

    def __init__(self, size):
        """Initialize a Square instance with a size (no validation required)."""
        self.__size = size
