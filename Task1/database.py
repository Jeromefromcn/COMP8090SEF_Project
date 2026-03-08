"""
database.py
Defines the StudentDatabase class that manages a collection of Student objects.
Demonstrates:
- Encapsulation (internal list hidden from outside)
- Use of objects / composition
- Linear search and filter-based search methods
"""

from student import Student, GradStudent


class StudentDatabase:
    """
    A simple in-memory database for storing and searching Student records.
    Supports adding, removing, and searching by multiple criteria.
    """

    def __init__(self):
        # Encapsulation: the record list is private
        self.__records: list[Student] = []

    def add_student(self, student: Student) -> None:
        """Add a Student (or GradStudent) to the database."""
        if not isinstance(student, Student):
            raise TypeError("Only Student instances can be added.")
        # Prevent duplicate IDs
        if self.find_by_id(student.student_id):
            raise ValueError(f"Student ID '{student.student_id}' already exists.")
        self.__records.append(student)
        print(f"  Added: {student}")

    def remove_student(self, student_id: str) -> bool:
        """Remove a student by ID. Returns True if removed, False if not found."""
        for i, s in enumerate(self.__records):
            if s.student_id == student_id:
                removed = self.__records.pop(i)
                print(f"  Removed: {removed.name} ({student_id})")
                return True
        print(f"  Student ID '{student_id}' not found.")
        return False

    def find_by_id(self, student_id: str) -> Student | None:
        """Linear search by student ID. Returns the Student or None."""
        for s in self.__records:
            if s.student_id == student_id:
                return s
        return None

    def search_by_name(self, keyword: str) -> list[Student]:
        """Case-insensitive partial match on student name."""
        keyword = keyword.lower()
        return [s for s in self.__records if keyword in s.name.lower()]

    def search_by_major(self, major: str) -> list[Student]:
        """Case-insensitive exact match on major."""
        return [s for s in self.__records if s.major.lower() == major.lower()]

    def search_by_gpa_range(self, min_gpa: float, max_gpa: float) -> list[Student]:
        """Return all students whose GPA falls within [min_gpa, max_gpa]."""
        return [s for s in self.__records if min_gpa <= s.gpa <= max_gpa]

    def list_all(self) -> list[Student]:
        """Return a copy of all records."""
        return list(self.__records)

    def total_count(self) -> int:
        return len(self.__records)

    @staticmethod
    def display_results(results: list[Student]) -> None:
        """Static helper to pretty-print a list of search results."""
        if not results:
            print("  No results found.")
            return
        print(f"  Found {len(results)} record(s):")
        for s in results:
            print(f"    {s.get_summary()}")
