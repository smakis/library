import sys


def Main(filename: str):
    print("Welcome to the library!")
    while True:
        choice = input(
            "Select option below: "
            + "\n 1. Add new book: "
            + "\n 2. Show all books: "
            + "\n Q. Exit: "
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
            if save.lower == "y":
                add_book(filename, book, author, isbn, publ)
        elif int(choice) == 2:
            fetch_books()
        else:
            print("\nIncorrect option. Try again! \n")


def add_book(filename: str, book: str, author: str, isbn: str, publish_year: str):
    with open(filename, mode="a+") as file:
        file.write(f"{book},{author}, {isbn}, {publish_year}")


def fetch_books(filename: str):
    pass


if __name__ == "__main__":
    db_file = sys.argv[1]
    Main(db_file)
