# Some APIs require an API Key to access information. This is due to the creators of these APIs wanting to monitor your use of their API, in regards to how often you access their information, when you access their information and which information you are accessing. Some APIs even put a limit on how often you can access them and how many times in a day you're allowed to use them. APIs are all about information. Just imagine if you built your own API and allowed anyone to access your hosted API. This is great for you, you get to have people use this data you laid around. These other developers are making super cool apps and making a lot of money on their amazing websites but they are using your information and doing so for free. Wouldn't it be better to let them have limited access, say make 5000 requests per day to your API, and if they want to have more frequent access; they just pay a monthly fee. That's where the API key comes in.


                # Getting an API Key

# In order to get an API key, let's use the Open Weather API as an example.

# You'll need to sign up for a free account at  http://openweathermap.org/api. Your profile will then be attached to a unique key, which you will add to the end of your URL request in the following format:
        # http://api.openweathermap.org/data/2.5/forecast/daily?id=524901&APPID={INSERTAPIKEY}
        # // Make sure to put your unique API key in the URL (taking out the brackets).
        # // &APPID={INSERTAPIKEY} will need to be at the end of each URL you access below and in the assignment.


# Now every single request you send to this API will have to include that API Key you were given. From here on out you can assume you will have to use an API Key for just about every API out there. Most APIs will have a free tier that allows devs to play around with their data.

