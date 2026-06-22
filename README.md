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