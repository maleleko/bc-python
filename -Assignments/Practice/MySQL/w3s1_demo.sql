USE w3s1_demo;
-- INSERT INTO users (name,email,password) VALUES ('John Doe', 'j@j.com',123456);
-- INSERT INTO users (name,email,password) VALUES ('John Doe', 'j@j.com',123456);
-- INSERT INTO users (name,email,password) VALUES ('Jane Doe', 'd@d.com', 123456);
-- INSERT INTO users (name,email,password) VALUES ('Jack Bauer', 'b@b.com',123456);
-- INSERT INTO users (name,email,password) VALUES ('James Bond', 'jb@jb.com',123456);
-- SET SQL_SAFE_UPDATED = 1; -- dont use this lol

-- DELETE from users; -- dont use this lol

-- UPDATE

UPDATE users SET name= "NEW NAME" WHERE id = 1; -- updates id 1
UPDATE users SET name = "Will Doe", email="w@w.com", password="123456" WHERE id=2; -- updates id 2 etc
SELECT * from users;

-- POST
INSERT INTO posts (content, users_id) VALUES ('My name is Bond, James Bond', 5),("I'm Jack Bauer the CTU Director", 4);

SELECT * FROM posts; 
--            left            right    || works left from right
SELECT * FROM users LEFT JOIN posts ON posts.users_id = users.id;
-- SELECT * FROM posts LEFT JOIN users ON posts.users_id = users.id;
-- SELECT * FROM users JOIN posts ON posts.users_id = users.id;

-- joining only for user specfics
SELECT * FROM posts LEFT JOIN users ON posts.users_id = users.id WHERE users.id = 4;

-- INSERT INTO likes (posts_id,users_id) VALUES (8,1),(3,4),(3,3);
-- SELECT * FROM likes;

-- INSERT INTO likes (posts_id,users_id) VALUES(1,4);
-- SELECT * FROM likes;