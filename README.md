# LibrarySystem

A command-line library management system built with Python and SQLite.

## Features
- Add, list, update, and delete books
- Add, list, update, and delete members
- Issue and return book loans
- All data stored in SQLite database

## Project Structure
- database.py — database connection and initialization
- books.py — CRUD operations for books
- members.py — CRUD operations for members
- loans.py — CRUD operations for loans
- main.py — CLI menu and entry point
- schema.sql — database schema and sample data
- tests.py — automated test cases

## How to Run
1. Make sure Python is installed
2. Clone the repository
3. Run the program: python main.py

## How to Run Tests
python tests.py

## Database Schema
- books - id, title, author, year, available
- members - id, name, email, phone
- loans - id, book_id, member_id, loan_date, return_date

## How I Developed This Project

I started by designing the database schema — three tables: books, members, and loans. After that I wrote the database connection module, then CRUD functions for each entity in separate files, and finally the CLI menu in main.py. At the end I wrote automated tests to verify everything works correctly.

Development process: database design → backend modules → CLI interface → testing → GitHub.

## Challenging Parts

- When restarting the program, it crashed with a UNIQUE constraint error because sample data was inserted again on every launch. Fixed by using INSERT OR IGNORE in schema.sql.
- Git refused to commit because Visual Studio was locking its own service files in the .vs/ folder. Fixed by creating a .gitignore file.

## What I Learned

- How to structure a Python project across multiple modules
- How to connect Python to SQLite and perform CRUD operations
- How relational tables and foreign keys work in practice
- How to use Git and GitHub with meaningful commits
- How to write basic automated tests