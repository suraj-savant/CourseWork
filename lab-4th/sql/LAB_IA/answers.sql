-- 1. Consider the following Student database:
-- STUDENT(snum: integer, sname: string, major: string, levels: string, age: integer)
-- CLASS(cname: string, meetsat: string, room: string, fid: integer)
-- ENROLLED(snum: integer, cname: string)
-- FACULTY(fid: integer, fname: string, deptid: integer)
-- Write the following queries in SQL.

-- Query 1: Find the names of all Juniors (level = JR) who are enrolled in a class taught by Prof. Harshith
SELECT s.sname
FROM STUDENT s, CLASS c, ENROLLED e, FACULTY f
WHERE s.snum = e.snum
  AND c.cname = e.cname
  AND c.fid = f.fid
  AND s.levels = 'JR'
  AND f.fname = 'Harshith';


-- Query 2: Find the names of all classes that either meet in room R128 or have five or more Students enrolled

SELECT DISTINCT c.cname
FROM CLASS c, ENROLLED e
WHERE c.room = 'R128'
   OR (c.cname = e.cname
      AND (SELECT COUNT(*) FROM ENROLLED e2 WHERE e.cname = e2.cname) >= 5);


-- Query 3: Find the names of all students who are enrolled in two classes that meet at the same time.

SELECT DISTINCT s.sname
FROM STUDENT s, ENROLLED e1, ENROLLED e2, CLASS c1, CLASS c2
WHERE s.snum = e1.snum
  AND e1.snum = e2.snum
  AND e1.cname <> e2.cname
  AND e1.cname = c1.cname
  AND e2.cname = c2.cname
  AND c1.MEETSTAT = c2.MEETSTAT;

-- Query 4: Find the names of faculty members who teach in every room in which some class is taught.**

SELECT DISTINCT f.fname
FROM FACULTY f
WHERE NOT EXISTS (
    SELECT DISTINCT c.room
    FROM CLASS c
    WHERE NOT EXISTS (
        SELECT *
        FROM CLASS c2
        WHERE c2.fid = f.fid AND c2.room = c.room
    )
);


-- Query 5: Find the names of faculty members for whom the combined enrollment of the courses that they teach is less than five.**

SELECT DISTINCT f.fname
FROM FACULTY f
WHERE (SELECT SUM(enrollment_count)
       FROM (SELECT COUNT(*) as enrollment_count
             FROM CLASS c, ENROLLED e
             WHERE c.cname = e.cname AND c.fid = f.fid
             GROUP BY c.cname) as enrollments) < 5;


-- EXPT 2
-- The following relations keep track of Airline Flight information:
-- FLIGHTS(no: integer, fromPlace: string, toPlace: string, distance: integer, Departs: date, 
-- arrives: date,price: real)
-- AIRCRAFT(aid: integer, aname: string, cruisingrange: integer)
-- CERTIFIED(eid: integer, aid: integer)
-- EMPLOYEES(eid: integer, ename: string, salary: integer)
-- Query 1: Find the names of aircraft such that all pilots certified to operate them have salaries more than Rs. 80,000.

SELECT DISTINCT a.aname
FROM AIRCRAFT a
WHERE NOT EXISTS (
    SELECT e.eid
    FROM EMPLOYEES e, CERTIFIED c
    WHERE e.eid = c.eid AND c.aid = a.aid AND e.salary <= 80000
);

-- Query 2: For each pilot who is certified for more than three aircraft, find the eid and the maximum cruising range of the aircraft for which she or he is certified.


SELECT e.eid, MAX(a.cruisingrange)
FROM EMPLOYEES e, CERTIFIED c, AIRCRAFT a
WHERE e.eid = c.eid AND c.aid = a.aid
GROUP BY e.eid
HAVING COUNT(*) > 3;

-- Query 3: Find the names of pilots whose salary is less than the price of the cheapest route from Bengaluru to Frankfurt.


SELECT e.ename
FROM EMPLOYEES e
WHERE e.salary < (
    SELECT MIN(f.price)
    FROM FLIGHTS f
    WHERE f.fromPlace = 'Bengaluru' AND f.toPlace = 'Frankfurt'
);

-- Query 4: Find the names of pilots certified for some Boeing aircraft.


SELECT e.ename
FROM EMPLOYEES e
WHERE EXISTS (
    SELECT c.eid
    FROM CERTIFIED c, AIRCRAFT a
    WHERE c.eid = e.eid AND c.aid = a.aid AND a.aname LIKE 'Boeing%'
);

-- Query 5: Find the aids of all aircraft that can be used on routes from Bengaluru to New Delhi.

SELECT a.aid
FROM AIRCRAFT a
WHERE NOT EXISTS (
    SELECT f.no
    FROM FLIGHTS f
    WHERE f.fromPlace = 'Bengaluru' AND f.toPlace = 'New Delhi' AND f.no = a.aid
);

-- EXPT 3
-- AUTHOR(author_id:int, name:string, city:string, country:string)
-- PUBLISHER(publisher_id:int, name:string, city:string,country:string)
-- CATALOG(book_id:int, title:string, author_id:int, publisher_id:int, category_id:int, 
-- year:int, price:int)
-- CATEGORY(category_id:int, description:string)
-- ORDER_DETAILS(order_no:int, book_id:int, quantity:int)
-- Query 1: Find the publisher id who have not published any books.

SELECT publisher_id
FROM PUBLISHER
WHERE publisher_id NOT IN (
    SELECT DISTINCT publisher_id
    FROM CATALOG
);

-- Query 2: Find the author of the book which has maximum sales.
SELECT name
FROM AUTHOR
WHERE author_id = (
    SELECT author_id
    FROM CATALOG
    WHERE book_id = (
        SELECT book_id
        FROM ORDER_DETAILS
        GROUP BY book_id
        ORDER BY SUM(quantity) DESC
        LIMIT 1
    )
);

-- Query 3: Demonstrate how you increase the price of books published by a specific publisher by 10%.

UPDATE CATALOG
SET price = price * 1.10
WHERE publisher_id = (SELECT publisher_id FROM PUBLISHER WHERE name = 'PublisherName');

-- Query 4: Find the author name and publisher name who live in the same city.

SELECT a.name AS author_name, p.name AS publisher_name
FROM AUTHOR a, PUBLISHER p
WHERE a.city = p.city AND a.country = p.country;

-- Query 5: Find the publisher name who have published at least 4 books.

SELECT name
FROM PUBLISHER
WHERE publisher_id IN (
    SELECT publisher_id
    FROM CATALOG
    GROUP BY publisher_id
    HAVING COUNT(book_id) >= 4
);



-- EXPT 4
-- BRANCH(branch_name:string, branch_city:string, assets:real)
-- ACCOUNT(accno:int, branch_name:string, balance:real)
-- DEPOSITOR(customer_name:string, accno:int)
-- CUSTOMER(customer_name:string, customer_street:string,customer_city:string)
-- LOAN(Loan_number:int, branch_name:string, amount:real)
-- BORROWER(customer_name:string, Loan_number:int)
-- Query 1: Find all the customers who have at least two accounts at the main branch.

SELECT DISTINCT d.customer_name
FROM DEPOSITOR d, ACCOUNT a
WHERE d.accno = a.accno
  AND a.branch_name = 'main'
GROUP BY d.customer_name
HAVING COUNT(d.accno) >= 2;

-- Query 2: Demonstrate how you delete all account tuples at every branch located in a specific city.

DELETE FROM ACCOUNT
WHERE branch_name IN (
    SELECT branch_name
    FROM BRANCH
    WHERE branch_city = 'City B'
);

-- Query 3: Find the bank that has the highest average balance.

SELECT b.branch_name
FROM BRANCH b
WHERE b.assets = (
    SELECT MAX(assets)
    FROM BRANCH
);

-- Query 4: Find all the customers who have both account and loan at a specific branch.

SELECT DISTINCT c.customer_name
FROM CUSTOMER c, ACCOUNT a, LOAN l
WHERE c.customer_name IN (
    SELECT d.customer_name
    FROM DEPOSITOR d, ACCOUNT a
    WHERE d.accno = a.accno
      AND a.branch_name = 'SpecificBranch'
)
AND c.customer_name IN (
    SELECT b.customer_name
    FROM BORROWER b, LOAN l
    WHERE b.Loan_number = l.Loan_number
      AND l.branch_name = 'SpecificBranch'
);

-- EXPT 5
-- Consider the following Insurance database:
-- PERSON(driver_id,name ,address ) 
-- CAR(regno,model,year )
-- ACCIDENT(report_number,accd_date,location)
-- OWNS(driver_id,regno )
-- PARTICIPATED(driver_id,regno,report_number, damage_amount)

-- Query 1: Find the driver name and the model of the car which is owned by them.

SELECT p.name, c.model
FROM PERSON p, CAR c, OWNS o
WHERE p.driver_id = o.driver_id
  AND c.regno = o.regno;

-- Query 2: Update the damage amount for the car with specific regno in the accident with report number 4 to 25000.

UPDATE PARTICIPATED
SET damage_amount = 25000
WHERE regno = 'SpecificRegNo'
  AND report_number = 4;

-- Query 3: Find the total number of people who owned cars that were involved in accidents in the year 2020.

SELECT COUNT(DISTINCT p.driver_id)
FROM PERSON p, CAR c, OWNS o, PARTICIPATED pd, ACCIDENT a
WHERE p.driver_id = o.driver_id
  AND c.regno = o.regno
  AND o.regno = pd.regno
  AND pd.report_number = a.report_number
  AND YEAR(a.accd_date) = 2020;


-- EXPT 6
-- Consider the following schema for Order Database:
-- SALESMAN(Salesman_id,Name,City,Commission)
-- CUSTOMER(Customer_id,Cust_Name,City, Grade,Salesman_id)
-- ORDERS (Ord_No, Purchase_Amt, Ord_Date, Customer_id, Salesman_id)
-- Query 1: Count the customers with grades above Bangalore’s average.

SELECT COUNT(*)
FROM CUSTOMER
WHERE Grade > (SELECT AVG(Grade) FROM CUSTOMER WHERE City = 'Bangalore');

-- Query 2: Find the name and numbers of all salesmen who had more than one customer.

SELECT S.Name, S.Salesman_id, (
    SELECT COUNT(*)
    FROM CUSTOMER C
    WHERE C.Salesman_id = S.Salesman_id
) AS customer_count
FROM SALESMAN S
HAVING customer_count > 1;

-- Query 3: List all salesmen names and customer names for whom order amount is more than 4000.

SELECT S.Name AS salesman_name, C.Cust_Name AS customer_name
FROM SALESMAN S, CUSTOMER C, ORDERS O
WHERE S.Salesman_id = C.Salesman_id AND C.Customer_id = O.Customer_id
  AND S.Salesman_id = O.Salesman_id
  AND O.Purchase_Amt > 4000;

-- Query 4: Demonstrate the DELETE operation by removing salesman with id 1000. All his orders must also be deleted.

DELETE FROM ORDERS
WHERE Salesman_id = 1000;

DELETE FROM CUSTOMER
WHERE Salesman_id = 1000;

DELETE FROM SALESMAN
WHERE Salesman_id = 1000;


-- EXPT 7
-- Consider the schema for Movie Database:

-- ACTOR (Act_id, Act_Name, Act_Gender)
-- DIRECTOR (Dir_id, Dir_Name, Dir_Phone)
-- MOVIES (Mov_id, Mov_Title, Mov_Year, Mov_Lang, Dir_id)
-- MOVIE_CAST (Act_id, Mov_id, Role)
-- RATING (Mov_id, Rev_Stars)

-- Query 1: List the titles of all movies directed by 'Sanjay Leela Bhansali'.

SELECT Mov_Title
FROM MOVIES
WHERE Dir_id = (SELECT Dir_id FROM DIRECTOR WHERE Dir_Name = 'Sanjay Leela Bhansali');

-- Query 2: Find the movie names where one or more actors acted in two or more movies.

SELECT M.Mov_Title
FROM MOVIES M
JOIN MOVIE_CAST MC ON M.Mov_id = MC.Mov_id
GROUP BY M.Mov_id, M.Mov_Title
HAVING COUNT(DISTINCT MC.Act_id) >= 2;

-- Query 3: Find the title of movies and number of stars for each movie that has at least one rating and find the highest number of stars that movie received. Sort the result by movie title.

SELECT M.Mov_Title, MAX(R.Rev_Stars) AS Max_Stars
FROM MOVIES M
LEFT JOIN RATING R ON M.Mov_id = R.Mov_id
GROUP BY M.Mov_Title
HAVING MAX(R.Rev_Stars) IS NOT NULL
ORDER BY M.Mov_Title;

-- Query 4: Update rating of all movies directed by 'Ram Gopal Verma' to 5.

UPDATE RATING
SET Rev_Stars = 5
WHERE Mov_id IN (
    SELECT Mov_id
    FROM MOVIES
    WHERE Dir_id = (SELECT Dir_id FROM DIRECTOR WHERE Dir_Name = 'Ram Gopal Verma')
);


select  book_id 
from order_details o 
group by o.book_id 
having o.quantity = max(o.quantity);