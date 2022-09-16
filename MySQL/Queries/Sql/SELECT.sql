		-- we are using twitter database as example

-- users table 

-- SELECT * FROM users;
-- if we want to select specifics instead of all(*) tables we can instead run 

-- SELECT first_name as first, last_name as last FROM users;

		-- we can also add conditionals like
-- SELECT * FROM users 
-- WHERE id=1 OR id=2;
-- ORDER BY birthday -- ASC/DESC-- 

		-- faves table
-- SELECT * FROM faves; 

			-- -- follows table
-- SELECT * FROM follows;

			-- tweets table
-- SELECT * FROM tweets;



			-- Basics
-- What query would you run to get all of the users?
SELECT * FROM users; 

-- What query would you run to only get the first names of all of the users?
SELECT first_name FROM users;

-- What query would you run to only get the first and last names of all of the users?  
SELECT first_name, last_name FROM users;



-- SELECT w/ CONDITIONALS
-- What query would you run to only get the first name of users with id of 2?
SELECT first_name FROM users WHERE id=2; 

-- What query would you run to get the last names of users with id of 2 or 3?
SELECT last_name FROM users WHERE id=2 OR id=3;

-- What query would you run to get all of the users with id greater than 2?
SELECT * FROM users WHERE id > 2;

-- What query would you run to get all of the users with id less than or equal to 3?
SELECT * FROM users WHERE id <= 3;

-- What query would you run to get all of the users with first names ending in "e"?
SELECT * FROM users WHERE first_name LIKE "%e"; -- I guess placement of "%" acts as an ender

-- What query would you run to get all of the users with first names starting in "K"?
SELECT * FROM users WHERE first_name LIKE "K%"; -- placement of % acts as starter here

-- What query would you run to get all of the users with first names not starting in "K"?
SELECT * FROM users WHERE first_name NOT LIKE "K%"; -- "NOT LIKE" 



			-- SELECT w/ Sorting

-- What query would you run to get all of the users with the youngest users at the top of the table?
SELECT * from users ORDER BY birthday DESC; -- ORDER BY is the syntax we use here. DESC/ASC for organization

-- What query would you run to get all of the users with the oldest users at the top of the table?
SELECT * FROM users ORDER BY birthday ASC;

-- What query would you run to get all of the users with the first name that ends with "e" with the youngest users at the top of the table?
SELECT * FROM users WHERE first_name LIKE "%e" ORDER BY birthday DESC;

-- What query would you run to get only the first names of all of the users in alphabetical order?
SELECT first_name FROM users ORDER BY first_name ASC;



				-- SELECT w/ LIMIT and OFFSET
                
-- What query would you run to get the first 3 users?
SELECT * FROM users LIMIT 3;

-- What query would you run to get user records 3-5?
SELECT * FROM users LIMIT 3 OFFSET 2;

-- You could also combine LIMIT and OFFSET like this:
SELECT * FROM users LIMIT 2,3; -- I guess you put the offset number first, then the limit.