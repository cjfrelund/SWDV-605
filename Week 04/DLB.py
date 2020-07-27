# DLB.py
# Doubly Linked Base

class _DoublyLinkedBase:
    """A base class providing a doubly linked list representation."""

    class _Node:
        """Lightweight, nonpublic class for stoaring a doubly linked node."""
        __slots__ = '_element', '_previous', '_next'  # streamlines memory

        # initialize node's fields
        def __init__(self, element, previous, next):
            self._element = element  # user's element
            # previous node reference
            self._previous = previous
            self._next = next  # next node reference

    def __init__(self):
        """Create an empty list."""
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        # trailer is after header
        self._header._next = self._trailer
        # header is before trailer
        self._trailer._previous = self._header
        self._size = 0  # number of elements

    def __len__(self):
        """Return the number of elements in the list"""
        return self._size

    def is_empty(self):
        """Return True if list is empty."""
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        """Add element between two existing nodes and return new node."""
        newest = self._Node(
            e, predecessor, successor)  # linked to neighbors
        predecessor._next = newest
        successor._previous = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        """Delete nonsentinel node from the list and return its element."""
        predecessor = node._previous
        successor = node._next
        predecessor._next = successor
        successor._previous = predecessor
        self._size -= 1
        # record deleted element
        element = node._element
        # deprecate node
        node._previous = node._next = node._element = None
        return element

    # note the use of inheritance


class LinkedDeque(_DoublyLinkedBase):
    """Double ended queue implementation based on a doubly linked list."""

    def first(self):
        """Return (but do not remove) the element at the front of the deque."""
        if self.is_empty():
            raise Exception("Deque is empty")
        # real item just after header
        return self._header._next._element

    def last(self):
        """Return (but do not remove) the element at the back of the deque."""
        if self.is_empty():
            raise Exception("Deque is empty")
        # real item just before trailer
        return self._trailer._previous._element

    def insert_first(self, e):
        """Add an element to the front of the deque."""
        self._insert_between(
            e, self._header, self._header._next)  # after trailer

    def insert_last(self, e):
        """Add an element to the back of the deque."""
        self._insert_between(e, self._trailer._previous,
                             self._trailer)  # before trailer

    def delete_first(self):
        """Remove and return the element from the front of the deque.

        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Exception("Deque is empty")
        # use inherited method
        return self._delete_node(self._header._next)

    def delete_last(self):
        """Remove and return the element from the back of the deque.

        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Exception("Deque is empty")
        # use inherited method
        return self._delete_node(self._trailer._previous)
