#!/usr/bin/python3

class Person:

    Current_year = 2025

    def __init__(self,name,country, date_birth):
        self.name = name
        self.country = country
        self.date_birth = date_birth

    def Calculate_age(self):
        age = Person.Current_year - self.date_birth
        return age
Person1 = Person("Adam", "USA", 1995)
Person2 = Person("Barthez" , "RWANDA", 1992)

Age1 = Person1.Calculate_age()
Age2 = Person2.Calculate_age()

print(f"Age of {Person1.name} is {Age1}")
print(f"Age of {Person2.name} is {Age2}")
print(Person.__doc__)
print(Person.__dict__)
print(Person.__name__)
print(Person.__module__)
print(Person.__bases__ )


