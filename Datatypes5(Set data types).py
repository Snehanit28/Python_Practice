"""Set data types
     set -> Unordered collection of unique items (like- {1, 2, 3}, {'a', 'b', 'c'})
     frozenset -> Immutable set (like- frozenset({1, 2, 3}))
     Immutable means that the items of frozenset cannot be changed after creation.
     Sets are used to store multiple items in a single variable,
     and they automatically remove duplicate items.
     """
unique_numbers = {1,1,5,1,2,4,2,3,3,4,4,4,4}  # Set of unique numbers
print(unique_numbers)  # => {1, 2, 3, 4, 5}
print(type(unique_numbers))  # => <class 'set'>
added_number = 6
unique_numbers.add(added_number)  # Adding item to set
removed_number = unique_numbers.remove(2)  # Removing item from set
print(unique_numbers)  # => {1, 3, 4, 5, 6}

immutable_set = frozenset([1,2,2,3,4,4,5,5])  # Frozenset of unique numbers
print(immutable_set)  # => frozenset({1, 2, 3, 4, 5})
print(type(immutable_set))  # => <class 'frozenset'>
# immutable_set.add(6)  # This will raise an AttributeError
# immutable_set.remove(2)  # This will raise an AttributeError   
# Uncommenting above two lines will show that frozenset is immutable
