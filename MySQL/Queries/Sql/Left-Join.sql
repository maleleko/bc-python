		-- LEFT JOIN
        
--  What query would you run to get all tweets from the user id of 1?
SELECT * FROM users LEFT JOIN tweets ON users.id = tweets.user_id WHERE users.id = 1;

-- we can just grab the tweets by:
SELECT tweets.tweet AS kobe_tweets FROM users LEFT JOIN tweets ON users.id = tweets.user_id 
WHERE users.id = 1;

-- What query would return all the tweets that the user with id 2 has tagged as favorites?
SELECT first_name, tweet FROM users LEFT JOIN faves ON users.id = faves.user_id LEFT JOIN tweets 
ON faves.tweet_id = tweets.id WHERE users.id = 2;

-- What query would you run to get all the tweets that user with id 2, or user with id 1, has tagged as favorites?
SELECT first_name, tweet FROM users LEFT JOIN faves ON users.id = faves.user_id LEFT JOIN tweets
ON faves.tweet_id = tweets.id WHERE users.id = 2 OR users.id =1;

-- What query would you run to get all the users that are following the user with id 1?
SELECT users.first_name AS followed, users2.first_name AS follower FROM users LEFT JOIN follows
ON users.id = follows.followed_id LEFT JOIN users AS users2 ON users2.id = follows.follower_id
WHERE users.id =1;

--  What query would you run to get all users that are not following the user with id of 2?
	-- This requires nested queries, which you can learn about at
    -- http://sqlzoo.net/wiki/SELECT_within_SELECT_Tutorial
SELECT * FROM users WHERE users.id NOT IN(SELECT follower_id FROM follows WHERE followed_id = 2)
AND users.id !=2;

-- we can run functions on specific columns and often times it is paired up with the GROUP BY statement.
	-- We will have plent of practice with functions in the next tab.
SELECT users.first_name as user, COUNT(users2.first_name) as follower_count FROM users
LEFT JOIN follows ON users.id = follows.followed_id LEFT JOIN users AS users2
ON users2.id = follows.follower_id WHERE users.id = 1 GROUP BY users.id;


			-- LEFT JOIN VS JOIN
-- As mentioned earlier, LEFT JOIN and JOIN are all that you need for web development. 
	-- They are very similar, but you should not think of them interchangeably. 
		-- There is a difference in the output that they provide,
			-- specifically in the cases where a record in one table has no matching record in the joining table.

-- if we run the following sql command in our twitter database
SELECT first_name, tweet FROM users LEFT JOIN tweets ON users.id = tweets.user_id;
-- it pretty much includes everything associated with the left table onto the right table
	-- but if we just use regular JOIN it will only include the things that are associated
    -- with the specific id
SELECT first_name, tweet FROM users JOIN tweets ON users.id = tweets.user_id;


--  In the second example, Rajon is omitted from the table.
	-- When SQL uses the keyword JOIN, it only includes those records that have matches on both sides.
		-- It will omit any records that don't have a 'partner'. 
        
-- On the other hand, LEFT JOIN will include all the records from the FIRST table(the 'left' table | left2right)
-- REGARDLESS of whether that record has a matching foreign key in the 'right' table that we are trying to join
    
-- To summarize, JOIN will only include the intersection of the two tables, whereas LEFT JOIN will include all
	-- records from the first table, plus the records from the second table that correspond.
-- This is why the JOIN is sometimes called the INNER JOIN,
	-- while all the other joins (including LEFT JOIN) are referred to as OUTER JOINs. 