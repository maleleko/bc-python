-- Create 3 New Dojos
INSERT INTO dojos (name) VALUES ('Coding Dojo');
INSERT INTO dojos (name) VALUES ('Gaming Dojo');
INSERT INTO dojos (name) VALUES ('Skateboarding Dojo'); 
SELECT * FROM dojos;

	-- Delete the 3 Dojos You just Created
DELETE FROM dojos WHERE id = 1 OR id = 2 OR id = 3;
SELECT * FROM dojos;

	-- Create 3 more dojos
INSERT INTO dojos (name) VALUES ('FPS Dojo');
INSERT INTO dojos (name) VALUES ('FGC Dojo');
INSERT INTO DOJOS (name) VALUES ('Street Dojo');
SELECT * FROM dojos;


	-- Create 3 Ninjas that belong to the first dojo
INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ('Maleko', 'Osby', 25, 4);
INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ('Kyle', 'Reimers', 99, 4);
INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ('Ced', 'Gal', 28, 4); 
SELECT * from ninjas;

-- Create 3 ninjas that belong to the second dojo
INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ('Tim', 'Single', 88, 5);
INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ('Sophea', 'Vann', 66, 5);
INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ('James', 'Ngyu', 24, 5);
select * from ninjas;

-- Retrieve all the ninjas from the first dojo
SELECT * from ninjas WHERE dojo_id=4;

-- Retrieve all the ninjas from the last dojo
SELECT * FROM ninjas WHERE dojo_id=5;
