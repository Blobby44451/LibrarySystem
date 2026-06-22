from database import initialize_db
import books, members, loans

def main():
    initialize_db()

    while True:
        print("\n===== Library Management System =====")
        print("1. Books")
        print("2. Members")
        print("3. Loans")
        print("0. Exit")
        choice = input("Select: ")

        if choice == "1":
            print("\n1. List books\n2. Add book\n3. Update book\n4. Delete book")
            c = input("Select: ")
            if c == "1":
                books.list_books()
            elif c == "2":
                title = input("Title: ")
                author = input("Author: ")
                year = input("Year: ")
                books.add_book(title, author, int(year))
            elif c == "3":
                book_id = int(input("Book ID: "))
                title = input("New title: ")
                author = input("New author: ")
                year = int(input("New year: "))
                books.update_book(book_id, title, author, year)
            elif c == "4":
                book_id = int(input("Book ID: "))
                books.delete_book(book_id)

        elif choice == "2":
            print("\n1. List members\n2. Add member\n3. Update member\n4. Delete member")
            c = input("Select: ")
            if c == "1":
                members.list_members()
            elif c == "2":
                name = input("Name: ")
                email = input("Email: ")
                phone = input("Phone: ")
                members.add_member(name, email, phone)
            elif c == "3":
                member_id = int(input("Member ID: "))
                name = input("New name: ")
                email = input("New email: ")
                phone = input("New phone: ")
                members.update_member(member_id, name, email, phone)
            elif c == "4":
                member_id = int(input("Member ID: "))
                members.delete_member(member_id)

        elif choice == "3":
            print("\n1. List loans\n2. Issue loan\n3. Return loan")
            c = input("Select: ")
            if c == "1":
                loans.list_loans()
            elif c == "2":
                books.list_books()
                book_id = int(input("Book ID: "))
                members.list_members()
                member_id = int(input("Member ID: "))
                loans.issue_loan(book_id, member_id)
            elif c == "3":
                loans.list_loans()
                loan_id = int(input("Loan ID: "))
                loans.return_loan(loan_id)

        elif choice == "0":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()