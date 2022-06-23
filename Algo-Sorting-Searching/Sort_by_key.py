import operator
from unicodedata import name


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        pass

    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age

    def __lt__(self, other):    # Default less then behavior: Operator overriding
        return self.age < other.age

    def __repr__(self) -> str:
        return f'{self.name} {self.age}'


class SortSolution:
    def sortPersonsByAge(self, persons: list) -> list:
        return sorted(persons, key=self.byAge)

    def byAge(self, person: Person):
        return person.age
        

persons = ([Person("Jigar", 37), Person("Krupa", 38), Person("Parshvi", 4), Person("Nency", 24)])
sortSolution = SortSolution()
print(sortSolution.sortPersonsByAge(persons))