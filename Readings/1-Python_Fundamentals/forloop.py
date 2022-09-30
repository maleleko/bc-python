# 1. Python for loop to iterate through the letters in a word
for i in "pythonista":
    print(i)

# 2. Python for loop using the range() function
for j in range(5):
    print(j)

# 3. Python for loop to iterate through a list
AnimalList = ['Cat','Dog','Tiger','Cow']
for x in AnimalList:
    print(x)

# 4. Python for loop to iterate through a dictionary
programmingLanguages = {'J':'Java','P':'Python'}
for key in programmingLanguages.keys():
    print(key,programmingLanguages[key])

programmingLanguages = {'J':'Java','P':'Python'}
for key,value in programmingLanguages.items():
    print(key,value)

# 5. Python for loop using the zip() function for parallel iteration
a1 = ['Python','Java','CSharp']
b2 = [1,2,3]

for i,j in zip(a1,b2):
    print(i,j)

# 6. Using else statement inside a for loop in Python
flowers = ['Jasmine','Lotus','Rose','Sunflower']
for f in flowers:
    print(f)
else:
    print('Done')

# 7. Nested for loops in Python (one loop inside another loop)
list1 = [5,10,15,20]
list2 = ['Tomatoes','Potatoes','Carrots','Cucumbers']

for x in list1:
    for y in list2:
        print(x,y)

# 8. Using break statement inside a for loop in Python
vehicles = ['Car','Cycle','Bus','Tempo']

for v in vehicles:
    if v == "Bus":
        break
    print(v)

# 9. Using continue statement inside a for loop in Python
vehicles = ['Car','Cycle','Bus','Tempo']

for v in vehicles:
    if v == "Bus":
        continue
    print(v)

# 10. Python for loop to count the number of elements in a list
numbers = [12,3,56,67,89,90]
count = 0

for n in numbers:
    count += 1

print(count)

# you can use len(numbers) also to get the count

# 11. Python for loop to find the sum of all numbers in a list
numbers = [12,3,56,67,89,90]
sum = 0

for n in numbers:
    sum += n

print(sum)

# 12. Python for loop to find the multiples of 5 in a list
numbers = [2,5,6,10,15,20,25]

for n in numbers:
    if n%5 == 0:
        print(n)

# 13. Python for loop to print a triangle of stars
for i in range(1,5):
    for j in range(i):
        print('*',end='')
    print()

# 14. Python for loop to copy elements from one list to another
list1 = ['Mango','Banana','Orange']
list2 = []
for i in list1:
    list2.append(i)
    
print(list2)

# 15. Python for loop to find the maximum element in a list
numbers = [1,4,50,80,12]
max = 0

for n in numbers:
    if(n>max):
        max = n
        
print(max)

# 16. Python for loop to find the minimum element in a list
numbers = [1,4,50,80,12]
min = 1000

for n in numbers:
    if(n<min):
        min = n

print(min)

# 17. Python for loop to sort the numbers in a list in ascending order
numbers = [1,4,50,80,12]

for i in range(0, len(numbers)):    
    for j in range(i+1, len(numbers)):    
        if(numbers[i] > numbers[j]):    
            temp = numbers[i]   
            numbers[i] = numbers[j];    
            numbers[j] = temp 

print(numbers)

# 18. Python for loop to sort the numbers in a list in descending order
numbers = [1,4,50,80,12]

for i in range(0, len(numbers)):    
    for j in range(i+1, len(numbers)):    
        if(numbers[i] < numbers[j]):    
            temp = numbers[i]   
            numbers[i] = numbers[j];    
            numbers[j] = temp 

print(numbers)

# 19. Python for loop to print the multiples of 3 using range() function
# printing multiples of 3 till 20

for i in range(3,20,3):
    print(i)

# 20. Python for loop to print the multiples of 5 using range() function
# printing multiples of 5 till 20

for i in range(5,20,5):
    print(i)

# 21. Python for loop to print the numbers in reverse order using range() function
for i in range(10,0,-1):
    print(i)