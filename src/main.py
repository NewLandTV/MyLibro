from library import Library
import os
import sys

myLibro = Library()

def show_command_list():
    print("=== 명령어 목록 ===")
    print("1. /add : 새 책을 추가합니다.")
    print("2. /show : 도서관에 저장된 책을 보여줍니다.")
    print("3. /find : 특정 책을 찾습니다.")
    print("4. /save : 도서관 데이터를 저장합니다.")
    print("5. /load : 도서관 데이터를 불러옵니다.")
    print("6. /exit : 도서관 프로그램을 종료합니다. (저장 안 됨)")
    print("7. /cls : 화면을 지웁니다.")

def add():
    index = input("\t색인: ")
    title = input("\t도서명: ")
    author = input("\t저자: ")
    print(f"\t[{index}] 제목: {title}, 저자: {author}")

    while True:
        agree = input("\t새 책으로 추가하시겠습니까? (y/n): ")
        if agree.upper() == "Y":
            myLibro.add_book(index, title, author)
            return
        elif agree.upper() == "N":
            return
        
def find():
    while True:
        print("\t검색 방법을 번호로 쓰시오.")
        print("\t1. 색인")
        print("\t2. 제목")
        print("\t3. 저자")
        method = input("\t번호 입력: ")

        if method.isdigit() and 1 <= int(method) <= 3:
            method = int(method)
            break

    match method:
        case 1:
            index = input("\t색인: ")
            index, books = myLibro.find_book_by_index(index)
            if index and books:
                print(f"\t[{index}] 찾은 도서 {len(books)}권")
                for book in books:
                    print(f"\t제목: {book.title}\n\t저자: {book.author}\n\t추가된 날짜: {book.added_date}\n\t회독: {book.num_read}회")
        case 2:
            title = input("\t도서명: ")
            books = myLibro.find_book_by_title(title)
            if not books:
                print(f"\t'{title}' 책을 찾을 수 없습니다.")
            else:
                print(f"\t'{title}' 찾은 도서 {len(books)}권")
                for book in books:
                    print(f"\t제목: {book.title}\n\t저자: {book.author}\n\t추가된 날짜: {book.added_date}\n\t회독: {book.num_read}회")
        case 3:
            author = input("\t저자: ")  # TODO: 저자로 책 찾기

def exit():
    while True:
        agree = input("\t정말로 도서관 프로그램을 종료하시겠습니까? (y/n): ")
        if agree.upper() == "Y":
            sys.exit(0)
        elif agree.upper() == "N":
            return

def main():
    try:
        myLibro.load_data_from_local_file()

        while True:
            show_command_list()

            while True:
                cmd = input(">> ")
                if cmd == "/add":
                    add()
                elif cmd == "/show":
                    myLibro.show_books()
                elif cmd == "/find":
                    find()
                elif cmd == "/save":
                    myLibro.save_data_to_local_file()
                elif cmd == "/load":
                    myLibro.load_data_from_local_file()
                elif cmd == "/exit":
                    exit()
                elif cmd == "/cls":
                    os.system("cls")
                elif cmd == "/read":
                    os.system("cls")
    except KeyboardInterrupt:
        myLibro.save_data_to_local_file()
        print("'Ctrl + C' 감지, MyLibro 프로그램을 종료합니다.")
        sys.exit(0)
    
if __name__ == "__main__":
    main()