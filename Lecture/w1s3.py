#lecture playground



# students = [ 
#     {"name": "test1", "age": 21, "stacks": ["python", "java", "mern"]},
#     {"name": "test2", "age": 40, "stacks": ["python", "java", "mern"]},
#     {"name": "test3", "age": 20, "stacks": ["python", "java",]},
#     {"name": "test4", "age": 50, "stacks": ["python",]},
# ]

# for element in students:
#     # print("the student is?????", element["name"], element["stacks"])
#     for stack in element["stacks"]:
#         print(stack)



#functions in python
#def <--- defining function syntax

def function_name():
    pass
    #creating function
function_name()
#calling function, MUST invoke the function with parenthesis

#func example
def say_hi():
    print("hi, ")
say_hi()

def greet(name): #(name) is the parameter
    print(f"Hello, {name}")

#pass the statement like this below
greet('Maleko') #<--- requires argument which is 'Maleko'

#code will look like
def say_hi(name):
    print(f"hi, {name}")
say_hi('Maleko')


#variables

def sum(a, b):
    return a + b
value = sum(4, 5)
print(value)



def fizz_buzz(num):
    result = []
    for i in range(1, num +1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("fizzbuzz")
        elif i % 5==0:
            result.append("buzz")
        elif i % 3==0:
            result.append("fizz")
        else:
            result.append(i)

    return result
theresult = fizz_buzz(30)
print(theresult)
