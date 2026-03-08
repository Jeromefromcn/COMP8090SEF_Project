"""
main.py
Demonstration of the MinHeap data structure and Heap Sort algorithm.
"""

from heap import MinHeap
from heap_sort import heap_sort, heap_sort_verbose


def demo_min_heap():
    print("=" * 50)
    print("  MinHeap Data Structure Demo")
    print("=" * 50)

    h = MinHeap()

    # Insert elements one by one
    values = [15, 10, 8, 4, 20, 3, 7]
    print(f"\nInserting: {values}")
    for v in values:
        h.insert(v)
        print(f"  insert({v:2d})  →  {h}")

    print(f"\nPeek (minimum): {h.peek()}")
    print(f"Heap size     : {h.size()}")

    # Extract all elements — they come out in sorted order
    print("\nExtracting all elements (should be ascending):")
    extracted = []
    while not h.is_empty():
        extracted.append(h.extract_min())
    print(f"  {extracted}")

    # Build heap from list using heapify (O(n))
    print("\nBuilding heap from list [9, 2, 6, 1, 5] using heapify:")
    h2 = MinHeap()
    h2.heapify([9, 2, 6, 1, 5])
    print(f"  {h2}")
    print(f"  Min element: {h2.peek()}")


def demo_heap_sort():
    print("\n" + "=" * 50)
    print("  Heap Sort Algorithm Demo")
    print("=" * 50)

    data = [38, 27, 43, 3, 9, 82, 10]
    print(f"\nInput : {data}")
    sorted_data = heap_sort(data)
    print(f"Sorted: {sorted_data}")
    print(f"(Original unchanged: {data})")

    print("\n--- Verbose step-by-step trace ---")
    heap_sort_verbose([5, 1, 4, 2, 8])


if __name__ == "__main__":
    demo_min_heap()
    demo_heap_sort()
