import sqlite3
from database import get_connection

def add_book(title, author, year):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO books (title, author, year) VALUES (?, ?, ?)", (title, author, year))
    conn.commit()
    conn.close()
    print(f"Book '{title}' added.")

def list_books():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    conn.close()
    if not books:
        print("No books found.")
        return
    print("\n--- Books ---")
    for b in books:
        status = "Available" if b[4] == 1 else "On Loan"
        print(f"[{b[0]}] {b[1]} by {b[2]} ({b[3]}) — {status}")

def update_book(book_id, title, author, year):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE books SET title=?, author=?, year=? WHERE id=?", (title, author, year, book_id))
    conn.commit()
    conn.close()
    print(f"Book ID {book_id} updated.")

def delete_book(book_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id=?", (book_id,))
    conn.commit()
    conn.close()
    print(f"Book ID {book_id} deleted.")