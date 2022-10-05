# Lastly, we will need to go to the template and show our information.



# templates/homepage.html

# {% for one_tweet in all_the_tweets %}
#     <h6>{{ one_tweet.creator.name }}</h6> 
#     <a href="/profile/{{ one_tweet.creator.id }}">@{{ one_tweet.creator.handle }}</a>
#     <p>{{ one_tweet.content }}</p>
# {% endfor %}


# Notice how we used the connecting word creator to get information about the User who wrote the Tweet, but did NOT when getting information about the Tweet's content. The word "creator" is coming from the attribute name creator in models/tweet.py in the previous reading.


# This goes back to the Users with Bank Accounts assignment and OOP reading on associating where we had to say:
    # # Does not use connecting word "account", as a BankAccount does not have a name, only a User.
    # self.name 
    # # -----------------------
    # # Uses connecting word "account" to refer to the balance the User has in their associated BankAccount. Also, a User does not have a balance attribute, only a BankAccount does.
    # self.account.balance 


# Sometimes, you will have to make the choice of whether you need to use the connecting word or not when dealing with associated instances. In the specific case of the profile link where we needed an id, why did we use the connecting word creator?

# # In this example, we are using a Tweet's id to go to what is intended to be a User's profile page. Errors are at a high risk, and the chance is low that a link will actually go to the expected User profile.
# <a href="/profile/{{ one_tweet.id }}">...</a> 
# # -----------------------
# # This time, we are using the User's id (specifically, the User that created the Tweet) to link to a User's profile page, this makes much more sense. The class of the information used (a User's id) matches the end destination (a User's page).
# <a href="/profile/{{ one_tweet.creator.id }}">...</a> 


# There may be situations where you want the Tweet’s id instead. For example, what if you wanted to link to a particular Tweet to see what Users had liked the Tweet? Just make sure to think of the end goal of what you are trying to accomplish.

# In these last assignments of this stack, you will have opportunities to incorporate this important concept.



