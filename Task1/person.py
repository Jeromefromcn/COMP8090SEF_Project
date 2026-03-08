"""
person.py
Defines the abstract base class Person and demonstrates:
- Abstraction (abstract methods via property)
- Encapsulation (private attributes with getters/setters)
"""

from abc import ABC, abstractmethod


class Person(ABC):
    """Abstract base class representing a person."""

    def __init__(self, name: str, age: int):
        # Encapsulation: private attributes
        self.__name = name
        self.__age = age

    # --- Getters and Setters (Encapsulation) ---
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value.strip():
            raise ValueError("Name cannot be empty.")
        self.__name = value.strip()

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, value: int):
        if value < 0 or value > 150:
            raise ValueError("Age must be between 0 and 150.")
        self.__age = value

    # --- Abstraction: subclasses must implement this ---
    @abstractmethod
    def get_role(self) -> str:
        """Return the role of this person (e.g. 'Student', 'Graduate Student')."""
        pass

    @abstractmethod
    def get_summary(self) -> str:
        """Return a one-line summary of this person."""
        pass

    def __str__(self) -> str:
        return f"[{self.get_role()}] {self.name}, Age: {self.age}"
