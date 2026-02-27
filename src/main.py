import api
from library import Book, Library
import os
import sys
from typing import List

myLibro = Library()

def confirm(prompt: str) -> bool:
    while True:
        agree = input(f"{prompt} (y/n): ")
        if agree.upper() == "Y":
            return True
        elif agree.upper() == "N":
            return False

def show_command_list():
    print("=== 명령어 목록 ===")
    print("0. /help : 명령어 목록을 출력합니다.")
    print("1. /add : 새 책을 추가합니다.")
    print("2. /show : 도서관에 저장된 책을 보여줍니다.")
    print("3. /find : 특정 책을 찾습니다.")
    print("4. /save : 도서관 데이터를 저장합니다.")
    print("5. /load : 도서관 데이터를 불러옵니다.")
    print("6. /exit : 도서관 프로그램을 종료합니다. (저장 안 됨)")
    print("7. /cls : 화면을 지웁니다.")
    print("8. /read : 특정 도서의 회독 수를 변경합니다.")
    print("9. /api : 외부 프로그램에서 접근할 수 있도록 API 서버를 실행 여부를 설정합니다.")

def add():
    index = input("\t색인: ")
    title = input("\t도서명: ")
    author = input("\t저자: ")
    print(f"\t[{index}] 제목: {title}, 저자: {author}")

    if confirm("\t새 책으로 추가하시겠습니까?"):
        myLibro.add_book(index, title, author)
        
def find(show_result=True) -> List[Book] | None:
    """
    CLI 기반 도서 간단한 도서 검색 명령입니다.
    
    :param show_result: 결과를 화면에 보여줄지 여부입니다.
    :return: 찾은 도서 목록이 있으면 리스트로 반환하지만, 없으면 None을 반환합니다.
    :rtype: List[Book] | None
    """
    while True:
        print("\t검색 방법을 번호로 쓰시오.")
        print("\t1. 색인")
        print("\t2. 제목")
        print("\t3. 저자")
        method = input("\t번호 입력: ")

        if method.isdigit() and 1 <= int(method) <= 3:
            method = int(method)
            break

    books = []
    match method:
        case 1:
            idx = input("\t색인: ")
            books = myLibro.find_book_by_index(idx)
            if not books:
                print(f"\t[{idx}] 도서를 찾을 수 없습니다.")
            elif show_result:
                print(f"\t[{idx}] 찾은 도서: {len(books)}권")
                for book in books:
                    print(f"\t제목: {book.title}\n\t저자: {book.author}\n\t추가된 날짜: {book.added_date}\n\t회독: {book.num_read}회")
        case 2:
            title = input("\t도서명: ")
            books = myLibro.find_book_by_title(title)
            if not books:
                print(f"\t제목이 '{title}'인 도서를 찾을 수 없습니다.")
            elif show_result:
                print(f"\t제목이 '{title}'인 도서: {len(books)}권")
                for book in books:
                    print(f"\t제목: {book.title}\n\t저자: {book.author}\n\t추가된 날짜: {book.added_date}\n\t회독: {book.num_read}회")
        case 3:
            author = input("\t저자: ")  # TODO: 저자로 책 찾기
            books = myLibro.find_book_by_author(author)
            if not books:
                print(f"\t저자가 '{author}'인 도서을 찾을 수 없습니다.")
            elif show_result:
                print(f"\t저자가 '{author}'인 도서: {len(books)}권")
                for book in books:
                    print(f"\t제목: {book.title}\n\t저자: {book.author}\n\t추가된 날짜: {book.added_date}\n\t회독: {book.num_read}회")
    return books if books else None

def exit():
    if confirm("\t정말로 도서관 프로그램을 종료하시겠습니까?"):
        sys.exit(0)

def read():
    books = find(False)
    if not books:
        return
    
    for i in range(len(books)):
        print(f"\t{i + 1}. [{books[i].index}] 제목: '{books[i].title}', 저자: '{books[i].author}', 회독: {books[i].num_read}회")
    
    while True:
        number = input("\t회독 수를 수정할 검색된 도서 중 번호를 쓰시오: ")

        if number.isdigit() and 1 <= int(number) <= len(books):
            number = int(number) - 1
            break

    print(f"\t'[{books[number].index}] {books[number].title}', 선택한 도서의 현재 회독 수: {books[number].num_read}")

    while True:
        print("\t회독 수 수정 방법을 번호로 쓰시오.")
        print("\t1. 1회독 추가")
        print("\t2. 1회독 감소")
        print("\t3. N회독 추가")
        print("\t4. N회독 감소")
        print("\t5. N회독으로 설정")
        print("\t6. 초기화 (0회독으로 설정)")
        method = input("\t번호 입력: ")

        if method.isdigit() and 1 <= int(method) <= 6:
            method = int(method)
            break
        
    match method:
        case 1:
            books[number].num_read += 1
            print(f"\t회독 수를 1만큼 추가했습니다. (현재: {books[number].num_read}회독)")
        case 2:
            if books[number].num_read > 0:
                books[number].num_read -= 1
                print(f"\t회독 수를 1만큼 감소했습니다. (현재: {books[number].num_read}회독)")
            else:
                print(f"\t회독 수가 0이므로 감소할 수 없습니다.")
        case 3:
            while True:
                n = input("\t추가할 회독 수 입력(N은 자연수): ")

                if n.isdigit() and 1 <= int(n):
                    n = int(n)
                    break
            books[number].num_read += n
            print(f"\t회독 수를 {n}만큼 추가했습니다. (현재: {books[number].num_read}회독)")
        case 4:
            if books[number].num_read == 0:
                print(f"\t회독 수가 0이므로 감소할 수 없습니다.")
                return
            
            while True:
                n = input(f"\t감소할 회독 수 입력(N은 {books[number].num_read} 이하인 자연수): ")

                if n.isdigit() and 1 <= int(n) <= books[number].num_read:
                    n = int(n)
                    break
            books[number].num_read -= n
            print(f"\t회독 수를 {n}만큼 감소했습니다. (현재: {books[number].num_read}회독)")
        case 5:
            while True:
                n = input("\t설정할 회독 수 입력(N은 음이 아닌 정수): ")

                if n.isdigit() and 0 <= int(n):
                    n = int(n)
                    break
            books[number].num_read = n
            print(f"\t회독 수를 {n}(으)로 설정했습니다. (현재: {books[number].num_read}회독)")
        case 6:
            if confirm("\t정말로 회독 수를 초기화하시겠습니까? (되돌릴 수 없습니다.)"):
                books[number].num_read = 0

def main():
    try:
        myLibro.load_data_from_local_file()
        api_server_info = api.APIServerInfo()
        api_server_info.load()
        if api_server_info.use_api_server:
            api.run_api_server()
            
        while True:
            show_command_list()
            while True:
                cmd = input(">> ")
                if cmd == "/help":
                    show_command_list()
                elif cmd == "/add":
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
                    read()
                elif cmd == "/api":
                    api_server_info.use_api_server = not api_server_info.use_api_server
                    if api_server_info.use_api_server:
                        api.run_api_server()
                    else:
                        api.shutdown_api_server()
                    api_server_info.save()
    except KeyboardInterrupt:
        myLibro.save_data_to_local_file()
        if api_server_info.use_api_server:
            api.shutdown_api_server()
            api.close_api_server()
        print("'Ctrl + C' 감지, MyLibro 프로그램을 종료합니다.")
        sys.exit(0)
    
if __name__ == "__main__":
    main()