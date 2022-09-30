
#if
a = 1
b = 2
c = 3
if a < b:
    print("a is less than b")
if c > b:
    print("i think c is greater than b")


#if and else
d = 4
e = 5
if d < e:
    print("d is less than e")
else: 
    print("c is NOT less than d")
    print("I don't think c is less than d")
print("outside the if else block")


#if, else if, and else.
f = 8
g = 7
if f < g:
    print("f is less than f")
elif f == g:
    print("f is equal to g") 
elif f + 10 > g:
    print(f+10, ">", g,)
    print("F is greater than G by more than 10")
else:
    print("f is greater than g")


#if inside of else
g = 7
h = 8
if g < h:
    print("g is less than h")
else:
    if g == h:
        print("g is equal to h")
    else:
        print("g is greater than h")

#bmi calc
name = "Maleko"
height_m = 1.8
weight_kg = 79

bmi = weight_kg / (height_m * height_m) #or (height_m ** 2)
print("bmi:", bmi)
# print(bmi)
if bmi < 25:
    print(name, "is not overweight")
    #print("is not overweight")
else: 
    print(name, "is overweight")
    #print("is overweight")