#1) Basic
for x in range(151):
    print(x)

#2) Multiples of 5
for x in range(5,1005,5):
    print(x)

#3) Counting, the Dojo Way
for x in range(101):
    if x % 10==0:
        print("Coding Dojo")
    elif x % 5==0:
        print("Coding")
    else:
        print(x)

#4) Woah, That sucker's huge.
woah = 0
huge = 0
for woah in range(500000):
    if woah % 2==1:
        huge = huge + woah
print("the sum is", huge)

#solution code, interesting.
sum = 0
for i in range(1,500001,2):
    sum += i
print(sum)


#5) Countdown by Fours
for x in range(2018,0,-4):
    print("hey it's", x)

#while loop practice lol, i did this at first but realized its a *FOR LOOP* assignment not a while loop assignment lol
x = 2018
while x > 0:
    print(x)
    x = x -4



#6) Flexible Counter
lowNum = 2
highNum = 20
multi = 5
for x in range(lowNum,highNum+1):
    if x % multi==0:
        print(x)
#hmm i don think this concept was introduced in the learn platform?