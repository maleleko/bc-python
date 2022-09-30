

                            # ONE TO MANY
# Continuing from our previous example of customers and addresses tables where one customer can only have one address


#                   customers
# |id | firstName | lastName | address_id  |
# |---|-----------|----------|-------------|
# | 1 | randall   | frisk    |     4       |
# | 2 | michael   | choi     |     5       |
# | 3 | dexter    | clark    |     6       |


# #                   addresses
# |id |      Street     |      City      |     State    |
# |---|-----------------|----------------|--------------|
# | 4 | 576 steel in    |  Grass valley  | 576 steel in |
# | 5 | 333 ninja dr    |    Seattle     | 333 ninja dr |
# | 6 | 978 flip in     |    San Jose    | 978 flip in. |

# We now want our customers to be able to order items from us. To add our orders table, it will require us to define a different relationship. Each customer is able to have multiple orders, but each order can only belong to one customer

# # #                   orders
# | id  |    ORDER_DATE   |     AMOUNT     |    CUST_ID   | <--- new
# |-----|-----------------|----------------|--------------|
# | 687 |      10/1/13    |     $225.00    |     1        |
# | 688 |      10/5/13    |     $200.00    |     2        |
# | 689 |      10/20/13   |     $195.00    |     2        |
# | 690 |      10/25/13   |     $165.00    |     3        |

#notice how we can easily reference all the customer info by including the cust_id FOREIGN KEY

# since one customer can have many orders for any given user we call this a ONE TO MANY RELATIONSHIP

# |CUSTOMERS                     |   <-->    |ORDERS                   |
# |------------------------------|   <-->    |-------------------------|
# |^id INT                       |   <-->    |^ id INT                 |
# |* first_name VARCHAR(45)      |   <-->    |* order_date DATE        |
# |* lane_name VARCHAR(45)       |   <-->    |* amount FLOAT           |
# |** addresses_id INT           |   <-->    |** cust_id INT           |
# |------------------------------|           |-------------------------|
# |indexes-----------------------|   <-->    |indexes------------------|


# What Can We Do with SQL

# Notice how the foreign key  and the id  of the table that we want to combine act as the glue. We can join different tables using SQL. Once again, we will learn how to do this later on but it is important to know that we are setting up these relationships so that we can create customized tables like the illustration below by using SQL to join different tables on the FOREIGN KEY and the PRIMARY ID.

# http://i.imgur.com/SdHYDDl.gif

# Examples 
# One-to-Many is probably the most common relationship you'll encounter while making web applications. Often times a One-to-One relationship is actually much more similar to a One-to-Many. Below are a few examples:

    # Messages and Comments - One Comment belongs to one Message, but one Message can have many Comments.

    # States and Cities - One City is only in one State, but one State can have many Cities.

    # Customers and Orders - One Order only has one Customer, but one Customer can have many Orders.




#                               4) MANY TO MANY
# We have a table that keeps track of each of the orders the customer placed but we haven't created a way to keep track of the items they are ordering.

# # #                   orders
# | id  |    ORDER_DATE   |     AMOUNT     |    CUST_ID   |
# |-----|-----------------|----------------|--------------|
# | 687 |      10/1/13    |     $225.00    |     1        |
# | 688 |      10/5/13    |     $200.00    |     2        |
# | 689 |      10/20/13   |     $195.00    |     2        |
# | 690 |      10/25/13   |     $165.00    |     3        |

#  Below we created an items table to hold the name and description of each item that the customer can order.

# # #                       items
# | id  |      NAME       |            DESC                  |
# |-----|-----------------|----------------------------------|
# | 110 |      iphone 4   |  best phoned deal out there      |
# | 111 |   iphone case   |  protect your phone              |
# | 112 |      apple TV   |  best way to stream multimedia   |
# | 113 |      keyboard   |  wireless kb to use from a far   |
# | 114 |        mouse    |  wireless magic mouse            |
# | 115 |    headphones   | high quality sound in small buds |

# Since each order can have many different items and those same items can show up in many different orders, we have to use a different type of relationship to connect orders to items. ORDERS can have many ITEMS and ITEMS can have many ORDERS, so we call this a Many to Many Relationship.


# In a Many to Many relationship, we create a connector table (also known as a joiner table) that has both the order_id and the item_id so that we can determine all the items in a particular order.

#       items_orders
# |  ORDER_ID  |  ITEM_ID  |
# |------------|-----------|
# |     687    |   110     |
# |     687    |   111     |
# |     688    |   112     |
# |     688    |   115     |
# |     689    |   113     |
# |     689    |   114     |
# |     689    |   115     |
# |     690    |   113     |
# |     690    |   114     |

# here is how we can visualize this kind of relationship

# |ORDERS                   |   <-->   |ITEMS_ORDERS       |   <-->   |ITEMS                  |
# |-------------------------|          |-------------------|          |-----------------------|
# |^ id INT                 |          |                   |          |^ id INT               |
# |* order_date DATE        |   <-->   |*items_id INT      |   <-->   |* name VARCHAR(45)     |
# |* amount FLOAT           |   <-->   |*orders_ID INT     |   <-->   |*desc TEXT             |
# |** cust_id INT           |   <-->   |                   |          |-----------------------|
# |-------------------------|          |-------------------|          |-----------------------|
# |indexes----------------->|   <-->   |indexes----------->|   <-->   |indexes--------------->|

# what we can do with SQL
# http://i.imgur.com/zu3hsWo.gif

# Examples
# Many-to-Many is often the most confusing type of relationship for lots of people, but if you make sure to talk-out the relationship out loud, you'll quickly find if it works or not. Remember, anytime you have a Many-to-Many, it will require some sort of joining table! Check out the below examples and use how we describe the relationship as a guide

    # Users and Interests - One User can have many Interests, one Interest can be applied to many Users.
    # Actors and Movies - One Movie can have many Actors, one Actor can be in many Movies.
    # Businesses and Cities - One Business can be spread across many Cities, one City can be home to many Businesses.