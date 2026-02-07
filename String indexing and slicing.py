# string indexing

str1 = "Hello, World!"
print(str1[0])    # => 'H'
print(str1[7])    # => 'W'
print(str1[-1])   # => '!'
print(str1[-5])   # => 'o'

# string slicing
print(str1[0:5])  # => 'Hello'
print(str1[7:12]) # => 'World'
print(str1[:5])   # => 'Hello'
print(str1[7:])   # => 'World!'
print(str1[:])    # => 'Hello, World!'
print(str1[-13:-8]) # => 'Hello'    
print(str1[::2])  # => 'Hlo ol!' (0-last, step 2)
print(str1[1::3]) # => 'eoWl'  (1-last, step 3)
print(str1[::-1]) # => '!dlroW ,olleH' (reversed string)
print(str1[1:10:3]) # => 'eoW' (1 to 9, step 3)
print(str1[-2:-11:-2]) # => 'drW,l' (-2 to -10, step -2)
print(str1[5::-1]) # => ',olleH'
print(str1[12:5:-1]) # => '!dlroW '
print(str1[::4])  # => 'Hoo!'
print(str1[1:12:4]) # => 'e,r'
print(str1[-1::-3]) # => '!r lH'
print(str1[-3::-6]) # => 'lo'
