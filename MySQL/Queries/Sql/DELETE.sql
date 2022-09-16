					-- DELETE BASICS
                    
			-- we are using twitter database as example
	-- if you are getting errors regarding SQL SAFE UPDATES
    -- run SET SQL_SAFE_UPDATES = 0; | 1 is default


			--  DELETING RECORDS
 
-- The SQL command pattern for deleting/removing records is as follows
	-- DELETE FROM *table_name* WHERE *condition*;
-- IMPORTANT: if WHERE condition is not added to the DELETE statement, it will delete all the records on the table.


-- let's delete the tweets we added from our INSERT practice/learning.
-- SELECT * FROM tweets
DELETE FROM tweets WHERE id=14;
-- DELETE FROM tweets WHERE id=13; -- i had two lol


		-- i'll add the INSERT method here just for future reference.
-- INSERT INTO tweets (tweet, user_id, created_at, updated_at) VALUES ("hey wassup", 1, NOW(), NOW());