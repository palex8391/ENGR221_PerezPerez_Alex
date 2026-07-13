"""
Author: Alex Perez Perez
Date: 07/12/26
Description:Simple data structures used for pathfinding in the game.
This module provides a queue for breadth-first search and a stack for depth-first search.
"""


class Queue():
    """A first-in, first-out (FIFO) data structure."""

    def __init__(self):
        # Store the queue items in a list.
        self.items = []

    def add(self, item) -> None:
        """Add an item to the end of the queue."""
        self.items.append(item)

    def remove(self):
        """Remove and return the item at the front of the queue."""
        return self.items.pop(0)

    def is_empty(self) -> bool:
        """Return True if the queue contains no items."""
        return len(self.items) == 0


class Stack():
    """A last-in, first-out (LIFO) data structure."""

    def __init__(self):
        # Store the stack items in a list.
        self.items = []

    def add(self, item) -> None:
        """Push an item onto the top of the stack."""
        self.items.append(item)

    def remove(self):
        """Remove and return the item from the top of the stack."""
        return self.items.pop()

    def is_empty(self) -> bool:
        """Return True if the stack contains no items."""
        return len(self.items) == 0