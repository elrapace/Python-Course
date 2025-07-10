#CLASS PERSON
class Person:
    #CONSTRUCTOR
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    #METOD PRESENTATI
    def presentati(self):
        print(f'My name is: {self.name}, my age is: {self.age} and my sex is: {self.sex}')

#INSTANZA OBJECT
person = Person("Alice", "23", "Female")
person.presentati()