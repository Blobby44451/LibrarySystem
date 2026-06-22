from database import get_connection
from datetime import date

def issue_loan(book_id, member_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT available FROM books WHERE id=?", (book_id,))
    book = cursor.fetchone()
    if not book:
        print("Book not found.")
        conn.close()
        return
    if book[0] == 0:
        print("Book is already on loan.")
        conn.close()
        return
    loan_date = str(date.today())
    cursor.execute("INSERT INTO loans (book_id, member_id, loan_date) VALUES (?, ?, ?)", (book_id, member_id, loan_date))
    cursor.execute("UPDATE books SET available=0 WHERE id=?", (book_id,))
    conn.commit()
    conn.close()
    print(f"Book ID {book_id} issued to Member ID {member_id}.")

def return_loan(loan_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT book_id, return_date FROM loans WHERE id=?", (loan_id,))
    loan = cursor.fetchone()
    if not loan:
        print("Loan not found.")
        conn.close()
        return
    if loan[1]:
        print("This loan is already returned.")
        conn.close()
        return
    return_date = str(date.today())
    cursor.execute("UPDATE loans SET return_date=? WHERE id=?", (return_date, loan_id))
    cursor.execute("UPDATE books SET available=1 WHERE id=?", (loan[0],))
    conn.commit()
    conn.close()
    print(f"Loan ID {loan_id} returned.")

def list_loans():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT loans.id, books.title, members.name, loans.loan_date, loans.return_date
        FROM loans
        JOIN books ON loans.book_id = books.id
        JOIN members ON loans.member_id = members.id
    """)
    loans = cursor.fetchall()
    conn.close()
    if not loans:
        print("No loans found.")
        return
    print("\n--- Loans ---")
    for l in loans:
        returned = l[4] if l[4] else "Not returned"
        print(f"[{l[0]}] '{l[1]}' → {l[2]} | Issued: {l[3]} | Returned: {returned}")