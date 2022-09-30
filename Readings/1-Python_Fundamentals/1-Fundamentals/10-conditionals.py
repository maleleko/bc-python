#conditional keywords if, elif, and else.
x = 12
if x > 50:
    print("bigger than 50")
else:
    print("smaller than 50")

#will print the else because 12 is less than 50

x = 55 
if  x > 10:
    print("bigger than 10")
elif x > 50:
    print("bigger than 50")
else:
    print("smaller than 10")

#since x is greater than both 10 and 50, the first statement will be the one that executes. we will see only "bigger than 10"

if x < 10:
    print("smaller than 10") #nothing happens here cause statement is false.



#comparison and logic ops

# == checks if the value of two operands are equal - 1 == 2 => False | 1 == 1 => True

# != checks if the value of two operands are not equal. - 1 != 2 => True | 1 !=1 => False

# > checks if the value is greater - 1 > 2 => False | 2 > 1 => True

# < checks if the value is less 1 < 2 => True | 2 < 1 => False

# >= checks if value is greater or equal to the value
#  1 >= 2 => False | 2 >= 2 => True

#-

# <= checks if value is less than or equal to the value
#  1 <= 2 >> True | 2 <= 2 => True

#-

# *and* checks if either the expression on the left and right are both true
# (1 <= 2) and (2 <= 3) => True  | 
# (1 <= 2) and (2 >= 3) => False | (1 >= 2) and (2 >= 3) => False

# *or* checks if either the expression on the left or right is True (1 <= 2) or (2 >= 3) => True | (1 <= 2) or (2 <= 3) => True | (1 >= 2) or (2 >= 3) => False

# *not* reverses the true-false value of the operand 
# not True => False | not False => True | not 1<-2 -< True | not 1 <= 2 => False
# not (1 <=2 and 2 >=3) => True | not 1 <= 2 and 2 >=3 +> False