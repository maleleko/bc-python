def multiply(num_list, num):
    for x in num_list:
        x *=num
        return num_list
a = [2,4,10,16]
b = multiply(a,5)
print(b)
#output is [2, 4, 10, 16] arrrgh why? it should be [10, 20, 50, 80] lets try to debug

#step 1, step through the code. ask, what runs first? first line is a function so the interpreter runs in this order

def multiply(num_list, num): #don't go inside the function until the function is called
# a = [2,4,10,16]
# b = multiply(a,5) # now our function executes; what is a function call equal to?
# print(b) # and the resulting value is printed

#ask what is my input, and what do i expect as an output. if unexpected results, eliminate all unknowns. try a print statement as the first line.

# def multiply(num_list, num):
    print(num_list, num)
    for x in num_list:
        x *= num
    return num_list
a = [2,4,10,16]
b = multiply(a,5)
print(b)
# output:
#[2, 4, 10, 16] 5
#[2, 4, 10, 16]

#our output confirms that its doing everything weve for so far. add another print under the following line, in this case the for loop

def multiply(num_list, num):
    print(num_list, num)
    for x in num_list:
        print(x)
        x *= num
    return num_list
a = [2,4,10,16]
b = multiply(a,5)
print(b)
# output 
# [2, 4, 10, 16] 5
# 2
# 4
# 10
# 16
# [2, 4, 10, 16]

#ok so our loop is working as intended with each variable being outputted, how do we multiply those individual values? first, let's see if we're changing our x value

def multiply(num_list, num):
    print(num_list, num) #this works as intended
    for x in num_list:
        print(x) #this works as intended
        x *= num
        print(x) #it is indeed mulitplying our individual values
    return num_list
a = [2,4,10,16]
b = multiply(a,5)
print(b)
# output 
# [2, 4, 10, 16] 5
# 2
# 10
# 4
# 20
# 10
# 50
# 16
# 80
# [2, 4, 10, 16]

#so yes its working as intended and changing our values, but what about within our list?
def multiply(num_list, num):
    print(num_list, num) #this works as intended
    for x in num_list:
        print(x) #this works as intended
        x *= num
        print(num_list) #we've found our error.
    return num_list
a = [2,4,10,16]
b = multiply(a,5)
print(b)


#okay so lets search up how to modify OR multiply values in a list during a for loop in python

def multiply(num_list, num):
    for x in range(len(num_list)):
        num_list[x] *= num
    return num_list
a = [2,4,10,16]
b = multiply(a,5)
print(b)

# Learning to use print statements to their greatest advantage and how to correctly search for answers are not one-time skills. You can't just do this assignment and move on, or assume that we'll tell you when you need to use these skills. What we've introduced here is a skill set you'll use for every assignment in all of your code forever. Now is the time to start practicing, because the better you get, the more self-sufficient you become.

#If you ever need help figuring out what to search, try collaborating with your neighbor or asking an instructor to help you out. Always remember the 20 minute rule