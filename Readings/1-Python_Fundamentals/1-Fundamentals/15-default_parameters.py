#set defaults when declaring the parameters
def be_cheerful(name='', repeat=2):
    print(f"good morning {name}\n" * repeat)
be_cheerful() #output - good morning | x2
be_cheerful('tim') #output - good morning tim | x2
be_cheerful(name='john') #output - good morning john | x2
be_cheerful(repeat=6) #output - good morning | x6
be_cheerful(name='michael', repeat=5) #output - good morning michael | x5



#Note all the different ways we are able to call on this one function! Even though our function defines 2 parameters, if:

# 1) no arguments are provided -- the defaults are used

# 2) one UNNAMED argument provided -- provided value is used as the value for the first parameter, and the second parameter's default value is used

# 3) one NAMED argument provided -- provided value is used as the value of the parameter of the same name, and the other parameter's default value is used

# 4) both UNNAMED arguments provided -- values assigned to parameters in order (i.e. what we've been doing up to this point)

# 5) both NAMED arguments provided -- values are assigned to associated parameter (and then order doesn't matter!)