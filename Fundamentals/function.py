#syntax for function is def

#what is a function? 
# 1) a block of code designed to execute a specific task whenever it is called 
# 2) a function can be said to take in raw materials and return a finished product
# a function should be used any time a set of code is to be reused

#why use a function?
#1) so we can reuse code
#2) to improve clarity by modularizing code for individual repeatable tasks.



#examples
def add(a,b): #function name add: parameters a and b
    x = a + b 
    return x

#calling/invoking the function
new_val = add(3,5) # calling the add function, with arguments 3 and 5
print(new_val) # the result of the add function gets sent back to and saved into new_val, so we will see 8



#parameters/arguments

#whats the difference between paramerters and arguments?
#1) an argument is passed in when a function is called. A parameter is defined during function creation and works a lot like a variable.
#2) A parameter is a container. An argument is a value.

#examples
def say_hi(name): #parameter
    print("hi, " + name)

##invoking the function 3 times, passing in one argument each time
say_hi('Maleko') #<- argument
say_hi('Cedric')
say_hi('Harrison')
##with ex above, 'name' is the parameter and 'maleko' is the argument

##i assume code would look like this
def say_hi(name):
    print("hi, " + name)
say_hi('Maleko')

#can i do it like this?
# def say_hi(name):
#     say_hi('Maleko')
#     print('hi, ' + name)
#     #no i cant

#returning values

#we modify the above code
def say_hi(name): #<-- we are invoking/calling the function with a parameter
    return "Hi, "+ name #this is new, we are returning our value
greeting = say_hi("Maleko") #<---- 'maleko' is the parameter's argument we are passing it
print(greeting)

#returning the value from the function allows us to store it in a variable. we invoked the function with 'Maleko' and set it to the GREETING variable.
#if we print this function, we get "Hi, Maleko"


#predict the output
#ex
def add(a, b): #<-- this is our parameter, we have two
    x = a + b #this is our variable
    return x #we are returning this values within our function
sum1 = add(4,6) #<-- assigning arguments to our function, this result will be 10
sum2 = add(1,4) #<-- more arguments, this result would be 5
sum3 = sum1 + sum2 #desired sum3 output should be 15 if we print
print(sum3)

#return also means EXIT, reaching a return statement says EXIT THIS FUNCTION NOW PLS & print() is used for DEBUGGING and seeing if things are working as they should

#function w/ multiple variables prac

def full_name(): #<- no parameter?
    return 'Maleko', 'koh', 'Osby' #<-- is this acting as my parameter?
name1, name2, name3 = full_name() #<--- wouldn't this technhically be considered an argument?
print("my full name is, " + name1, name2, name3) #output is "my full name is, Maleko koh Osby"

def say_hi(name, name2, name3): #<- parameter
    return "hi, " + name + name2 + name3 #<-- DONT COMMA, it will tuple
ayo = say_hi('maleko ', 'osby ', 'works now?') #<- argument
print(ayo) #prints as expected


#some funkin around
def say_hi(name, name2, name3):
    return "hi, " + name + name2 + name3
    # print(f"hello {name}, {name2}, {name3}") # doesnt work how we want it to, close though
ayo = say_hi('maleko ', 'koh ', 'osby')
print(ayo)