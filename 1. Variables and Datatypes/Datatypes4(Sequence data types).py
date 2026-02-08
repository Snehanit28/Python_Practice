"""Sequence data types
     str -> Sequence of characters (like- "Hello", 'Ram', "1234")
     list -> Ordered collection of items (like- [1, 2, 3], ['a', 'b', 'c'])
     tuple -> Ordered collection of items (like- (1, 2, 3), ('a', 'b', 'c'))
     range -> Sequence of numbers (like- range(0, 10)) """

name = "Ram is learning Python"
fruits = ['apple', 'banana', 'cherry']  # List of strings
Fruits = ('apple', 'banana', 'cherry') # Tuple of strings
num_range = range(0, 10)
# Difference between list and tuple is that
#      list is mutable (can be changed)
#      whereas tuple is immutable (cannot be changed)

added_fruit = 'orange'
fruits.append(added_fruit)  # Adding item to list
removed_fruit = fruits.pop(0)  # Removing item from list
changed_fruit = fruits[0] = 'mango'  # Changing item in list
removed_fruit = Fruits[0]  # Accessing item from tuple (cannot add or remove)

print(name)        # => Ram is learning Python
print(fruits)     # => ['mango', 'cherry', 'orange']
print(Fruits)    # => ('apple', 'banana', 'cherry')
print(num_range)  # => range(0, 10)
print(type(name), type(fruits), type(Fruits), type(num_range)) 
# => <class 'str'> <class 'list'> <class 'tuple'> <class 'range'>
