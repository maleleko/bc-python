

#practice not part of assignment
# def convert(miles):
#     return 1.6 * miles
# convert(5)
# print(convert(5), "km is equal to 5 miles")

#1) Countdown --- thank you svet for help
def countdown(num):
    list = []
    for down in range(num,0-1,-1):
        list.append(down)
    return list
countdown(5)
print(countdown(5))

#2) Print and Return 
def printreturn(list):
    # list = [6,9]
    print(list[0])
    return list[1]
# printreturn([6,9])
print(printreturn([6,9]))

#3) First Plus Length
def firstpluslen(list):
    list = [1,2,3,4,5]
    print(len(list) + list[0])
    return list
firstpluslen([1,2,3,4,5])

#or

def firstpluslen(list):
    return len(list) + list[0]
print(firstpluslen([1,2,3,4,5]))

#whats the difference? snippet 1 would probably return [1,2,3,4,5] instead of returning what we actually want which would be adding our first idex to our length of the list

#4) Values greater than Second
def valuesgreater(list):
    if len(list) < 2:
        return False
    count = []
    for i in range(0, len(list)):
        if list[i] > list[1]:
            count.append(list[i])
    print(len(count))
    return count
print(valuesgreater([3]))
print(valuesgreater([5,2,3,2,1,4]))

#5) This Length, That Value
def thislengththatval(size,value):
    arr = []
    for i in range(0, size):
        arr.append(value)
    return arr
print(thislengththatval(4,7))
print(thislengththatval(6,2))