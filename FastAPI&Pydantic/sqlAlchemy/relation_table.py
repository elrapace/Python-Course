from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

# CLASSE AUTORE
class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # RELAZIONE UNO-A-MOLTI CON BOOK
    books = relationship("Book", back_populates="author")

# CLASSE BOOK
class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'))

    # RELAZIONE INVERSA
    author = relationship("Author", back_populates="books")

# Creiamo un autore
author = Author(name="J.K. Rowling")

# Creiamo due libri per questo autore
book1 = Book(title="Harry Potter and the Sorcerer's Stone", author=author)
book2 = Book(title="Harry Potter and the Chamber of Secrets", author=author)