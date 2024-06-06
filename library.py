import sys


def Main(filename: str):
    print("Welcome to the library!")
    while True:
        try:
            choice = input(
                "Select option below: "
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
                    print('hey')
                    add_book(filename, book, author, isbn, publ)
            elif int(choice) == 2:
                print("::::::: BOOKS :::::::")
                fetch_books(filename)
            else:
                print("\nIncorrect option. Try again! \n")
        except ValueError as err:
            print("\nIncorrect option. Try again! \n")


def add_book(filename: str, book: str, author: str, isbn: str, publish_year: str):
    with open(filename, mode="a+") as file:
        file.write(f"{book} {author} {isbn} {publish_year}\n")


def fetch_books(filename: str):
    with open(filename, mode="r") as file:
        for line in file.readlines():
            print(line)


if __name__ == "__main__":
    db_file = sys.argv[1]
    Main(db_file)
