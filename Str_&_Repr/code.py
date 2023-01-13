class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # magic method to turn object into string representation
    # def __str__(self):
    #     return f"Person {self.name}, {self.age} years old"

    # unambiguous representation original object
    # str method is more common 
    def __repr__(self):
        return f"<Person('{self.name}', {self.age})>"



bob = Person("Bob", 35)
print(bob)