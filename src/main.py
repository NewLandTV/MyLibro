from library import Library

def main():
    myLibro = Library()
    myLibro.add_book("004", "Test", "Dr. K")
    myLibro.show_books()
    myLibro.find_book_by_index("1234")
    
if __name__ == "__main__":
    main()