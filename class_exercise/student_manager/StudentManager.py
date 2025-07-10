#CLASS STUDENT MANAGER
class StudentManager:
    def __init__(self):
        self.students = {}

    #ACCEPT / INSERT METHOD
    def accept(self, p_student):
        self.students[p_student.number] = p_student
        print(f'Insert new student! Matricola: {p_student.number}\n')
        return True

    #SEARCH METHOD
    def search(self, p_student_number):
        if p_student_number in self.students:
            #ACCEDO A QUELLO STUDENTE CHE HO TROVATO
            student = self.students[p_student_number]
            print(f'Student found!')
            print(f'Matricola: {student.number}, Name: {student.name}, Surname: {student.surname}, Age: {student.age}, Country: {student.country}\n')
            return student
        else:
            print(f'Student with matricola {p_student_number} not found!\n')
            return None

    #DELETE METHOD
    def delete(self, p_key_student):
        self.students.pop(p_key_student)
        #CONTROLLO CHE EFFETTIVAMENTE SIA STATO ELIMINATO
        l_student = self.search(p_key_student)
        if l_student:
            print(f'Student {p_key_student} not successfully elimnated\n') 
            return False
        else:
            print(f'Student {p_key_student} successfully elimnated\n') 
            return True
            

    #UPDATE METHOD
    def update_age(self, p_student_number, p_student_age):
        l_student = self.search(p_student_number)
        if l_student:
            l_student.age = p_student_age
            print(f'Update age! New age is: {l_student.age}\n')
            return True
        else:
            return False

    #DISPLAY METHOD
    def display(self):
        print(f'Display all student:')
        for key, student in self.students.items():
            print(f'Matricola: {key}, Name: {student.name}, Surname: {student.surname}, Age: {student.age}, Country: {student.country}\n')