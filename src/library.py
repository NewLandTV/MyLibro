from datetime import datetime
import index
import json
import path
from typing import List, Tuple

class Book:
    def __init__(self, index: str, title: str, author: str, added_date=None, num_read=0, is_borrowed=False):
        self.index = index
        self.title = title
        self.author = author
        self.added_date = added_date if added_date else datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.num_read = num_read
        self.is_borrowed = is_borrowed

class Library:
    def __init__(self):
        self.books: List[Book] = []

    def add_book(self, idx: str, title: str, author: str):
        if not index.find_korean_decimal_classification(idx):
            return
        self.books.append(Book(idx, title, author))
        print(f"[{idx}] '{title}' 도서가 등록되었습니다.")

    def show_books(self):
        for book in self.books:
            status = "대여중" if book.is_borrowed else "대여 가능"
            print(f"[{book.index}] 제목: {book.title}, 저자: {book.author}, 추가된 날짜: {book.added_date}, 회독: {book.num_read}회, 상태: {status}")

    def find_book_by_index(self, idx: str)-> Tuple[str | None, List[Book]]:
        find = []
        for book in self.books:
            if book.index == idx:
                find.append(book)
        return index.find_korean_decimal_classification(idx), find
    
    def find_book_by_title(self, title: str)-> List[Book]:
        find = []
        for book in self.books:
            if book.title == title:
                find.append(book)
        return find
    
    def save_data_to_local_file(self, filename="mylib.json"):
        data = []
        for book in self.books:
            data.append(book.__dict__)
        with open(path.join(path.data_dir, filename), "w", encoding="utf8") as f:
            json.dump(data, f, ensure_ascii=False)
        print("도서관 데이터를 로컬 파일에 저장했습니다.")

    def load_data_from_local_file(self, filename="mylib.json"):
        pth = path.join(path.data_dir, filename)
        if not path.exists(pth):
            print(f"'{filename}' 파일을 찾을 수 없어 도서관 데이터를 불러오지 못했습니다.")
            return
        
        with open(pth, "r", encoding="utf8") as f:
            data = json.load(f)
            self.books = []
            for book in data:
                self.books.append(Book(**book))
        print("도서관 데이터를 로컬 파일에서 불러왔습니다.")