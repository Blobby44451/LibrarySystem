from database import initialize_db
import books, members, loans
import sqlite3
import os

DB_NAME = "library.db"

def reset_db():
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)
    initialize_db()

def test_add_and_list_books():
    reset_db()
    books.add_book("Test Book", "Test Author", 2020)
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books WHERE title='Test Book'")
    result = cursor.fetchone()
    conn.close()
    assert result is not None, "FAIL: Book not added"
    print("PASS: test_add_and_list_books")

def test_add_and_list_members():
    reset_db()
    members.add_member("Test User", "test@email.com", "123")
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM members WHERE email='test@email.com'")
    result = cursor.fetchone()
    conn.close()
    assert result is not None, "FAIL: Member not added"
    print("PASS: test_add_and_list_members")

def test_issue_and_return_loan():
    reset_db()
    books.add_book("Loan Book", "Author", 2021)
    members.add_member("Loan User", "loan@email.com", "456")
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM books WHERE title='Loan Book'")
    book_id = cursor.fetchone()[0]
    cursor.execute("SELECT id FROM members WHERE email='loan@email.com'")
    member_id = cursor.fetchone()[0]
    conn.close()
    loans.issue_loan(book_id, member_id)
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM loans WHERE book_id=? AND member_id=?", (book_id, member_id))
    loan = cursor.fetchone()
    conn.close()
    assert loan is not None, "FAIL: Loan not created"
    loans.return_loan(loan[0])
    print("PASS: test_issue_and_return_loan")

def test_delete_book():
    reset_db()
    books.add_book("Delete Me", "Author", 2000)
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM books WHERE title='Delete Me'")
    book_id = cursor.fetchone()[0]
    conn.close()
    books.delete_book(book_id)
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books WHERE id=?", (book_id,))
    result = cursor.fetchone()
    conn.close()
    assert result is None, "FAIL: Book not deleted"
    print("PASS: test_delete_book")

if __name__ == "__main__":
    print("\n--- Running Tests ---")
    test_add_and_list_books()
    test_add_and_list_members()
    test_issue_and_return_loan()
    test_delete_book()
    print("--- All tests passed ---")