-- Create the FLIGHTS table
CREATE TABLE FLIGHTS (
    no INTEGER PRIMARY KEY,
    fromPlace VARCHAR(25),
    toPlace VARCHAR(25),
    distance INTEGER,
    Departs DATE,
    arrives DATE,
    price REAL
);

-- Create the AIRCRAFT table
CREATE TABLE AIRCRAFT (
    aid INTEGER PRIMARY KEY,
    aname VARCHAR(25),
    cruisingrange INTEGER
);

-- Create the EMPLOYEES table
CREATE TABLE EMPLOYEES (
    eid INTEGER PRIMARY KEY,
    ename VARCHAR(25),
    salary INTEGER
);

-- Create the CERTIFIED table
CREATE TABLE CERTIFIED (
    eid INTEGER,
    aid INTEGER,
    PRIMARY KEY (eid, aid),
    FOREIGN KEY (eid) REFERENCES EMPLOYEES(eid),
    FOREIGN KEY (aid) REFERENCES AIRCRAFT(aid)
);


-- Insert values into the AIRCRAFT table
INSERT INTO AIRCRAFT (aid, aname, cruisingrange) VALUES
    (1, 'Boeing 737', 3000),
    (2, 'Airbus A320', 2800),
    (3, 'Boeing 747', 5000);

-- Insert values into the EMPLOYEES table
INSERT INTO EMPLOYEES (eid, ename, salary) VALUES
    (101, 'Pilot 1', 90000),
    (102, 'Pilot 2', 75000),
    (103, 'Pilot 3', 85000),
    (104, 'Pilot 4', 95000);

-- Insert values into the CERTIFIED table
INSERT INTO CERTIFIED (eid, aid) VALUES
    (101, 1),
    (102, 2),
    (103, 1),
    (104, 3);

-- Insert values into the FLIGHTS table
INSERT INTO FLIGHTS (no, fromPlace, toPlace, distance, Departs, arrives, price) VALUES
    (1, 'Bengaluru', 'New Delhi', 1200, '2023-09-01', '2023-09-01', 6000),
    (2, 'Bengaluru', 'Frankfurt', 8000, '2023-09-02', '2023-09-02', 15000),
    (3, 'New Delhi', 'Bengaluru', 1200, '2023-09-03', '2023-09-03', 5500);

-- MariaDB [flight]> show tables;
-- +------------------+
-- | Tables_in_flight |
-- +------------------+
-- | select * from aircraft;         |
-- | select * from certified;        |
-- | select * from employees;        |
-- | select * from flights;          |
-- +------------------+
-- 4 rows in set (0.001 sec)


-- MariaDB [flight]> select * from aircraft;
-- +-----+-------------+---------------+
-- | aid | aname       | cruisingrange |
-- +-----+-------------+---------------+
-- |   1 | Boeing 737  |          3000 |
-- |   2 | Airbus A320 |          2800 |
-- |   3 | Boeing 747  |          5000 |
-- |   4 | Boeing750   |          1000 |
-- +-----+-------------+---------------+
-- 4 rows in set (0.001 sec)

-- MariaDB [flight]> select * from certified;
-- +-----+-----+
-- | eid | aid |
-- +-----+-----+
-- | 101 |   1 |
-- | 101 |   2 |
-- | 101 |   3 |
-- | 101 |   4 |
-- | 102 |   2 |
-- | 103 |   1 |
-- | 104 |   3 |
-- +-----+-----+
-- 7 rows in set (0.001 sec)

-- MariaDB [flight]> select * from employees;
-- +-----+---------+--------+
-- | eid | ename   | salary |
-- +-----+---------+--------+
-- | 101 | Pilot 1 |  90000 |
-- | 102 | Pilot 2 |  75000 |
-- | 103 | Pilot 3 |  85000 |
-- | 104 | Pilot 4 |  95000 |
-- | 105 | Pilot 5 |   8000 |
-- +-----+---------+--------+
-- 5 rows in set (0.001 sec)

-- MariaDB [flight]> select * from flights;
-- +----+-----------+-----------+----------+------------+------------+-------+
-- | no | fromPlace | toPlace   | distance | Departs    | arrives    | price |
-- +----+-----------+-----------+----------+------------+------------+-------+
-- |  1 | Bengaluru | New Delhi |     1200 | 2023-09-01 | 2023-09-01 |  6000 |
-- |  2 | Bengaluru | Frankfurt |     8000 | 2023-09-02 | 2023-09-02 | 15000 |
-- |  3 | New Delhi | Bengaluru |     1200 | 2023-09-03 | 2023-09-03 |  5500 |
-- |  4 | Bengaluru | Frankfurt |     8000 | 2023-09-05 | 2023-09-06 | 10000 |
-- +----+-----------+-----------+----------+------------+------------+-------+
-- 4 rows in set (0.001 sec)

-- 1.Find the names of aircraft such that all pilots certified to operate them have salaries more 
-- than Rs.80,000.

SELECT aname
    FROM AIRCRAFT
    WHERE aid NOT IN (
        SELECT aid
        FROM CERTIFIED
        WHERE eid IN (
            SELECT eid
            FROM EMPLOYEES
            WHERE salary <= 80000
        )
    );

-- +------------+
-- | aname      |
-- +------------+
-- | Boeing 737 |
-- | Boeing 747 |
-- | Boeing750  |
-- +------------+


-- 2. For each pilot who is certified for more than three aircrafts,find the eid and the 
-- maximum cruisingrange of the aircraft for which she or he is certified.

SELECT eid, MAX(cruisingrange)
FROM CERTIFIED C, AIRCRAFT A
WHERE C.aid = A.aid
GROUP BY c.eid
HAVING COUNT(c.aid) > 3;

-- +-----+--------------------+
-- | eid | MAX(cruisingrange) |
-- +-----+--------------------+
-- | 101 |               5000 |
-- +-----+--------------------+

-- 3.Find the names of pilots whose salary is less than the price of the cheapest route from 
-- Bengaluru to Frankfurt.
SELECT ename
    FROM EMPLOYEES
    WHERE salary < (
        SELECT MIN(price)
        FROM FLIGHTS
        WHERE fromPlace = 'Bengaluru' AND toPlace = 'Frankfurt'
    );
-- +---------+
-- | ename   |
-- +---------+
-- | Pilot 5 |
-- +---------+
-- 1 row in set (0.001 sec)

-- 4.Find the names of pilots certified for some Boeing aircraft.
SELECT ename
 FROM EMPLOYEES
 WHERE eid IN (
     SELECT eid
     FROM CERTIFIED
     JOIN AIRCRAFT ON CERTIFIED.aid = AIRCRAFT.aid
     WHERE aname LIKE 'Boeing%'
 );
-- +---------+
-- | ename   |
-- +---------+
-- | Pilot 1 |
-- | Pilot 3 |
-- | Pilot 4 |
-- +---------+
-- 3 rows in set (0.001 sec)

-- 5.Find the aids of all aircraft that can be used on routes from Bengaluru to New Delhi.
SELECT AID 
FROM AIRCRAFT
WHERE cruisingrange > (
                       SELECT DISTANCE 
                       FROM FLIGHTS 
                       WHERE fromPlace="Bengaluru" and toPlace = "New Delhi"
                       );
-- +-----+
-- | AID |
-- +-----+
-- |   1 |
-- |   2 |
-- |   3 |
-- +-----+
-- 3 rows in set (0.001 sec)


