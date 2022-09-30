# conisder the following tables


#               customers
# id | firstName | lastName | address      |
# ------------------------------------------
# 1  | randall   | frisk   | 576 steel in |
# 2  | michael   | choi     | 333 ninja dr |
# 3  | dexter    | clark    | 978 flip in. |

# Although each customer can only have one address, it would seem more fitting and better organized if we separate out the address and put it in its own table. We can then keep better track of specific information about a given address without the fear of our table getting too large to manage.

#                   customers
# |id | firstName | lastName | address_id  |
# |---------------|----------|-------------|
# | 1 | randall   | frisk    |     4       |
# | 2 | michael   | choi     |     5       |
# | 3 | dexter    | clark    |     6       |


#                   addresses
# id |      Street     |      city      |     state    |
# ---|-----------------|----------------|--------------|
# 4  | 576 steel in    |  Grass valley  | 576 steel in |
# 5  | 333 ninja dr    |    Seattle     | 333 ninja dr |
# 6  | 978 flip in     |    San Jose    | 978 flip in. |

# Since each address that we have can only belong to a single customer and each customer can only have one address, we call this a One to One Relationship.

# We can visualize the relationship between the customer and address records like this:

# |customers                     |   <-->    |addresses                    |
# |------------------------------|   <-->    |-----------------------------|
# |id INT                        |   <-->    |* street VARCHAR(45)         |
# |* first_name VARCHAR(45)      |   <-->    |* city VARCHAR(45)           |
# |* lane_name VARCHAR(45)       |   <-->    |* state VARCHAR(45)          |
# |** addresses_id INT           |   <-->    |* zipcode INT                |
# |------------------------------|           |-----------------------------|
# |indexes-- --------------------|   <-->    |indexes----------------------|



# What Can We Do with SQL

# Even though we split up our tables into two different tables, we can combine them into one using SQL. No need to know how to do this yet, but it is important to see how a table can be joined as long as there is a foreign key that references another table's id. We'll cover actual SQL syntax in the next chapter.
# http://i.imgur.com/0Bw6pb7.gif




# Examples of One-to-One
# The easiest way to check to see if your relationship makes sense for your data is to simply talk through the relationship out loud.
# Remember that relationships go in two directions. For example, one address has only one ZIP code, but one ZIP code can have many addresses, thus making it a different type of relationship.

# some sample one to ones
    # Customers and Credit Cards | Every Customer has one Credit Card, every Credit Card belongs to one Customer.

    # User and Email  | Every User has one Email Address, every Email Address has one User.

    # Product and Image | Every Product has an Image, every Image is of a Product.