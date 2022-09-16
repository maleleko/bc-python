print("Hello World!")

x = "Hello Python"
print(x)
y = 42
print(y)

# comma, *spaces.*
name = "Maleko"
print("My name is", name)

# concatenate, no space. doesnt work on ints
name = "Maleko"
print("My name is " + name)

#mixture of comma and concatenate
username = "Maleko"
num = 18
print("My username is " + username, num)

#making an int, a string
num = 96
name = "Maleko"
print("My username is " + name + str(num))
#or
num = 96
name = "Maleko"
print("My USERNAME is " + name + str(96))

#f-string interpolation
first = "Maleko"
last = "Osby"
age = 25
print(f"My name is {first} {last} and I am {age} years old.")

#string.format()
first = "Maleko"
last = "Osby"
age = 25
print("My NAME IS {} {} and I am {} YEARS old.".format(first, last, age))

#% formatting
#%'s are used to indicate a placeholder. %s for string %d for number.
hw = "Hello %s" % "world"
py = "I love Python %d" % 3
print(hw, py)

name = "Maleko"
age = 25
print("My name is %s and I'm %d" % (name, age), "years old")
# this is so ugly and confusing. glad it's easier nowadays.
# USED IN JAVA LOL F ME

# built-in string methods
x = "Hello world"
print(x.title())
#don't know when this will prove useful but its good to have.

a = 1
b = 3
print(a, b)

# swapping variables
v1 = "first string"
v2 = "second string"
temp1 = v1
temp2 = v2

v1 = temp2
v2 = temp1
print(v1, v2)

#or
v1 = "first string"
v2 = "second string" 
temp = v1 #using temp var to store line 74 as v1 - give it a value of "first string"
v1 = v2 #swapping v1 value to v2 value which is "second string"
v2 = temp #using v2 to match current temp value which is "first string"
print(v1, v2)