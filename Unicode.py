# String and Type Conversion in Python
#unicode values
print(ord('A'))  # => 65
print(chr(65))     # => 'A'

print(ord('a'))  # => 97
print(chr(97))     # => 'a'

print(ord('@'))  # => 64
print(chr(64))     # => '@'

print(ord('😊'))  # => 128522
print(chr(128522)) # => '😊'

print(ord('👍')) # => 128077
print(chr(128077)) # => '👍'

# print(ord('Sneha Saha'))  
# TypeError: ord() expected a character, but string of length 10 found

print(ord('A'))  # the ascii value of 'A' is 65
print(ord('B'))  # the ascii value of 'B' is 66 
print(ord('a'))  # the ascii value of 'a' is 97
print(ord('b'))  # the ascii value of 'b' is 98
print('A' < 'B')  # => True 65 < 66
print('a'<'b')   # => True 97 < 98
print('A' > 'a')  # => False 65 > 97
print('B' > 'a')  # => False 66 > 97
print('ABD' < 'ABC')  # => False 65 < 65, 66 < 66, 68 > 67
print('ABD' > 'ABC')  # => True 65 < 65, 66 < 66, 68 > 67
print('abc' < 'bcd')  # => True 97 < 98, 98 < 99, 99 < 100

# We compare string with srting not with int or float

