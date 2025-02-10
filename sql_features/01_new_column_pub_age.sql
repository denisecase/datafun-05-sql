-- Add a new column to the books table to store the author's age at the time of publication 
ALTER TABLE books ADD COLUMN author_age_at_publication INT;

-- Update the author_age_at_publication column in the books table
-- NOTE: You might need to refresh the database to see results in the books table
UPDATE books
SET author_age_at_publication = (
    SELECT publication_year - birth_year
    FROM authors
    WHERE authors.author_id = books.author_id
);
