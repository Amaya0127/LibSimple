class Book:
    def __init__(self, title, author, publisher, category, isbn):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.category = category
        self.isbn = isbn
    
    def info(self):
        print("---도서 정보---")
        print("책 제목: " + self.title)
        print("저자: " + self.author)
        print("출판사: " + self.publisher)
        print("카테고리: " + self.category)
        print("ISBN: " + self.isbn + "\n")

class Bookmanager:
    def __init__(self):
        self.booklist = []

    def add_book(self, book):
        self.booklist.append(book)
        print("도서가 추가되었습니다.")

    def view_books(self):
        for book in self.booklist:
            book.info()

    def remove_book(self, isbn):
        for book in self.booklist:
            if book.isbn == isbn:
                self.booklist.remove(book)
                print("도서가 삭제되었습니다.")
                return
        print("해당하는 도서가 없습니다.")
        
book = Book
manager = Bookmanager()

while True:
    print("---도서관리 시스템에 오신 것을 환영합니다---")
    print("1. 도서 목록 보기")
    print("2. 도서 추가")
    print("3. 도서 삭제")
    print("4. 종료")

    menu = input()

    if menu == "1":
        manager.view_books()

    elif menu == "2":
        title = input("제목을 입력하세요: ")
        author = input("저자를 입력하세요: ")
        publisher = input("출판사를 입력하세요: ")
        category = input("카테고리를 입력하세요: ")
        isbn = input("ISBN을 입력하세요: ")
        b1 = book(title, author, publisher, category, isbn)
        manager.add_book(b1)

    elif menu == "3":
        isbn = input("삭제할 도서의 ISBN을 입력하세요: ")
        manager.remove_book(isbn)

    elif menu == "4":
        print("도서관리 시스템을 종료합니다.")
        break

    else:
        print("올바른 번호를 입력하세요.")