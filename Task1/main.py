"""
main.py
Entry point for the Student Record Search System.
Demonstrates the interaction between all modules and OOP concepts.
"""

from database import StudentDatabase
from student import Student, GradStudent


def populate_database(db: StudentDatabase) -> None:
    """Helper function to seed the database with sample records."""
    sample_students = [
        Student("S001", "Alice Wong", 21, "Computer Science", 3.8),
        Student("S002", "Bob Chan", 22, "Mathematics", 3.2),
        Student("S003", "Carol Lee", 20, "Computer Science", 3.5),
        Student("S004", "David Ng", 23, "Physics", 2.9),
        Student("S005", "Eva Lam", 21, "Mathematics", 3.7),
        GradStudent("S011", "Frank Ho", 26, "Computer Science", 3.9, "Machine Learning"),
        GradStudent("S012", "Grace Yip", 28, "Physics", 3.6, "Quantum Computing"),
    ]
    print("=== Populating Database ===")
    for s in sample_students:
        db.add_student(s)
    print(f"Total records: {db.total_count()}\n")


def demo_search(db: StudentDatabase) -> None:
    """Run several search demonstrations."""

    print("=== Search by ID ===")
    result = db.find_by_id("S001")
    print(f"  {result}\n" if result else "  Not found.\n")

    print("=== Search by Name (keyword: 'lee') ===")
    StudentDatabase.display_results(db.search_by_name("lee"))
    print()

    print("=== Search by Major: Computer Science ===")
    StudentDatabase.display_results(db.search_by_major("Computer Science"))
    print()

    print("=== Search by GPA range: 3.5 – 4.0 ===")
    StudentDatabase.display_results(db.search_by_gpa_range(3.5, 4.0))
    print()


def demo_polymorphism(db: StudentDatabase) -> None:
    """Show polymorphism: same method call, different output per class."""
    print("=== Polymorphism Demo (get_role) ===")
    for student in db.list_all():
        # get_role() behaves differently for Student vs GradStudent
        print(f"  {student.name:15s} → role: {student.get_role()}")
    print()


def main():
    db = StudentDatabase()
    populate_database(db)
    demo_search(db)
    demo_polymorphism(db)

    print("=== Remove a Record ===")
    db.remove_student("S002")
    print(f"  Records remaining: {db.total_count()}\n")


if __name__ == "__main__":
    main()
