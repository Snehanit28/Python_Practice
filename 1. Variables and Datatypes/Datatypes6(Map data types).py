"""Mapp data types
     dict -> Collection of key-value pairs (like- {'name': 'Ram', 'age': 25,'city': 'Kathmandu'})
     Keys must be unique and immutable (like- strings, numbers, tuples)"""

person = {'name': 'Ram', 'age': 25, 'city': 'Kathmandu'}  # Dictionary of key-value pairs
print(person)  # => {'name': 'Ram', 'age': 25, 'city': 'Kathmandu'}
print(type(person))  # => <class 'dict'>