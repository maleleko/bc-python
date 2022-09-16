num1 = 42 #variable 42
num2 = 2.3 #variable 2.3
boolean = True #boolean lol
string = 'Hello World' # variable with string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable string array
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable string again
fruit = ('blueberry', 'strawberry', 'banana') #variable string again
print(type(fruit)) # ???
print(pizza_toppings[1]) #will print Sausage
pizza_toppings.append('Mushrooms') #adds mushrooms at the end of string/array
print(person['name']) #will print John 
person['name'] = 'George' #changes name to George
person['eye_color'] = 'blue' #adds eye color in array
print(fruit[2]) #prints banana

if num1 > 45:
    print("It's greater")
else:
    print("It's lower") #<--- will print

if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!") #<--- will print

for x in range(5):
    print(x) #prints 0 1 2 3 4
for x in range(2,5):
    print(x) #prints 2 3 4
for x in range(2,10,3):
    print(x) #prints 2 5 8, increments of 3. why? idk.
x = 0
while(x < 5):
    print(x) #<--- wont stop printing unless a certain condition is met i.e below.
    x += 1 #adds value to x and prints up to 4 from 0.

pizza_toppings.pop() # removes mushrooms
pizza_toppings.pop(1) # removes sausage

print(person) #prints name: John, location: Salt Lake, age: 37, is_balding: false, eye color: blue
person.pop('eye_color') #removes eye_color from array
print(person) #prints name: John, location: Salt Lake, age: 37, is_balding: false

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement') #<--- will print
    if topping == 'Olives':
        break #code stops cause Olives is met

def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times() #prints Hello 10 times

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4) #prints Hello 4 times

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times() #will print Hello 10 times
print_hello_x_or_ten_times(4) #also prints an addition Hello 4 times.


"""
Bonus section
"""

# print(num3) #num3 hasnt been defined yet.
# num3 = 72 <---- will print 72 if print(num3) is below.
# fruit[0] = 'cranberry' <--  replaces blueberry with cranberry
# print(person['favorite_team']) <----- no value given, error.
# print(pizza_toppings[7]) <---- 7 is not defined, error code.
#   print(boolean) <---- prints True
# fruit.append('raspberry') <--- adds raspberry at end of array
# fruit.pop(1) <--- removes strawberry from array
