from Student import Student
from StudentManager import StudentManager

#ISTANZIO GLI STUDENTI DA INSERIRE
g_student1 = Student('Alice', 'Rossi', 6554, 22, 'Italy')
g_student2 = Student('Emanuel', 'Roja', 6789, 23, 'Spain')
g_student3 = Student('Rodrigo', 'De Paul', 9988, 25, 'Argentina')

#ISTANZIO IL STUDENT MANAGER E INSERISCO GLI STUDENTI
g_student_manager = StudentManager()
g_student_manager.accept(g_student1)
g_student_manager.accept(g_student2)
g_student_manager.accept(g_student3)
g_student_manager.display()

#SEARCH STUDENT
g_student_manager.search(6554)
g_student_manager.search(7887)

#UPDATE AGE
g_student_manager.update_age(6554, 23)
g_student_manager.display()

#DELETE STUDENT
g_student_manager.delete(9988)
g_student_manager.display()
