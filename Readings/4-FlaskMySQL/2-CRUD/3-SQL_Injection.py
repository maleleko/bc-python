#                   SQL Injection



# As mentioned in the last module, let's discuss further why we want to use prepared statements.

# Take a look at this code snippet. Hopefully it feels familiar:
    # query = "SELECT * FROM users WHERE email = %(email)s;"
    # data = { 'email' : request.form['email'] }
    # result = mysql.query_db(query, data)

# Here, we are using a PREPARED STATEMENT in order to create our SQL query with data provided by our user. This is done by leaving placeholders in our query that are filled in with the values from our data dictionary.

# Maybe you're thinking it seems tedious to create a dictionary just to pass the user's email input into the query. Perhaps we can be clever and use literal string interpolation to generate our query, and save ourselves from the step of making a dictionary at all.


                # ***** DANGER, LAZY CODING BELOW *****

    # this code is for demonstration purposes only
    # DO NOT use this code in production, it will leave you vulnerable to SQL injection
    # query = f"SELECT * FROM users WHERE email = '{request.form['email']}';"
    # result = mysql.query_db(query)

# This might save us some code, but it is not worth it! Creating a query this way allows for SQL injection, which means that we are vulnerable to any input that a user may provide in the form, such as more SQL code. For example, consider what will happen if our user types the following into our form's email input:

# Email:
    # joe@GMAIL.COM' OR '1'='1
    # By using plain string interpolation, this would turn our query into:
        # SELECT * FROM users WHERE email = 'joe@gmail.com' OR '1'='1'; 

# Since '1' = '1' will always evaluate to true, this query will now fetch all the data from the users table. We may have just opened a huge portion of our database to a malicious user. Any user with SQL knowledge may easily figure out how to manipulate our SQL queries. They may gain access to sensitive data or force us to run a very dangerous query.

            # Other Examples of SQL Injections

# Consider another scenario where the user put in the following as their email:
    # joe@gmail.com"; DROP TABLE users;

# What would have happened if the way you prepared the SQL query was like this?
#    query = f"SELECT * FROM users WHERE email = '{request.form['email']}';"
#    result = mysql.query_db(query)

# The query it would have run would have been
    # SELECT * FROM users WHERE email = "joe@gmail.com";  DROP users;
# In other words, it would have dropped the entire users table!

# What if the user passed the following as their email input?
    # joe@gmail.com"; UPDATE users SET password = '____' WHERE id = '___'

# This would have changed someone's password. Similarly, you can see how one could set oneself to be an admin or retrieve sensitive information from other users table (e.g. credit card, address, etc). The possibilities are endless.

# Now that you're feeling paranoid about SQL injection, cheer yourself up with this xkcd comic!  - https://xkcd.com/327/



                # Prepared Statements to the Rescue

# Fortunately, by using prepared statements, we can be assured that the user input will not be interpreted as SQL code. Our users may type in all the dangerous characters they'd like - apostrophes, semicolons, parentheses - and it won't matter. With the prepared statement, everything will simply be treated as a regular string, so our query will be harmlessly nonsensical as it looks for an impossible email address:
    # SELECT * FROM users WHERE email = "joe@gmail.com' OR '1'='1"; 

# There are many ways to protect against SQL injection, including using a framework and trusted libraries. For example, the way we currently have PyMySQL set up, we will not be able to run more than one query at a time. Users will therefore not be able to attach extra queries to ours. We may also try to sanitize strings from our post data manually by escaping special characters with the '/' character.

# Let's definitely stick with running queries by using the following pattern any time user input is concerned:
    # query = "SELECT * FROM users WHERE email = %(email)s;"
    
# the placeholder variable is called email
# it must match the key name in the data dictionary
    # data = { 
    #     # this 'email' Key in data must be named to match the placeholder in the query.
    #     'email' : request.form['email'] 
    # }
    # result = mysql.query_db(query, data)