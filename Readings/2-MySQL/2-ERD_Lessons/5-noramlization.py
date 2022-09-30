# What is Normalization?

# Database normalization is simply a convention for splitting large tables of data into smaller separate tables with the primary goal being to NOT REPEAT DATA.
# Let's say that you wear a watch so you can check the time, because it's very important for you to know what the current time is. Would wearing eight watches make it easier? No way! Now we have eight conflicting accounts of what the proper time is. Worse yet, if we ever want to update the time, we'd have to do it for every watch independently. That's not very efficient!

# You can apply a similar concept to database design.
# If we want to store a user's email address, we'd want to store it in only one place. Then, if we ever need to refer to it again, we'd simply use the *ID*. The id will never change, so even if we update the user's email address, none of the other connections we defined in our database will be damaged.

# IT IS POSSIBLE TO TAKE NORMALIZATION TO AN EXTREME.
# For example, a simple address field. One state can have many cities, one city can have many streets, one street can have many buildings, one building can have many apartments, one apartment can have many residents... and so on.
# In the next sections, you'll learn more about why this type of complexity can be inefficient, especially for simple assignments.


#                                               FIRST FORM
# Each Column in your table can only have 1 value.
# Ex: You should not have an ADDRESS column in your table that lists the address, city, state, and zip, all separated by commas.
#instead create an id to reference specific addresses. 

#                   customers                      |\/|                           addresses
# |id | firstName | lastName | address_id  |       |\/|      # id |      Street     |      city      |     state    |
# |---------------|----------|-------------|       |\/|      # ---|-----------------|----------------|--------------|
# | 1 | randall   | frisk    |     4       |       |\/|    <-# 4  | 576 steel in    |  Grass valley  | 576 steel in |
# | 2 | michael   | choi     |     5       |       |\/|    <-# 5  | 333 ninja dr    |    Seattle     | 333 ninja dr |
# | 3 | dexter    | clark    |     6       |       |\/|    <-# 6  | 978 flip in     |    San Jose    | 978 flip in. | address_id references the id of addresses.



#                                               SECOND FORM
# Each Column in your table that is not a key (primary or foreign) must have unique values.
# Ex. If you have a movies table with a categories column, you should not have a category listed more than once.

#                   movies                                         categories
# |id |       title     |   year   | category_id |     -      |id |   name    |
# |---|-----------------|----------|-------------|     -      |---|-----------|
# | 1 | happy gilmore   |   1996   |     1       |     -      | 1 |  Comedy   |
# | 2 |      avatar     |   2009   |     2       |     -      | 2 | Adventure |
# | 3 |  despicable me  |   2010   |     3       |     -      | 3 |  Family   |
# | 4 |   21 Jump St    |   2012   |     1       |
# | 5 | despicable me 2 |   2013   |     3       |



#                                               THIRD FORM
# You cannot have a non-key column that is dependent on another non-key column.
# Ex. If you have a books table with columns publisher_name and publisher_address, the publisher_address and publisher_name should be separated into a separate table and linked to books with a foreign key. The publisher_address is dependent on the publisher_name and neither column is a key column.

# #                   books                                #publishers
# |id |       title     |  publisher_id  |     -      |id |      name      | publisher_rank |
# |---|-----------------|----------------|     -      |---|----------------|----------------|
# | 1 |   Mathematics   |     Pearson    |     -      | 1 |     Pearson    |    01          |
# | 2 |     Physics     |  Reed Elsevier |     -      | 2 |  Reed Elsevier |    02          |
# | 3 | Hacking Exposed |   McGraw-Hill  |     -      | 3 |   McGraw-Hill  |    08          |
# | 4 |  Hunger Games   |   Shcolastic   |     -      | 4 |   Shcolastic   |    10          |