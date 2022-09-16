#list example
ninjas = ['Rozen', 'KB', 'Oliver']
my_list = ['4', ['list', 'in', 'a', 'list'], 987]
empty_list = []


#combining lists
fruits = ['apple', 'banana', 'orange', 'strawberry']
vegetables = ['lettuce', 'cucumber', 'carrots']
fruits_and_vegetables = fruits + vegetables #makes variable by combining 2 sep variables
print(fruits_and_vegetables) 
salad = 3 * vegetables #pretty much prints veg list 3 times
print(salad)


#list manipulation
drawers = ["documents", "envelopes", "pens"]
    
# access the drawer with index of 0 and print value
print(drawers[0])  #prints documents
# access the drawer with index of 1 and print value
print(drawers[1]) #prints envelopes
# access the drawer with index of 2 and print value
print(drawers[2]) #prints pens
    
# replace "documents" with "tchotchkes"
drawers[0] = "tchotchkes"
print(drawers) # prints ["tchotchkes", "envelopes", "pens"]
    
# stores the value "tchotchkes" in a temporary variable.
top_contents = drawers[0]
    
# Replaces the value at index 1
# with whatever value is stored at index 0
drawers[1] = drawers[0]
print(drawers) # prints ["tchotchkes", "tchotchkes", "pens"]



#appending values to list with whatevervar.append(whatever)
nums = [1,2,3,4,5]
nums.append(99)
print(nums)
#the output would be [1,2,3,4,5,99]



#slicing - uses ":" in brackets [:]
words = ["hmm", "i'm", "kinda", "tired"]
print(words[0:]) #this prints up to "hmm" and stops
print(words[:2]) #this prints everything before "kinda"(index 2) and stops before reaching the index
print(words[1:3]) #this starts at (index 1) "i'm" and prints everything between the assigned index (index 3 "kinda")

copied_words = words[:]
copied_words.append("*yawns*")
print(copied_words)
print(words)



#sample code from platform
words = ["start","going","till","the","end"]
# Sub-ranges (portions) of the list
print(words[1:]) # prints ['going', 'till', 'the', 'end']
print(words[:4]) # prints ['start', 'going', 'till', 'the']
print(words[2:4]) # prints ['till', 'the']

# Making a copy of a list
copy_of_words = words[:]
copy_of_words.append("dojo") # only appends to the copy
print(copy_of_words) # prints ['start', 'going', 'till', 'the', 'end', 'dojo']
print(words) # prints ['start', 'going', 'till', 'the', 'end']




#built in functions for lists
#len seq ex
my_list = [1, 'Zen', 'yo']
print(len(my_list))
#prints 3

#more ex
# print(max(my_list))
# print(min(my_list))
# print(sorted(my_list))

#list specific methods
my_num = [1,16,999,9]
my_num.pop() #removes last value
print(my_num)

my_num.pop(2)
print(my_num)

my_num.append(20) #adds new value at end
print(my_num)

my_num[3] = 15 #replaces the 3rd index with new 
print(my_num)

my_num.reverse() #reverses
print(my_num)

my_num.sort() #sorts form least to greatest
print(my_num)


#tuples are immutable, meaning they can't be changed.

#ex
tuple_data = ('physics', 'chem', 1969, 1996)
tuple_nun = (1,2,3,4,5)
tuple_letters = "a", "b", "c" "d"

#its conventional to enclose tuples with parenthesis
dog = ("canis familiaris", "dog", "carnivore", 12)

#negative index
my_arr = ["a", "b", "c"]
print(my_arr[-1]) #prints the last index

my_arr.insert(1, "m") #inserts at the called index, pushing the previous index over by 1.
print(my_arr) #outputs['a' 'm' 'b' 'c']