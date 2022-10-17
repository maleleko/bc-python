                    # Http Request-Response Cycle

# We know as developers that we can make requests to a server and it responds back with HTML , CSS , and JavaScript to display a web page.  While this is how most user interactions happen, we as developers may not always want the actual website . . .maybe we want just the data.

# We can utilize the Request-Response Cycle with a built in JavaScript method called Fetch.


                    # Fetch Method

# The fetch method can make a GET request to an API server, and "get" some data sent back to us.  We can achieve this in two different ways, via a Promise or Async/Await. 

# Let's use the Github API as an example:

    # Using Promises:
        # fetch("https://api.github.com/users/adion81")
        # .then(response => response.json() )
        # .then(coderData => console.log(coderData) )
        # .catch(err => console.log(err) )

# Using promises looks almost like a chain reaction.  We make the request using fetch, then we wait for the data to come back, then we convert it to JSON. If there are any errors with the request, we can attach a catch to see the errors coming back.

# Note: If you noticed the arrow syntax in the code above, those are called arrow functions.  Simply put, they are a more compact way of expressing a function.  For more documentation on Arrow Functions.
    # https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions


    # Using Async/Await:
    #     async function getCoderData() {
    #     var response = await fetch("https://api.github.com/users/adion81");
        #     The await keyword lets js know that it needs to wait until it gets a response back to continue.
    #     var coderData = await response.json();
        #    We then need to convert the data into JSON format.
    #     return coderData;
    # }
        
    # console.log(getCoderData());

# When using Async/Await we apply the async keyword to the function, and we must wait for the data to come back.  In order accomplish and ensure that we always return the data after it comes back we use the await keyword.  

# If we run both of these functions in our JavaScript file, we will get back the same result. Both are using asynchronous behavior to get data back to us the developer. 

# More documentation on Promises and Async/Await.
    # Promises: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

    # Async/Await: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function