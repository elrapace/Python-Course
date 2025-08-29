#CLASS USER
class User:
    def __init__(self, p_name):
        self.name = p_name
        self.books = {}

    #DISPLAY USER'S BOOKS
    def display(self):
        print(f'Users {self.name} books:')
        if len(self.books) == 0:
            print(f'Not books!\n')
        else:
            for l_code, l_book in self.books.items():
                print(f'Code: {l_code}, Title: {l_book.title}, Author: {l_book.author}, Year: {l_book.year}, State: {l_book.state}\n')
