-- Create the CATEGORY table
CREATE TABLE CATEGORY (
    category_id INT PRIMARY KEY,
    description VARCHAR(25)
);

-- Create the AUTHOR table
CREATE TABLE AUTHOR (
    author_id INT PRIMARY KEY,
    name VARCHAR(25),
    city VARCHAR(25),
    country VARCHAR(25)
);

-- Create the PUBLISHER table
CREATE TABLE PUBLISHER (
    publisher_id INT PRIMARY KEY,
    name VARCHAR(25),
    city VARCHAR(25),
    country VARCHAR(25)
);

-- Create the CATALOG table
CREATE TABLE CATALOG (
    book_id INT PRIMARY KEY,
    title VARCHAR(25),
    author_id INT,
    publisher_id INT,
    category_id INT,
    year INT,
    price INT,
    FOREIGN KEY (author_id) REFERENCES AUTHOR(author_id),
    FOREIGN KEY (publisher_id) REFERENCES PUBLISHER(publisher_id),
    FOREIGN KEY (category_id) REFERENCES CATEGORY(category_id)
);

-- Create the ORDER_DETAILS table
CREATE TABLE ORDER_DETAILS (
    order_no INT,
    book_id INT,
    quantity INT,
    PRIMARY KEY (order_no, book_id),
    FOREIGN KEY (book_id) REFERENCES CATALOG(book_id)
);
-- MariaDB [book]> show tables;
-- +----------------+
-- | Tables_in_book |
-- +----------------+
-- | select * from author;          |
-- | select * from catalog;         |
-- | select * from category;        |
-- | select * from order_details;   |
-- | select * from publisher;       |
-- +----------------+
-- 5 rows in set (0.001 sec)


-- MariaDB [book]> select * from author;
-- +-----------+----------+--------+-----------+
-- | author_id | name     | city   | country   |
-- +-----------+----------+--------+-----------+
-- |         1 | Author 1 | City A | Country A |
-- |         2 | Author 2 | City B | Country B |
-- |         3 | Author 3 | City C | Country C |
-- +-----------+----------+--------+-----------+
-- 3 rows in set (0.001 sec)

-- MariaDB [book]> select * from catalog;
-- +---------+--------+-----------+--------------+-------------+------+-------+
-- | book_id | title  | author_id | publisher_id | category_id | year | price |
-- +---------+--------+-----------+--------------+-------------+------+-------+
-- |       1 | Book 1 |         1 |            1 |           1 | 2020 |   100 |
-- |       2 | Book 2 |         2 |            2 |           2 | 2018 |   150 |
-- |       3 | Book 3 |         3 |            1 |           1 | 2021 |   120 |
-- |       4 | Book 4 |         1 |            3 |           3 | 2019 |    90 |
-- |       5 | Book 5 |         2 |            2 |           4 | 2022 |   110 |
-- +---------+--------+-----------+--------------+-------------+------+-------+
-- 5 rows in set (0.001 sec)

-- MariaDB [book]> select * from category;
-- +-------------+-----------------+
-- | category_id | description     |
-- +-------------+-----------------+
-- |           1 | Fiction         |
-- |           2 | Science Fiction |
-- |           3 | Mystery         |
-- |           4 | Romance         |
-- +-------------+-----------------+
-- 4 rows in set (0.001 sec)

-- MariaDB [book]> select * from order_details;
-- +----------+---------+----------+
-- | order_no | book_id | quantity |
-- +----------+---------+----------+
-- |      101 |       1 |        5 |
-- |      102 |       2 |        8 |
-- |      103 |       3 |        3 |
-- |      104 |       4 |        6 |
-- |      105 |       5 |       10 |
-- +----------+---------+----------+
-- 5 rows in set (0.001 sec)

-- MariaDB [book]> select * from publisher;
-- +--------------+-------------+--------+-----------+
-- | publisher_id | name        | city   | country   |
-- +--------------+-------------+--------+-----------+
-- |            1 | Publisher 1 | City A | Country A |
-- |            2 | Publisher 2 | City B | Country B |
-- |            3 | Publisher 3 | City C | Country C |
-- +--------------+-------------+--------+-----------+
-- 3 rows in set (0.001 sec)


-- Write the following queries in SQL.
-- 1. Find the publisher id who have not published any books.

SELECT publisher_id
    -> FROM PUBLISHER
    -> WHERE publisher_id NOT IN (
    ->     SELECT DISTINCT publisher_id
    ->     FROM CATALOG
    -> );
-- +--------------+
-- | publisher_id |
-- +--------------+
-- |            4 |
-- +--------------+
-- 1 row in set (0.001 sec)


-- 2. Find the author of the book which has maximum sales.
SELECT name
    -> FROM AUTHOR
    -> WHERE author_id = (
    ->     SELECT author_id
    ->     FROM CATALOG
    ->     WHERE book_id = (
    ->         SELECT book_id
    ->         FROM ORDER_DETAILS
    ->         GROUP BY book_id
    ->         ORDER BY SUM(quantity) DESC
    ->         LIMIT 1
    ->     )
    -> );
-- +----------+
-- | name     |
-- +----------+
-- | Author 2 |
-- +----------+
-- 1 row in set (0.001 sec) 

-- 3. Demonstrate how you increase the price of books published by a specific publisher by 
-- 10%.
> UPDATE CATALOG
    -> SET price = price * 1.1
    -> WHERE publisher_id = 1;
-- Query OK, 2 rows affected (0.010 sec)
-- Rows matched: 2  Changed: 2  Warnings: 0

-- MariaDB [book]> select * from catalog;
-- +---------+--------+-----------+--------------+-------------+------+-------+
-- | book_id | title  | author_id | publisher_id | category_id | year | price |
-- +---------+--------+-----------+--------------+-------------+------+-------+
-- |       1 | Book 1 |         1 |            1 |           1 | 2020 |   110 |
-- |       2 | Book 2 |         2 |            2 |           2 | 2018 |   150 |
-- |       3 | Book 3 |         3 |            1 |           1 | 2021 |   132 |
-- |       4 | Book 4 |         1 |            3 |           3 | 2019 |    90 |
-- |       5 | Book 5 |         2 |            2 |           4 | 2022 |   110 |
-- +---------+--------+-----------+--------------+-------------+------+-------+
-- 5 rows in set (0.001 sec)


-- 4. Find the author name and publisher name who live in the same city.
SELECT a.name AS author_name, p.name AS publisher_name
    -> FROM AUTHOR a, PUBLISHER p
    -> WHERE a.city = p.city AND a.country = p.country;
-- +-------------+----------------+
-- | author_name | publisher_name |
-- +-------------+----------------+
-- | Author 1    | Publisher 1    |
-- | Author 2    | Publisher 2    |
-- | Author 3    | Publisher 3    |
-- | Author 1    | Publisher 4    |
-- +-------------+----------------+
-- 4 rows in set (0.001 sec)

-- 5. Find the publisher name who have published at least 4 books.

 SELECT P.name AS publisher_name
 FROM PUBLISHER P, CATALOG c
 WHERE P.publisher_id = C.publisher_id
 GROUP BY P.publisher_id, P.name
 HAVING COUNT(C.book_id) >= 4;
-- +----------------+
-- | publisher_name |
-- +----------------+
-- | Publisher 1    |
-- +----------------+
-- 1 row in set (0.033 sec)
