# Task 2 – Heap Data Structure & Heap Sort Algorithm

Self-study report and implementation for COMP8090SEF.

---

## Chosen Topics

| Category           | Topic                  |
|--------------------|------------------------|
| **Data Structure** | Min-Heap (Binary Heap) |
| **Algorithm**      | Heap Sort              |

These two topics are naturally related: Heap Sort is built on top of the Heap data structure,
making them ideal to study together.

---

## 1. Min-Heap — Data Structure

### What is a Heap?

A **Binary Heap** is a complete binary tree that satisfies the *heap property*:

- **Min-Heap**: every parent node ≤ its children → root holds the **minimum** value.
- **Max-Heap**: every parent node ≥ its children → root holds the **maximum** value.

### Array Representation

A heap is efficiently stored as a flat array. For a node at index `i`:

```
Parent       = (i - 1) // 2
Left child   = 2 * i + 1
Right child  = 2 * i + 2
```

Example — inserting `[15, 10, 8, 4, 3]` into a MinHeap:

```
Array: [3, 4, 8, 15, 10]

        3
       / \
      4   8
     / \
   15  10
```

### Key Operations & Time Complexity

| Operation       | Description                    | Time     |
|-----------------|--------------------------------|----------|
| `insert(v)`     | Append then sift-up            | O(log n) |
| `extract_min()` | Swap root↔last, pop, sift-down | O(log n) |
| `peek()`        | Read `data[0]`                 | O(1)     |
| `heapify(list)` | Build from unsorted list       | O(n)     |

### Applications

- **Priority Queue** – process tasks by urgency (e.g. hospital triage, CPU scheduling)
- **Dijkstra's shortest-path algorithm** – always expand the closest unvisited node
- **Heap Sort** – see below

---

## 2. Heap Sort — Algorithm

### How It Works

Heap Sort runs in two phases using a **Max-Heap**:

**Phase 1 – Build Max-Heap** (O(n))
Convert the input array into a valid Max-Heap by calling `sift_down` on every
non-leaf node from bottom to top.

**Phase 2 – Sort** (O(n log n))
Repeat n−1 times:

1. Swap the root (current maximum) with the last element.
2. Shrink the heap size by 1.
3. Sift-down the new root to restore the Max-Heap property.

### Step-by-step Example

Input: `[5, 1, 4, 2, 8]`

```
After build Max-Heap : [8, 2, 4, 1, 5]   (8 is at root)

Step 1: swap(8,5) → [5, 2, 4, 1, | 8]   sift-down → [5, 2, 4, 1]
Step 2: swap(5,1) → [1, 2, 4, | 5, 8]   sift-down → [4, 2, 1]
Step 3: swap(4,1) → [1, 2, | 4, 5, 8]   sift-down → [2, 1]
Step 4: swap(2,1) → [1, | 2, 4, 5, 8]   done

Sorted: [1, 2, 4, 5, 8]  ✓
```

### Time & Space Complexity

| Case    | Time       |
|---------|------------|
| Best    | O(n log n) |
| Average | O(n log n) |
| Worst   | O(n log n) |

**Space: O(1)** — sorting is done in-place with no extra array.

Compared with Merge Sort (O(n) extra space), Heap Sort is more memory-efficient.

---

## File Structure

```
Task2/
├── heap.py        # MinHeap class
├── heap_sort.py   # heap_sort() and heap_sort_verbose()
└── main.py        # Demo and test cases
```

## How to Run

Python 3.10+ required. No external packages.

```bash
cd Task2
python main.py
```

---

## References

1. Cormen, T. H. et al. *Introduction to Algorithms*, 4th ed., MIT Press, 2022. Ch. 6.
2. GeeksforGeeks – "Heap Data Structure": https://www.geeksforgeeks.org/heap-data-structure/
3. Wikipedia – "Heapsort": https://en.wikipedia.org/wiki/Heapsort
