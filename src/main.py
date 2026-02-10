from library import Library
import sys

myLibro = Library()

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

def main():
    try:
        myLibro.load_data_from_local_file()

        while True:
            print("=== 명령어 목록 ===")
            print("1. /add : 새 책을 추가합니다.")
            print("2. /show : 도서관에 저장된 책을 보여줍니다.")
            print("3. /find : 특정 책을 찾습니다.")
            print("4. /save : 도서관 데이터를 저장합니다.")
            print("5. /load : 도서관 데이터를 불러옵니다.")
            print("6. /exit : 도서관 프로그램을 종료합니다.")
            cmd = input(">> ")

            if cmd == "/add":
                add()
            elif cmd == "/show":
                myLibro.show_books()
            elif cmd == "/find":
                myLibro.find_book_by_index("1234")  # TODO: find book by index or title...
            elif cmd == "/save":
                myLibro.save_data_to_local_file()
            elif cmd == "/load":
                myLibro.load_data_from_local_file()
            elif cmd == "/exit":
                break
            
            input()
    except KeyboardInterrupt:
        myLibro.save_data_to_local_file()
        print("'Ctrl + C' 감지, MyLibro 프로그램을 종료합니다.")
        sys.exit(0)
    
if __name__ == "__main__":
    main()