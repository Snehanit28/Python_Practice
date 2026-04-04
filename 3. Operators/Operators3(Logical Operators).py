# Logical Operators: Used to combine multiple boolean expressions.

"""Logical Operators:
     and -> Logical AND
     or  -> Logical OR
     not -> Logical NOT"""

age = 25
has_license = True
a=10
b=5
c=0
d=15

# Examples of Logical Operators
print(True and True)    # => True
print(True and False)   # => False  
print(False and True)   # => False
print(False and False)  # => False
print("1.1-----")
print(a > 12 and b < 4)  # => False
print(a > 12 and b > 4)  # => False
print(a < 12 and b < 4)  # => False
print(a < 12 and b > 4)  # => True
print("1.2-----")
print(age > 18 and has_license)  # => True
print(age < 18 and has_license)  # => False
print(age > 18 and not has_license)  # => False
print(age < 18 and not has_license)  # => False
# In logical AND if both are True then only it returns True.
print("1.3-----")
print("-----")

# Examples of Logical OR
print(True or True)    # => True
print(True or False)   # => True
print(False or True)   # => True
print(False or False)  # => False
print("2.1-----")
print(a > 12 or b < 4)  # => False
print(a > 12 or b > 4)  # => True
print(a < 12 or b < 4)  # => True
print(a < 12 or b > 4)  # => True
print("2.2-----")
print(age > 18 or has_license)   # => True
print(age < 18 or has_license)   # => True
print(age > 18 or not has_license)  # => True 
print(age < 18 or not has_license)   # => False 
#In logical OR if both are False then only it returns False.
print("2.3-----")
print("-----")

# Examples of Logical NOT
print(not True)    # => False
print(not False)   # => True
print("3.1-----")
print(not (a > b))  # => False
print(not (a < b))  # => True
print("3.2-----")
print(not (age > 18))  # => False
print(not (age < 18))  # => True    
# Logical NOT reverses the boolean value.
# if the condition is True it returns False and if the condition is False it returns True.
print("3.3-----")
print("-----")

# Assignment Operators: Used to assign values to variables.
# Bitwise Operators: Used to perform bit-level operations on integers.
# Relational Operators: Used to compare values and determine their relationship (greater than, less than, etc.).
# Membership Operators: Used to check if a value is present in a sequence (like lists, strings, etc.).
# Identity Operators: Used to compare the memory locations of two objects.