from library import Library
import sys

def main():
    try:
        myLibro = Library()
        myLibro.add_book("004", "Test", "Dr. K")
        myLibro.show_books()
        myLibro.find_book_by_index("1234")
        while True:
            pass
    except KeyboardInterrupt:
        print("'Ctrl + C' 감지, MyLibro 프로그램을 종료합니다.")
        sys.exit(0)
    
if __name__ == "__main__":
    main()