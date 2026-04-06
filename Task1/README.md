# Task 1 – Student Record Search System

A Python OOP-based application for managing and searching student records.

## Overview

This system allows users to store, query, and manage undergraduate and graduate student
records. It demonstrates all OOP concepts covered in COMP8090SEF.

## OOP Concepts Used

| Concept               | Where                                                                         |
|-----------------------|-------------------------------------------------------------------------------|
| **Classes & Objects** | `Person`, `Student`, `GradStudent`, `StudentDatabase`                         |
| **Encapsulation**     | Private attributes (`__name`, `__gpa`, etc.) with `@property` getters/setters |
| **Inheritance**       | `Student` extends `Person`; `GradStudent` extends `Student`                   |
| **Polymorphism**      | `get_role()` and `get_summary()` overridden at each level                     |
| **Abstraction**       | `Person` is an abstract base class (`ABC`) with abstract methods              |

## File Structure

```
Task1/
├── person.py      # Abstract base class: Person
├── student.py     # Student and GradStudent classes
├── database.py    # StudentDatabase with search methods
└── main.py        # Entry point and demo
```

## How to Run

Python 3.10+ is required. No external packages needed.

```bash
cd Task1
python main.py
```

## Sample Output

```
=== Populating Database ===
  Added: [Undergraduate] Alice Wong (ID: S001) | Major: Computer Science | GPA: 3.80
  ...
=== Search by Major: Computer Science ===
  Found 3 record(s):
    ID: S001 | Name: Alice Wong | Major: Computer Science | GPA: 3.80
    ...
```

## Planned Improvements

- Add file persistence (save/load records from CSV)
- Implement a sort-by-GPA feature using a sorting algorithm
- Add a simple CLI menu for interactive use
