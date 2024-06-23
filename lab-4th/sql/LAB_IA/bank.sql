-- Create the BRANCH table
CREATE TABLE BRANCH (
    branch_name VARCHAR(25) PRIMARY KEY,
    branch_city VARCHAR(25),
    assets REAL
);

-- Create the ACCOUNT table
CREATE TABLE ACCOUNT (
    accno INT PRIMARY KEY,
    branch_name VARCHAR(25),
    balance REAL,
    FOREIGN KEY (branch_name) REFERENCES BRANCH(branch_name)
);

-- Create the DEPOSITOR table
CREATE TABLE DEPOSITOR (
    customer_name VARCHAR(25),
    accno INT,
    PRIMARY KEY (customer_name, accno),
    FOREIGN KEY (accno) REFERENCES ACCOUNT(accno)
);

-- Create the CUSTOMER table
CREATE TABLE CUSTOMER (
    customer_name VARCHAR(25) PRIMARY KEY,
    customer_street VARCHAR(25),
    customer_city VARCHAR(25)
);

-- Create the LOAN table
CREATE TABLE LOAN (
    Loan_number INT PRIMARY KEY,
    branch_name VARCHAR(25),
    amount REAL,
    FOREIGN KEY (branch_name) REFERENCES BRANCH(branch_name)
);

-- Create the BORROWER table
CREATE TABLE BORROWER (
    customer_name VARCHAR(25),
    Loan_number INT,
    PRIMARY KEY (customer_name, Loan_number),
    FOREIGN KEY (Loan_number) REFERENCES LOAN(Loan_number)
);



-- MariaDB [bank]> show tables;
-- +----------------+
-- | Tables_in_bank |
-- +----------------+
-- | select * from account;        |
-- | select * from borrower;       |
-- | select * from branch;         |
-- | select * from customer;       |
-- | select * from depositor;      |
-- | select * from loan;           |
-- +----------------+
-- 6 rows in set (0.001 sec)


-- MariaDB [bank]> select * from account;
-- +-------+-------------+---------+
-- | accno | branch_name | balance |
-- +-------+-------------+---------+
-- |     1 | Main        |   15000 |
-- |     2 | Downtown    |   20000 |
-- |     3 | Main        |   30000 |
-- |     4 | Uptown      |    5000 |
-- +-------+-------------+---------+
-- 4 rows in set (0.001 sec)

-- MariaDB [bank]> select * from borrower;
-- +---------------+-------------+
-- | customer_name | Loan_number |
-- +---------------+-------------+
-- | Customer 1    |         102 |
-- | Customer 2    |         101 |
-- | Customer 3    |         103 |
-- +---------------+-------------+
-- 3 rows in set (0.002 sec)

-- MariaDB [bank]> select * from branch;
-- +-------------+-------------+---------+
-- | branch_name | branch_city | assets  |
-- +-------------+-------------+---------+
-- | Downtown    | City A      |  800000 |
-- | Main        | City A      | 1000000 |
-- | Uptown      | City B      | 1200000 |
-- +-------------+-------------+---------+
-- 3 rows in set (0.001 sec)

-- MariaDB [bank]> select * from customer;
-- +---------------+-----------------+---------------+
-- | customer_name | customer_street | customer_city |
-- +---------------+-----------------+---------------+
-- | Customer 1    | Street X        | City A        |
-- | Customer 2    | Street Y        | City A        |
-- | Customer 3    | Street Z        | City B        |
-- +---------------+-----------------+---------------+
-- 3 rows in set (0.001 sec)

-- MariaDB [bank]> select * from depositor;
-- +---------------+-------+
-- | customer_name | accno |
-- +---------------+-------+
-- | Customer 1    |     1 |
-- | Customer 1    |     2 |
-- | Customer 2    |     3 |
-- | Customer 3    |     4 |
-- +---------------+-------+
-- 4 rows in set (0.001 sec)

-- MariaDB [bank]> select * from loan;
-- +-------------+-------------+--------+
-- | Loan_number | branch_name | amount |
-- +-------------+-------------+--------+
-- |         101 | Main        |  20000 |
-- |         102 | Downtown    |  30000 |
-- |         103 | Main        |  40000 |
-- +-------------+-------------+--------+
-- 3 rows in set (0.001 sec)

-- Write the following queries in SQL.
-- 1. Find all the customers who have at least two accounts at the main branch.
 SELECT DISTINCT d.customer_name
    FROM DEPOSITOR d, ACCOUNT a
    WHERE d.accno = a.accno AND a.branch_name = 'main'
    GROUP BY d.customer_name
    HAVING COUNT(d.accno) >= 2;
-- +---------------+
-- | customer_name |
-- +---------------+
-- | Customer 1    |
-- +---------------+
-- 1 row in set (0.001 sec)

-- 2. Demonstrate how you delete all account tuples at every branch located in a specific city.

-- MariaDB [bank]> select * from account;
-- +-------+-------------+---------+
-- | accno | branch_name | balance |
-- +-------+-------------+---------+
-- |     1 | Main        |   15000 |
-- |     2 | Downtown    |   20000 |
-- |     3 | Main        |   30000 |
-- |     4 | Uptown      |    5000 |
-- |     5 | Main        |    1000 |
-- |     6 | Main        |    2000 |
-- |     7 | Deltown     |    3000 |
-- |     8 | Deltown     |    3000 |
-- +-------+-------------+---------+
-- 8 rows in set (0.001 sec)

-- MariaDB [bank]> select * from branch;
-- +-------------+-------------+---------+
-- | branch_name | branch_city | assets  |
-- +-------------+-------------+---------+
-- | Deltown     | City C      |   12000 |
-- | Downtown    | City A      |  800000 |
-- | Main        | City A      | 1000000 |
-- | Uptown      | City B      | 1200000 |
-- +-------------+-------------+---------+
-- 4 rows in set (0.002 sec)

-- MariaDB [bank]> Delete from account where branch_name in (Select branch_name from branch where branch_city = "City C");
-- Query OK, 2 rows affected (0.006 sec)

-- MariaDB [bank]> select * from account;
-- +-------+-------------+---------+
-- | accno | branch_name | balance |
-- +-------+-------------+---------+
-- |     1 | Main        |   15000 |
-- |     2 | Downtown    |   20000 |
-- |     3 | Main        |   30000 |
-- |     4 | Uptown      |    5000 |
-- |     5 | Main        |    1000 |
-- |     6 | Main        |    2000 |
-- +-------+-------------+---------+
-- 6 rows in set (0.001 sec)

-- 3. Find the bank that has having highest average balance.
SELECT b.branch_name
 FROM BRANCH b
 WHERE b.assets = (
     SELECT MAX(assets)
     FROM BRANCH
 );
-- +-------------+
-- | branch_name |
-- +-------------+
-- | Uptown      |
-- +-------------+
-- 1 row in set (0.001 sec)

SELECT branch_name
FROM ACCOUNT
GROUP BY branch_name
HAVING AVG(balance) = (
    SELECT MAX(avg_balance)
    FROM (
        SELECT branch_name, AVG(balance) AS avg_balance
        FROM ACCOUNT
        GROUP BY branch_name
    ) AS branch_avg
);
-- +-------------+
-- | branch_name |
-- +-------------+
-- | Downtown    |
-- +-------------+
-- 1 row in set (0.001 sec)


-- 4. Find all the customers who have both account and loan at specific branch