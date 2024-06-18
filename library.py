import sys,os


def Main(filename: str):
    print("Welcome to the library!")
    try:
        while True:
                choice = input(
                    "\nSelect option below: "
                    + "\n 1. Add new book"
                    + "\n 2. Show all books"
                    + "\n Q. Exit\n"
                )
                if choice.lower() == "q":
                    break
                elif int(choice) == 1:
                    print("Input book information: ")
                    book = input("Book name: ")
                    author = input("Author: ")
                    isbn = input("ISBN: ")
                    publ = input("Year published: ")
                    save = input("Save book (y/n): ")
                    if save.lower() == "y":
                        add_book(filename, book, author, isbn, publ)
                elif int(choice) == 2:
                    print("::::::: BOOKS :::::::")
                    fetch_books(filename)
                else:
                    print("\nIncorrect option. Try again! \n")
    except ValueError:
        print("Input number please!")

def add_book(filename: str, book: str, author: str, isbn: str, publish_year: str):
    with open(filename, mode="a+") as file:
        file.write(f"{book},{author},{isbn},{publish_year}\n")

def fetch_books(filename: str):
    try:
        if os.stat(filename).st_size == 0 :
            print("No books found!")
        else:
            books = []
            with open(filename, mode="r") as file:
                for book in file:
                    book = book.strip()
                    bookname, author, isbn, publish_year = book.split(sep=",")
                    books.append((bookname, author, isbn, publish_year))
            books.sort(key=lambda s: s[3], reverse=True)
            for book in books:
                print(" ".join(book))
    except  FileNotFoundError:
        print("No books found!")
        

if __name__ == "__main__":
    db_file = sys.argv[1]
    Main(db_file)
