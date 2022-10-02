#                               SECURING PASSWORDS


# As we've seen, hackers can find ways to gain access to your database. Web developers are responsible for keeping users' data safe. No one should know our users' passwords - not even us! This can be very difficult to do correctly and is largely why we see so many websites offering us the option to sign up via Facebook or Google - they're passing the job of user authentication off to the experts (how you may feel about their expertise is a different matter). This may be an option you would like to explore in the future, but you should still know how to store - and how not to store - users' passwords.


                    # BAD idea: Directly store passwords in the database
                        # https://s3.amazonaws.com/General_V88/boomyeah2015/codingdojo/curriculum/content/chapter/Screen_Shot_2018-03-19_at_4.24.11_PM.png

# It should be pretty obvious why we would never want to put our users' passwords straight into our database. As we saw when we discussed SQL injection, it may be very easy for malicious users to access data that wasn't meant for them to see. So obviously we would never just store passwords in plain text! (It's obvious now, but unfortunately, many developers have had to learn that lesson the hard way.)

# Instead, we'll want to mask the data somehow, so even if hackers got into our database, they wouldn't know what to do with it.




                # Good idea, but not good enough #1: Hash the passwords before storing them
                    # https://s3.amazonaws.com/General_V88/boomyeah2015/codingdojo/curriculum/content/chapter/Screen_Shot_2018-03-19_at_4.35.58_PM.png

# In order to mask our users' passwords, we will use a technique called hashing. Hashing scrambles data in such a way that cannot be reversed. This is different from another technique you may have heard of called encryption, which scrambles data with the use of an encryption key so that it is reversible. With encryption, anyone with the encryption key may decrypt the data. Ideally, only the sender and the receiver of the data should know the encryption key. Credit card data, for example, should be encrypted. Passwords, however, should be hashed, and we'll only store hashed passwords in our database.

# We said that hashing is not reversible, so how can we match passwords? The answer is that a hashing algorithm will always produce the same output for a particular input. Therefore, we'll take the password input when a user logs in, hash it, and compare the hash to the value stored in the database.

# Sadly, hashing is supposed to be irreversible, but many of the common hashing algorithms, such as md5() and sha1(), have been hacked and are no longer reliable. Besides, this technique leaves us vulnerable to brute force attacks. Hackers have even made rainbow tables, which are tables of common passwords (we're looking at you, "password123") and their hashes. Rainbow tables aren't even necessary anymore, though, because modern computers and the hashing algorithms are so fast, it doesn't take long for a hacker's program to test thousands of passwords. Imagine all the harm that could quickly be done with a for-loop like the one below:

    #         for password in my_list_of_passwords_to_test:     # loop through every password we want to test
    # if md5(password + salt) in table:             # see if the salt is concatenated to the password
    #     print("I guessed a password!", password)




                # Good enough #3: Give each user a unique salt
                    # https://s3.amazonaws.com/General_V88/boomyeah2015/codingdojo/curriculum/content/chapter/Screen_Shot_2018-03-19_at_5.14.05_PM.png

# If we give each user a unique salt, we can just store that salt in the database as user data. It may seem silly, because now anyone who gets into our database will have all the salts. However, the point is not to keep the salts secret, but to slow down hackers' ability to test thousands of passwords. Notice our hacker's program now has a nested for-loop, which will take much longer to run:

            # for user in users:                                       # loop through all the users                
            #     for password in my_list_of_passwords_to_test:        # loop through every password we want to test
            #         if md5(password + user['salt']) in table:        # see if the user's salt is concatenated to the password
            #             print("I guessed a password!", password)

# So far, this is our best option, and the big benefit it has is slowing down hackers' attempts to brute force their way to finding passwords. Since this strategy of slowing down hackers is the best we have, that leads us to the solution we should use, Bcrypt.


                # Bcrypt, the best we've got

# Bcrypt is a hashing algorithm that is purposefully designed to be slow. It is not so slow to affect a particular user's experience, but hackers who are trying to brute force their way through thousands of passwords will not bother. Other than that, it uses the same ideas as we already listed above. Since it is slow, hackers may resort to rainbow tables again, so Bcrypt generates a salt. Bcrypt adds the salt to the user's password and hashes the result, which we store in the database.

# An important thing to note is that, as developers, we have to do all we can to protect our users' data. However, if a user decides to use a weak password, there is nothing we can do. Take this lesson into your own practice. Keep your passwords secure, keep them unusual enough so they will never appear on a rainbow table, never give your password to a site you do not trust, consider using a trusted password manager, and do not reuse passwords for different accounts.