"""
student.py
Defines the Student and GradStudent classes and demonstrates:
- Inheritance  (GradStudent extends Student)
- Polymorphism (overriding get_role, get_summary, __str__)
- Encapsulation (private attributes)
"""

from person import Person


class Student(Person):
    """Represents an undergraduate student."""

    def __init__(self, student_id: str, name: str, age: int, major: str, gpa: float):
        super().__init__(name, age)
        self.__student_id = student_id
        self.__major = major
        self.__gpa = gpa

    # --- Getters ---
    @property
    def student_id(self) -> str:
        return self.__student_id

    @property
    def major(self) -> str:
        return self.__major

    @property
    def gpa(self) -> float:
        return self.__gpa

    @gpa.setter
    def gpa(self, value: float):
        if not (0.0 <= value <= 4.0):
            raise ValueError("GPA must be between 0.0 and 4.0.")
        self.__gpa = value

    # --- Polymorphism: override abstract methods ---
    def get_role(self) -> str:
        return "Undergraduate"

    def get_summary(self) -> str:
        return (f"ID: {self.student_id} | Name: {self.name} | "
                f"Major: {self.major} | GPA: {self.gpa:.2f}")

    def __str__(self) -> str:
        # Polymorphism: overrides Person.__str__
        return (f"[{self.get_role()}] {self.name} (ID: {self.student_id}) "
                f"| Major: {self.major} | GPA: {self.gpa:.2f}")


class GradStudent(Student):
    """
    Represents a graduate student.
    Inherits from Student and extends it with a research topic.
    Demonstrates multi-level inheritance.
    """

    def __init__(self, student_id: str, name: str, age: int,
                 major: str, gpa: float, research_topic: str):
        super().__init__(student_id, name, age, major, gpa)
        self.__research_topic = research_topic

    @property
    def research_topic(self) -> str:
        return self.__research_topic

    # --- Polymorphism: override again for GradStudent ---
    def get_role(self) -> str:
        return "Graduate"

    def get_summary(self) -> str:
        base = super().get_summary()
        return f"{base} | Research: {self.research_topic}"

    def __str__(self) -> str:
        return (f"[{self.get_role()}] {self.name} (ID: {self.student_id}) "
                f"| Major: {self.major} | GPA: {self.gpa:.2f} "
                f"| Research: {self.research_topic}")
