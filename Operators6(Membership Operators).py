# Membership Operators: Used to check if a value is present in a sequence (like lists, strings, etc.).

"""Membership Operators:
     in     -> Returns True if a value is found in the sequence
     not in -> Returns True if a value is not found in the sequence"""

fruits = ['apple', 'banana', 'cherry']
print('banana' in fruits)      # => True, because 'banana' is in the list
print('grape' in fruits)       # => False, because 'grape' is not in the list
print('banana' not in fruits)  # => False
print('grape' not in fruits)   # => True

