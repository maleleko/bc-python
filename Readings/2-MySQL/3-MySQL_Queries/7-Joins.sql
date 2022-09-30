-- JOINING TABLES
	-- using provided database for example

		-- JOINS VIDEO FOLLOW ALONG
-- JOIN
-- Find all the clients (first and last name) billing amounts and charged rate
SELECT clients.first_name, clients.last_name, billing.amount, billing.charged_datetime FROM clients
JOIN billing ON clients.id = billing.clients_id;

-- list all the domain names and leads (first and last name) for each site
SELECT sites.domain_name, leads.first_name, leads.last_name FROM sites JOIN leads ON sites.id = leads.sites_id;

		-- JOIN ON MULTIPLE TABLES
-- Get the names of the clients, their domain names and the first names of all the leads generated from those sites
SELECT clients.first_name AS client_firstname, clients.last_name, sites.domain_name, leads.first_name 
AS leads_firstname FROM clients JOIN sites ON clients.id = sites.clients_id JOIN leads 
ON sites.id = leads.sites_id;

		-- LEFT & RIGHT JOIN
-- list all the clients and the sites each client has, even if the client hasn't landed a site yet.
SELECT clients.first_name, clients.last_name, sites.domain_name FROM clients LEFT JOIN sites 
ON clients.id = sites.clients_id;


		-- GROUPING ROWS
-- Find all the clients (first and last name) and their total billing amounts
SELECT clients.first_name, clients.last_name, SUM(billing.amount) FROM clients
JOIN billing ON clients.id = billing.clients_id GROUP BY clients.id;
-- when using group by, always use some sort of function.

	-- GROUP_CONCAT
-- list all the domain names associated with each client
SELECT GROUP_CONCAT(" ", sites.domain_name) AS domains, clients.first_name, clients.last_name FROM clients 
JOIN sites  ON clients.id = sites.clients_id GROUP BY clients.id;

	-- COUNT
-- find the total number of leads for each site
SELECT COUNT(leads.id), sites.domain_name FROM sites JOIN leads ON sites.id = leads.sites_id 
GROUP BY sites.id;



		-- MICAEL CHOI follow along video
 SELECT * FROM billing JOIN clients ON billing.clients_id = clients.id ORDER BY clients.id;
 
SELECT SUM(amount), count(*), clients.id, clients.first_name, clients.last_name, clients.email FROM billing 
JOIN clients ON billing.clients_id = clients.id GROUP BY clients.id;

SELECT SUM(amount) as total, count(*) as num_transactions, clients.id, clients.first_name as first,
clients.last_name, clients.email FROM billing 
JOIN clients ON billing.clients_id = clients.id GROUP BY clients.id;





