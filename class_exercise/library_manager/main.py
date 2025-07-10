#MAIN FILE

#IMPORT CLASS
from Book import Book
from Library import Library
from User import User

#INIZIALIZE BOOKS
g_book1 = Book(2345, "Libro1", "Alfonso", 2005, 'Free')
g_book2 = Book(2566, "Libro2", "Dario", 2010, 'Free')
g_book3 = Book(2334, "Libro3", "Andrea", 1890, 'Free')

#INIZIALIZE USRES
g_user1 = User('Alice')

#INIZIALIZE LIBRARY
g_library = Library()


#ADD BOOK IN LIBRARY
g_library.add_book(g_book1, g_book2, g_book3)
# g_library.add_book(g_book2)
# g_library.add_book(g_book3)

g_library.display()

#LOANED BOOKS
g_library.loaned_book(g_user1, 2345)
g_library.display()
g_user1.display()

#RETURNED BOOKS
g_library.returned_book(g_user1, 2345)
g_library.display()
g_user1.display()

#REMOVE BOOK
g_library.remove_book(2334)
g_library.display()