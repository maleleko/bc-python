# What all coding languages have in common is the ability to interpret some code and give a result (Output).  The result can be a variety of different results, including print statements, data types, html/css/javascript to render on a browser, etc.  Many times, we write our code to work with a certain set of data, but the data could be different in different situations.  In this case, we set up to pass an input to our code, so the interpreter can work with that data.  In the days to come, we will learn how we can pass inputs to functions by setting up a parameter and passing an argument at the function call, and how a user Request will include an input from the Client that is passed to the Server, but for now we will look into the input() function in Python which will allow us to interact with the bash window.

# favorite_color = input("What is your favorite color?") #input takes a prompt, which needs to be a string.

# print(f"Your favorite color is: {favorite_color}") #output prints the color given to the console.

# Put this line of code in a Python and run the file in the terminal/shell.  You will see a prompt that appears, and the print() statement will not be executed until you enter a name.  This program is expecting an input, and can not move forward until it is provided.

# We will use both input() and print() in the assignments to show different results with our code.  The following video will have an example of how we will use them. You can download the demo code on the link below.

import random

answers = []

def bridge_keeper():
    
    questions = ["What is your favourite colour?", "What is the airspeed velocity of an unladen swallow?","What is the capital of Assyria?"]
    correct_answer = "African or European?"

    print("STOP!!!!\nThose who approach the Bridge of Death must answer me these questions three, ere the other side they see.\n")
    # the built in input function can prompt with a string, and then return whatever the user has input into the console as a string.  Even if it's a number!!!
    name = input("What is your name?\n")
    quest = input("What is your quest?\n")
    random_question = random.randint(0,len(questions)-1)
    third = input(f"{questions[random_question]}\n")

    # What is your favourite colour?
    if random_question == 0:
        # checks to see if the color has been guessed already.
        if third in answers:
            print("You have been casted into gorge!!!\n")
            return True
        else:
            answers.append(third)
            print("Right. Off you go.\n")
            return True
    # What is the velocity of an unladen swallow?
    elif random_question == 1:
        if third == correct_answer:
            print("Wait... I don't know.  AHHHHHHH!!!!!!\nThe bridge keeper was casted into the gorge.")
            return False
        else:
            print("You have been casted into gorge!!!\n")
            return True
    # What is the capital of Assyria?
    elif random_question == 2:
        # checks for correct answer
        if third == "Ninevah":
            print("Right. Off you go.\n")
            return True
        else:
            print("You have been casted into gorge!!!\n")
            return True

isGuessing = True

while isGuessing == True:
    isGuessing = bridge_keeper()