-- UPDATING RECORDS
	-- the SQL command line for updating is as follows
    -- UPDATE *table_name* SET *column_name* = new_value WHERE *condition*
		-- we are using twitter database as example

-- first lest get the data table
-- SELECT * FROM users

-- now we can UPDATE a value of any id
	-- example below
-- UPDATE twitter.users SET first_name = "Frobe" WHERE id=1; --commenting out to run line 15 to show 
		-- run it
        -- if successful you can run SELECT * FROM users; to see updated value(s)

-- I guess you need to comment line 6 out for it to run
-- but lets reattain our result grid

-- SELECT * FROM users; -- have to comment out to run line 22

-- let's change it back for good practice

UPDATE twitter.users SET first_name = "Kobe" WHERE id=1; 

SELECT * FROM users;