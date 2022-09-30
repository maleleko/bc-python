--  FUNCTIONS VIDEO FOLLOW ALONG
	-- using twitter database for examples

-- SELECT * from users;


		-- text functions
-- concat()
-- SELECT CONCAT("Mr.", " ", first_name, ' ', last_name) FROM users;
	-- we can also do SELECT CONCAT("Mr.", " ", first_name, ' ', last_name) AS full_name FROM USERS;
    -- this will apply a whole new column(i assume)
    
-- concat_ws()
	-- we can use _WS to add spaces without having to hard code them in all the time
SELECT CONCAT_WS(" ", "Mr.", first_name, last_name, 'is cool af') AS full_name FROM users;

-- length()
	-- if we want to find the length/num of chars for a particular item
SELECT LENGTH(last_name) AS last_len FROM users;

-- lower()
	-- this pretty much makes all text lowercase lol, cool function
SELECT LOWER(first_name) AS first_lowercase FROM users;
SELECT first_name FROM users; -- spot the differences between 22 and 23. ez to see.



		-- date functions
        -- date functions need to be performed on DATETIME columns
-- hour()
-- itll give us the hour in a 24hr format for each
SELECT HOUR(created_at) AS date_hour, created_at FROM users;

-- dayname()
-- itll give us the day of the week for each
SELECT DAYNAME(created_at) AS day_name, created_at FROM users;

-- month()
-- this will give us the month num for each
SELECT MONTH(created_at) AS month_num, created_at FROM users;

-- now()
-- this will give us the current date & time
SELECT NOW() AS right_now;

-- date_format()
-- if we want to format it in a certain way
-- go to w3schools sql func_date_format
-- https://www.w3schools.com/sql/func_mysql_date_format.asp
SELECT DATE_FORMAT(created_at, '%W, %M %e, %Y') FROM users;



		-- numeric functions
-- abs() | abs(n)
-- absolute value of n

-- mod() | mod(n1, n2)
-- the remainder of dividing n1 by n2

-- rand() | rand()
-- a random number between 0-10

-- sqrt() | sqrt(n)
-- the square root of n

