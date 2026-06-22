CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    year INTEGER,
    available INTEGER DEFAULT 1
);

CREATE TABLE IF NOT EXISTS members (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone TEXT
);

CREATE TABLE IF NOT EXISTS loans (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER NOT NULL,
    member_id INTEGER NOT NULL,
    loan_date TEXT NOT NULL,
    return_date TEXT,
    FOREIGN KEY (book_id) REFERENCES books(id),
    FOREIGN KEY (member_id) REFERENCES members(id)
);

INSERT OR IGNORE INTO books (title, author, year) VALUES
    ('The Great Gatsby', 'F. Scott Fitzgerald', 1925),
    ('1984', 'George Orwell', 1949),
    ('To Kill a Mockingbird', 'Harper Lee', 1960);

INSERT OR IGNORE INTO members (name, email, phone) VALUES
    ('Alice Johnson', 'alice@email.com', '555-1234'),
    ('Bob Smith', 'bob@email.com', '555-5678');