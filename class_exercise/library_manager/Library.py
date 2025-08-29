#CLASS LIBRARY
class Library:
    def __init__(self):
        self.books = {}
    
    #ADD BOOK METHOD
    def add_book(self, *p_books):
        for l_book in p_books:
            self.books[l_book.code] = l_book
            print(f'Add new book in to a library!')
    #REMOVE BOOK METHOD
    def remove_book(self, p_book_code):
        self.books.pop(p_book_code)
        print(f'Removed {p_book_code} successfully!\n')
    #LOAN BOOK METHOD
    def loaned_book(self, p_user_name, p_book_code):
        for l_code, l_book in self.books.items():
            if l_code == p_book_code and l_book.state == 'Free':
                l_book.state = 'Loaned'
                p_user_name.books[l_code] = l_book
                print(f'Book {l_code} loaned!\n')
                return True
            else:
                return False
    #RETURN BOOK METHOD
    def returned_book(self, p_user_name, p_book_code):
        for l_code, l_book in self.books.items():
            if l_code == p_book_code and l_book.state == 'Loaned':
                l_book.state = 'Free'
                p_user_name.books.pop(l_code)
                print(f'Book {l_code} returned!\n')
                return True
            else:
                return False
            
    #DISPLAY LIBRARY BOOKS
    def display(self):
        print(f'Display all books:')
        for l_code, l_book in self.books.items():
            print(f'Code: {l_code}, Title: {l_book.title}, Author: {l_book.author}, Year: {l_book.year}, State: {l_book.state}\n')