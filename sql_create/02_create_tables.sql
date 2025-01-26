-- Create the authors table
CREATE TABLE authors (
    author_id TEXT PRIMARY KEY, -- Prefixed sequential ID as the primary key (e.g., AUTHOR_001)
    name TEXT NOT NULL,         -- Author's name (mandatory field)
    birth_year INTEGER,         -- Year of birth (optional)
    nationality TEXT            -- Nationality of the author (optional)
);

-- Create the books table
CREATE TABLE books (
    book_id TEXT PRIMARY KEY,   -- Prefixed sequential ID as the primary key (e.g., BOOK_001)
    title TEXT NOT NULL,        -- Book title (mandatory field)
    genre TEXT,                 -- Book genre (optional)
    publication_year INTEGER,   -- Year of publication (optional)
    author_id TEXT,             -- Foreign key linking to authors
    FOREIGN KEY (author_id) REFERENCES authors (author_id) -- Relationship with authors
);
