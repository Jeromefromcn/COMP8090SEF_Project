"""
heap.py
Implementation of a Min-Heap data structure.

A Min-Heap is a complete binary tree stored as an array where:
  - The parent node is always SMALLER than or equal to its children.
  - The smallest element is always at the root (index 0).

Index relationships for a node at index i:
  - Parent  : (i - 1) // 2
  - Left child  : 2 * i + 1
  - Right child : 2 * i + 2
"""


class MinHeap:
    """
    Min-Heap implemented with a Python list.

    Supported operations:
      insert(value)   – O(log n)
      extract_min()   – O(log n)
      peek()          – O(1)
      heapify(list)   – O(n)  (build heap from existing list)
    """

    def __init__(self):
        self._data: list = []   # internal array representation

    # ------------------------------------------------------------------ #
    #  Public Interface                                                    #
    # ------------------------------------------------------------------ #

    def insert(self, value) -> None:
        """Insert a new value and restore the heap property."""
        self._data.append(value)
        self._sift_up(len(self._data) - 1)

    def extract_min(self):
        """
        Remove and return the smallest element.
        Raises IndexError if the heap is empty.
        """
        if self.is_empty():
            raise IndexError("extract_min() called on an empty heap.")
        # Swap root with last element, then remove last
        self._swap(0, len(self._data) - 1)
        minimum = self._data.pop()
        # Restore heap property from the root downward
        if not self.is_empty():
            self._sift_down(0)
        return minimum

    def peek(self):
        """Return the smallest element without removing it."""
        if self.is_empty():
            raise IndexError("peek() called on an empty heap.")
        return self._data[0]

    def heapify(self, data: list) -> None:
        """
        Build a heap from an unsorted list in O(n) time.
        Starts sifting down from the last non-leaf node.
        """
        self._data = list(data)
        # Last non-leaf index
        start = (len(self._data) - 2) // 2
        for i in range(start, -1, -1):
            self._sift_down(i)

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def size(self) -> int:
        return len(self._data)

    def __str__(self) -> str:
        return f"MinHeap({self._data})"

    # ------------------------------------------------------------------ #
    #  Private Helpers                                                     #
    # ------------------------------------------------------------------ #

    def _sift_up(self, index: int) -> None:
        """Move node at `index` upward until heap property is satisfied."""
        while index > 0:
            parent = (index - 1) // 2
            if self._data[index] < self._data[parent]:
                self._swap(index, parent)
                index = parent
            else:
                break  # heap property satisfied

    def _sift_down(self, index: int) -> None:
        """Move node at `index` downward until heap property is satisfied."""
        n = len(self._data)
        while True:
            smallest = index
            left  = 2 * index + 1
            right = 2 * index + 2

            # Find the smallest among node and its children
            if left < n and self._data[left] < self._data[smallest]:
                smallest = left
            if right < n and self._data[right] < self._data[smallest]:
                smallest = right

            if smallest != index:
                self._swap(index, smallest)
                index = smallest
            else:
                break  # heap property satisfied

    def _swap(self, i: int, j: int) -> None:
        self._data[i], self._data[j] = self._data[j], self._data[i]
