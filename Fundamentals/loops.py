#range in a loop

#one argument
for i in range(5): #starts at index 0 and stops at index 5
    print(i)
#out put 0 1 2 3 4

#two arguments 
for i in range(2, 7): #arguemnts starts at 2 and stops at 7
    print(i)
    #output is 2-6

#three arguments

for i in range(3,10,2): #starts at 3, stops at 10 BUT increments by 2s
    print(i)
    #output is 3,5,7,9

#to go down increments

for x in range(0, 10, 2):
    print(i)
    #output is 0 2 4 6 8
for x in range (10, 0, -2):
    print(i)
    #output is 10 8 6 4 2
for x in range(5, 1, -3):
    print(i)
    #output is 5 2



#looping over lists & strings

#for loops through strings
for x in "Hello":
    print(x)
    #output is "H", "e", "l", "l", "o"

#for loops through lists
my_list = ["abe", 123, "linc"]
for i in range(0, len(my_list)):
    print(i, my_list[i])
    #output is 0 abe, 1 123, 2, linc

# OR

for v in my_list:
    print(v)
    # output is abe 123 linc


#while loops

#previous for loop
for count in range(0,5):
    print("looping =", count)

#we can write it like
count = 0
while count <= 5:
    print("looping = ", count)
    count +=1 #this tells the while loop to increment by 1 up to desired count

#basic syntax for while loop
while expression: #do something while making the expression false, otherwise memory crash

#else 
y = 3
while y > 0:
    print(y)
    y = y - 1
else:
    print("Final Else Statement")
    #output would be 3 2 1 Final Else Statement

#break
for val in "string":
    if val == "i":
        break #this causes the loop to stop at I since the val is True
    print(val)

#continue
for val in "string":
    if val == "i":
        continue #this stops the loops at "i" and continues after "i"
    print(val)

#more ex

y = 3
while y > 0:
    print(y)
    y = y -1
    if y == 0:
        break #this causes the code to stop at 0 since the condition is True
else: #else will only execute in this case on a clean exit from the loop. break causes it to stop "abruptly"
    print("final")




#lecture examples


# myarr = "a", "b", "c"

# for char in myarr:
#     print(char)

# for i in range(len(myarr)):
#     print(i,myarr[i])

# for i in range(len(myarr),2):
#     print(i, myarr[i])

# sum = 0
# for num in range(0,4):
#     sum += num
#     print(sum)
