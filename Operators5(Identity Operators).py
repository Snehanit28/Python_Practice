# Identity Operators: Used to compare the memory locations of two objects.

"""Identity Operators:
     is     -> Returns True if both variables point to the same object
     is not -> Returns True if both variables point to different objects"""

a = [1, 2, 3]
b = a  # b references the same list object as a
c = [1, 2, 3]  # c is a new list object with the same content as a
print(a is b)      # => True, because both a and b point to the same object
print(a is c)      # => False, because a and c point to different objects
print(a is not b)  # => False
print(a is not c)  # => True

# Bitwise Operators: Used to perform bit-level operations on integers.
# Relational Operators: Used to compare values and determine their relationship (greater than, less than, etc.).
# Membership Operators: Used to check if a value is present in a sequence (like lists, strings, etc.).