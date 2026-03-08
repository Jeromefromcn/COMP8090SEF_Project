"""
heap_sort.py
Implementation of the Heap Sort algorithm.

How Heap Sort works (ascending order):
  Phase 1 – Build a Max-Heap from the input array.         O(n)
  Phase 2 – Repeatedly extract the maximum element:
             swap root (max) with the last element,
             reduce heap size by 1,
             sift-down the new root.                       O(n log n)

Overall time complexity : O(n log n)  — best, average, and worst case
Space complexity        : O(1)        — in-place, no extra array needed
"""


def _sift_down_max(arr: list, n: int, root: int) -> None:
    """
    Maintain the Max-Heap property for the subtree rooted at `root`.
    Only considers elements within indices [0, n).

    Args:
        arr  : the array being sorted
        n    : current effective heap size
        root : index of the subtree root to sift down
    """
    largest = root
    left = 2 * root + 1
    right = 2 * root + 2

    # Find the largest value among root and its children
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If root is not the largest, swap and continue sifting down
    if largest != root:
        arr[root], arr[largest] = arr[largest], arr[root]
        _sift_down_max(arr, n, largest)  # recursive call


def heap_sort(arr: list) -> list:
    """
    Sort a list in ascending order using the Heap Sort algorithm.
    Returns a NEW sorted list (does not modify the original).

    Args:
        arr : list of comparable elements

    Returns:
        A new list sorted in ascending order.

    Example:
        >>> heap_sort([4, 10, 3, 5, 1])
        [1, 3, 4, 5, 10]
    """
    result = list(arr)  # work on a copy
    n = len(result)

    # --- Phase 1: Build Max-Heap ---
    # Start from the last non-leaf node and sift down each node.
    for i in range(n // 2 - 1, -1, -1):
        _sift_down_max(result, n, i)

    # --- Phase 2: Extract elements one by one ---
    # Move the current root (maximum) to the end of the array,
    # then restore the heap property for the remaining elements.
    for i in range(n - 1, 0, -1):
        result[0], result[i] = result[i], result[0]  # move max to end
        _sift_down_max(result, i, 0)  # re-heapify

    return result


# ------------------------------------------------------------------ #
#  Step-by-step trace (for study / demonstration purposes)           #
# ------------------------------------------------------------------ #

def heap_sort_verbose(arr: list) -> list:
    """
    Same as heap_sort() but prints each step for educational purposes.
    """
    result = list(arr)
    n = len(result)

    print(f"Input            : {result}")

    # Phase 1
    for i in range(n // 2 - 1, -1, -1):
        _sift_down_max(result, n, i)
    print(f"After build-heap : {result}")

    # Phase 2
    for i in range(n - 1, 0, -1):
        result[0], result[i] = result[i], result[0]
        print(f"  Swap root→end  : {result}  (heap size={i})")
        _sift_down_max(result, i, 0)
        print(f"  After sift-down: {result}")

    print(f"Sorted           : {result}")
    return result
