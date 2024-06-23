CREATE TABLE STUDENT(
    SNUM INT PRIMARY KEY,
    SNAME VARCHAR(20) NOT NULL,
    MAJOR VARCHAR(10) NOT NULL,
    LEVEL VARCHAR(3) NOT NULL,
    AGE INT
    );

CREATE TABLE FACULTY(
    FID INT PRIMARY KEY,
    FNAME VARCHAR(20) NOT NULL,
    DEPTID INT NOT NULL
); 

CREATE TABLE CLASS(
    CNAME VARCHAR(10) PRIMARY KEY,
    MEETSTAT VARCHAR(10) NOT NULL,
    ROOM VARCHAR(5) NOT NULL,
    FID INT,
    FOREIGN KEY (FID) REFERENCES FACULTY(FID)
    );

CREATE TABLE ENROLLED(
    SNUM INT,
    CNAME VARCHAR(10),
    PRIMARY KEY(SNUM, CNAME),
    FOREIGN KEY(SNUM) REFERENCES STUDENT(SNUM),
    FOREIGN KEY(CNAME) REFERENCES CLASS(CNAME)
);

-- MariaDB [STUDENT]> SHOW TABLES;
-- +-------------------+
-- | Tables_in_student |
-- +-------------------+
-- |select * from class    ;         |
-- |select * from enrolled ;         |
-- |select * from faculty  ;         |
-- |select * from student  ;         |
-- +-------------------+
-- 4 rows in set (0.001 sec)

-- MariaDB [STUDENT]> SELECT * FROM STUDENT;
-- +------+--------+-------+-------+------+
-- | SNUM | SNAME  | MAJOR | LEVEL | AGE  |
-- +------+--------+-------+-------+------+
-- |    1 | Ravi   | DBMS  | JR    |   20 |
-- |    2 | Ram    | OS    | SR    |   22 |
-- |    3 | Raju   | OS    | JR    |   20 |
-- |    4 | Radha  | DAA   | JR    |   20 |
-- |    5 | Sham   | DBMS  | SR    |   22 |
-- |    6 | Rajesh | DBMS  | SR    |   22 |
-- |    7 | Rakesh | DBMS  | JR    |   20 |
-- |    8 | Hemant | DBMS  | SR    |   23 |
-- +------+--------+-------+-------+------+
-- 8 rows in set (0.001 sec)

-- MariaDB [STUDENT]> SELECT * FROM FACULTY;
-- +-----+---------+--------+
-- | FID | FNAME   | DEPTID |
-- +-----+---------+--------+
-- |   1 | Harshit |     11 |
-- |   2 | Ruturaj |     12 |
-- +-----+---------+--------+
-- 2 rows in set (0.001 sec)

-- MariaDB [STUDENT]> SELECT * FROM CLASS;
-- +-------+----------+------+------+
-- | CNAME | MEETSTAT | ROOM | FID  |
-- +-------+----------+------+------+
-- | DAA   | 12       | R129 |    2 |
-- | DBMS  | 10       | R129 |    1 |
-- | OS    | 10       | R128 |    2 |
-- +-------+----------+------+------+
-- 3 rows in set (0.001 sec)

-- MariaDB [STUDENT]> SELECT * FROM ENROLLED;
-- +------+-------+
-- | SNUM | CNAME |
-- +------+-------+
-- |    1 | DBMS  |
-- |    2 | OS    |
-- |    3 | OS    |
-- |    4 | DAA   |
-- |    5 | DAA   |
-- |    5 | DBMS  |
-- |    6 | DBMS  |
-- |    7 | DBMS  |
-- |    8 | DBMS  |
-- +------+-------+
-- 9 rows in set (0.001 sec)


-- 1. Find the names of all Juniors (level = JR) who are enrolled in a class taught by Prof. 
-- Harshith

SELECT SNAME
FROM STUDENT S, CLASS C, ENROLLED E, FACULTY F
WHERE S.LEVEL = "JR" 
AND F.FNAME = "HARSHIT" 
AND C.FID = F.FID 
AND C.CNAME = E.CNAME
AND S.SNUM = E.SNUM;

-- +--------+
-- | SNAME  |
-- +--------+
-- | Ravi   |
-- | Rakesh |
-- +--------+
-- 2 rows in set (0.001 sec)

-- 2. Find the names of all classes that either meet in room R128 or have five or more Students 
-- enrolled

SELECT DISTINCT C.CNAME
FROM CLASS C, ENROLLED E
WHERE C.ROOM = "R128" 
      OR (C.CNAME = E.CNAME 
          AND (SELECT COUNT(*) 
        FROM ENROLLED E2 
        WHERE E.CNAME = E2.CNAME) >=5);

-- 3 Find the names of all students who are enrolled in two classes that meet at the same time.

SELECT sname
FROM STUDENT
WHERE snum IN (
    SELECT e1.snum
    FROM ENROLLED e1, ENROLLED e2, CLASS c1, CLASS c2
    WHERE e1.snum = e2.snum
    AND e1.cname <> e2.cname
    AND e1.cname = c1.cname
    AND e2.cname = c2.cname
    AND c1.MEETSTAT = c2.MEETSTAT
);

-- 4Find the names of faculty members who teach in every room in which some class is taught
Select fname 
from faculty f
where f.fid = (
SELECT FID
 FROM CLASS
 GROUP BY FID
 HAVING COUNT(*) = (SELECT COUNT(DISTINCT ROOM) FROM CLASS));
SELECT F.FNAME
FROM CLASS C, FACULTY F
GROUP BY C.FID 
HAVING COUNT(*) = (SELECT COUNT(DISTINCT ROOM) FROM CLASS);

-- 5 Find the names of faculty members for whom the combined enrollment of the courses that they teach is less than five
Select f.fname 
from faculty f
where f.fid in (

SELECT c.fid
from class c, enrolled E
where c.cname = e.cname
GROUP by c.fid
HAVING count(*) < 5
) ;

-- +---------+
-- | fname   |
-- +---------+
-- | Ruturaj |
-- +---------+
-- 1 row in set (0.002 sec)






