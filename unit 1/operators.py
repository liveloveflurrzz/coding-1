# Assignment operators - exclusively used to 
# assign values to variables.
# think key / value pairings.

# We use single equal sign to represent the assignment
# operator
name = "Jayden"
grade = 10
school = True 

# Arithmetic Operators- Used on numerical
# data types to perfomr calculations.
# intergers (whole numbers) and floats (decimal numbers)

# print is a function that lets is show code
# in the terminal

# Comparison Operators - Set of symbols used 
# to assess if data is the same or different and 
# how they differ

print(10 > 1) # greater than operator
print(2000 < 100) # less than operator

# 2 equal signs compare if something is the SAME
print("book" == "Book") # same as (false)
print ("2" == 2) # same as (false)
print (2.0 == 2) # same as (true)

# not equal is written with ! =
# this is to check and filter for values that are not
# the same
# side note - exclamation ALWAYS means NOT in
# programming
print(200 != 100) # True- these are not the same
print(300 != 300) # False- these are the same


# logical operators- compares 2 condition to check if 
# they are true or false
# conditions = other symbols, we represent these with words:
# and, or, not

# AND - checks if 2 conditions are true, if yes, the final
# result is true
print (3 > 1 and 100 > 50) # this would come out to be true

# OR- checks if only 1 condition is true. if yes,
# the final result will be true
print (3 > 1 or 100 == 50)

# NOT - the "opposite day" operator. it will reverse the
# result of the logical operators
print(not(3 > 1 and 100 > 50))
# this would come out to be false