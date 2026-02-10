import index

class Book:
    def __init__(self, index: str, title: str, author: str):
        self.index = index
        self.title = title
        self.author = author
        self.is_borrowed = False

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, index, title, author):
        self.books.append(Book(index, title, author))
        print(f"[{index}] '{title}' 도서가 등록되었습니다.")

    def show_books(self):
        for book in self.books:
            status = "대여중" if book.is_borrowed else "대여 가능"
            print(f"[{book.index}] 제목: {book.title}, 저자: {book.author}, 상태: {status}")

    def find_book_by_index(self, idx):
        return index.find_korean_decimal_classification(idx)