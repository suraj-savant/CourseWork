-- Create the ACTOR table
CREATE TABLE ACTOR (
    Act_id INT PRIMARY KEY,
    Act_Name VARCHAR(25),
    Act_Gender VARCHAR(10)
);

-- Create the DIRECTOR table
CREATE TABLE DIRECTOR (
    Dir_id INT PRIMARY KEY,
    Dir_Name VARCHAR(25),
    Dir_Phone VARCHAR(20)
);

-- Create the MOVIES table
CREATE TABLE MOVIES (
    Mov_id INT PRIMARY KEY,
    Mov_Title VARCHAR(25),
    Mov_Year INT,
    Mov_Lang VARCHAR(50),
    Dir_id INT,
    FOREIGN KEY (Dir_id) REFERENCES DIRECTOR(Dir_id)
);

-- Create the MOVIE_CAST table
CREATE TABLE MOVIE_CAST (
    Act_id INT,
    Mov_id INT,
    Role VARCHAR(100),
    PRIMARY KEY (Act_id, Mov_id),
    FOREIGN KEY (Act_id) REFERENCES ACTOR(Act_id),
    FOREIGN KEY (Mov_id) REFERENCES MOVIES(Mov_id)
);

-- Create the RATING table
CREATE TABLE RATING (
    Mov_id INT PRIMARY KEY,
    Rev_Stars INT,
    FOREIGN KEY (Mov_id) REFERENCES MOVIES(Mov_id)
);

-- +------------------+
-- | Tables_in_movies |
-- +------------------+
-- | select * from actor;            |
-- | select * from director;         |
-- | select * from movie_cast;       |
-- | select * from movies;           |
-- | select * from rating;           |
-- +------------------+
-- 5 rows in set (0.002 sec)


-- MariaDB [movies]> select * from actor;
-- +--------+----------+------------+
-- | Act_id | Act_Name | Act_Gender |
-- +--------+----------+------------+
-- |      1 | Actor 1  | Male       |
-- |      2 | Actor 2  | Female     |
-- |      3 | Actor 3  | Male       |
-- |      4 | Actor 4  | Female     |
-- +--------+----------+------------+
-- 4 rows in set (0.001 sec)

-- MariaDB [movies]> select * from director;
-- +--------+----------------------+--------------+
-- | Dir_id | Dir_Name             | Dir_Phone    |
-- +--------+----------------------+--------------+
-- |      1 | Sanjay Leela Bansali | 123-456-7890 |
-- |      2 | Ram Gopal Verma      | 987-654-3210 |
-- +--------+----------------------+--------------+
-- 2 rows in set (0.001 sec)

-- MariaDB [movies]> select * from movie_cast;
-- +--------+--------+------------------+
-- | Act_id | Mov_id | Role             |
-- +--------+--------+------------------+
-- |      1 |      1 | Lead Actor       |
-- |      1 |      2 | Lead Actor       |
-- |      1 |      4 | Lead Actor       |
-- |      2 |      1 | Supporting Actor |
-- |      2 |      3 | Lead Actor       |
-- |      3 |      2 | Supporting Actor |
-- |      3 |      3 | Lead Actor       |
-- |      4 |      3 | Supporting Actor |
-- +--------+--------+------------------+
-- 8 rows in set (0.000 sec)

-- MariaDB [movies]> select * from movies;
-- +--------+-----------+----------+----------+--------+
-- | Mov_id | Mov_Title | Mov_Year | Mov_Lang | Dir_id |
-- +--------+-----------+----------+----------+--------+
-- |      1 | Movie 1   |     2020 | English  |      1 |
-- |      2 | Movie 2   |     2018 | Hindi    |      1 |
-- |      3 | Movie 3   |     2019 | Hindi    |      2 |
-- |      4 | Movie 4   |     2021 | English  |      2 |
-- +--------+-----------+----------+----------+--------+
-- 4 rows in set (0.001 sec)

-- MariaDB [movies]> select * from rating;
-- +--------+-----------+
-- | Mov_id | Rev_Stars |
-- +--------+-----------+
-- |      1 |         4 |
-- |      2 |         3 |
-- |      3 |         5 |
-- |      4 |         4 |
-- +--------+-----------+
-- 4 rows in set (0.001 sec)

-- 1.List the titles of all movies directed by ‘Sanjay Leela Bansali’.
SELECT M.Mov_Title
    -> FROM movies M, Director d
    -> WHERE M.Dir_id = d.Dir_id and Dir_name = "Sanjay Leela Bansali";
-- +-----------+
-- | Mov_Title |
-- +-----------+
-- | Movie 1   |
-- | Movie 2   |
-- +-----------+
-- 2 rows in set (0.002 sec)

-- 2.Find the movie names where one or more actors acted in two or more movies.

-- +-----------+
-- | Mov_Title |
-- +-----------+
-- | Movie 1   |
-- | Movie 2   |
-- +-----------+
-- 2 rows in set (0.001 sec)

-- 3.Find the title of movies and number of stars for each movie that has at least one rating 
-- and find the highest number of stars that movie received. Sort the result by movie title.
 SELECT M.Mov_Title, R.Rev_Stars
    -> FROM Movies M, Rating R
    -> WHERE M.Mov_id = R.Mov_id AND  R.Rev_Stars = (SELECT MAX(Rev_Stars)
    -> FROM Rating
    -> )
    -> ORDER BY M.Mov_Title;
-- +-----------+-----------+
-- | Mov_Title | Rev_Stars |
-- +-----------+-----------+
-- | Movie 1   |         5 |
-- | Movie 3   |         5 |
-- +-----------+-----------+
-- 2 rows in set (0.001 sec)


-- 4.Update rating of all movies directed by ‘Ram Gopal Verma’ to 5
update rating 
set Rev_Stars = 5 
Where Mov_id in (
    SELECT Mov_id 
    from movies m, director d
    where d.dir_id = m.dir_id and d.dir_name = "Ram Gopal Verma"
    );
Query OK, 1 row affected (0.003 sec)
Rows matched: 2  Changed: 1  Warnings: 0




-- SELECT DISTINCT Mov_Title
--     FROM MOVIES
--     WHERE Mov_id IN (
--         SELECT Mov_id
--         FROM MOVIE_CAST
--         GROUP BY Act_id
--         HAVING COUNT(Mov_id) >= 2
--     );