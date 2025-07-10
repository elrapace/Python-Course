#CLASS EMPLOYEE
class Employee:
    def __init__(self, name, surname, number, salary):
        self.name = name
        self.surname = surname
        self.number = number
        self.salary = salary
    def aumenta_stipendio(self):
        aumento = (self.salary * 10) / 100
        self.salary = int(self.salary + aumento)
    def stampa_dettagli(self):
        print(f'Employee: {self.name} {self.surname}, matricola: {self.number}, salary: {self.salary} euro')

#ISTANZIA DELLE CLASSE
employee = Employee('Marco', 'Rossi', 12345, 3000)
employee.stampa_dettagli()
employee.aumenta_stipendio()
employee.stampa_dettagli()