# AJAX stands for Asynchronous JavaScript and XML. But what does asynchronous mean, to understand it let's first establish what synchronous code means.



                # Synchronous vs. Asynchronous

# JavaScript, like most languages, is synchronous by design.  The JS interpreter reads the code from top to bottom, line by line, and doesn't move on until the current line of code is finished.  While this might be fine for simple applications, eventually we will want multiple things to happen at the same time in our code.  We can use asynchronous behavior to accomplish this.

# Let's look at the restaurant analogy:

    # You and a friend walk into your favorite restaurant and sit down.  You see a bunch of wait staff standing by doing nothing, eventually your server comes to take your order.  Once completed, they deliver your order to the kitchen and wait for the food to be ready.  After your food is finished cooking, they bring it to your table.  They then wait for you to finish eating, and deliver your bill.  You pay, and then they move on to their next table.  This is synchronous behavior and it is how most code is written and executed.  But it is a waste of time for the server to wait for your entire process to finish.  Normally in restaurants we see the servers performing multiple tasks at once or asynchronous behavior.



                # The Birth of Asynchronous JavaScript And XML (AJAX)

# AJAX was born out of many different tech companies trying to communicate between servers behind the scenes of a website.  It was coined by Jesse James Garrett in 2005 and standardized by W3C in 2006.

# AJAX is a group of technologies that allows a developer to change parts of a web site with new content from servers, without reloading the page.  In a sense, it's magical.