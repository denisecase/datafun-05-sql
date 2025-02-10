-- Query to count the number of books written by each author
SELECT a.name AS author_name, COUNT(b.book_id) AS book_count
FROM authors a
LEFT JOIN books b ON a.author_id = b.author_id
GROUP BY a.name
ORDER BY book_count DESC;
