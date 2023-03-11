# 도서 관리 프로그램

class Book:
    def __init__(self, n, p, i):
        self.name = n
        self.price = p
        self.isbn = i


class BookRepository:
    def __init__(self):
        self.books = {}

    def registBook(self, book):
        # self.books.update({book.isbn: book})
        self.books[book.isbn] = book

    def removeBook(self, isbn):
        if isbn in self.books.keys():
            del self.books[isbn]
        else:
            print(f'존재하지 않는 책입니다.')

    def printBooksInfo(self):
        for isbn in self.books.keys():
            book = self.books[isbn]
            print(f'책 이름 : {book.name}')
            print(f'{book.name} 가격 : {book.price}')
            print(f'{book.name} isbn : {book.isbn}')

    def printBookInfo(self, isbn):
        if isbn in self.books.keys():
            book = self.books[isbn]
            print(f'책 이름 : {book.name}')
            print(f'{book.name} 가격 : {book.price}')
            print(f'{book.name} isbn : {book.isbn}')
        else:
            print(f'{isbn}이 존재하지 않습니다.')


books = BookRepository()

for i in range(3):
    name = input('책 이름 : ')
    price = input(f'{name} 가격 : ')
    isbn = input(f'{name} isbn : ')
    book = Book(name, price, isbn)
    books.registBook(book)

books.printBooksInfo()

print('-' * 30)
isbn = input('책의 정보 열람 :  ')
books.printBookInfo(isbn)
print('-' * 30)
isbn = input('삭제 할 책의 isbn :  ')
books.removeBook(isbn)
print('-' * 30)
books.printBooksInfo()
