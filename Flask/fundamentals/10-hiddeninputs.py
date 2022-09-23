#                   Hidden Inputs


# Hidden input fields are form fields that are hidden from the user. 
# Hidden input is used, along with other input elements, to transfer information between different pages.

# A hidden input is just an ordinary input element, but has no visual representation in the rendered HTML.

# <input type="hidden" name="action" value="register">

# There are multiple ways we can make use of the hidden input field. In this tab, we are going to look at just one example. Suppose we have two forms within our index page:

    # <form method="post" action="/process">
    #     <input type="hidden" name="which_form" value="register">
    #     <input type="text" name="first_name">
    #     <input type="text" name="last_name">
    #     <input type="text" name="email">
    #     <input type="password" name="password">
    #     <input type="submit" value="Register">
    # </form>
    # <form method="post" action="/process">
    #     <input type="hidden" name="which_form" value="login">
    #     <input type="text" name="email">
    #     <input type="password" name="password">
    #     <input type="submit" value="Login">
    # </form>

# Notice that both forms submit their data to the POST /process route. How will we know which form was submitted? Each of the forms also has a hidden input with the same name, but different values. In this example, we are using the name "which_form".

# In the POST /process route, we could do something like this to process appropriately depending on which form was submitted:

    # if request.form['which_form'] == 'register':
    #   //do registration process
    # elif request.form['which_form'] == 'login':
    #   //do login process


# But know that, even though hidden inputs are invisible to the user, it is actually very visible in the page's source. That means other users can still see and change the values you set in the hidden input. So be very careful in choosing what data you store in there as value, and set appropriate actions if a user tries to change or remove it.