# String methods and functions
s = " Py thon1 "
print(s.upper())     # PY THON1
print(s.lower())     # py thon1
print(s.strip())     # removes spaces # => "Python1"
print(s.join(["Hello", "World"])) # => "Hello Py thon1 World"
print(s.replace("P", "m"))  # => " my thon1 "
print(len(s))       # => 10
print(s.split("y"))     # => [' P', ' thon1 ']
print(s.find("th"))    # => 4
print(s.startswith(" P"))  # => True    
print(s.endswith("on "))   # => True
print(s.isalpha()) #=> False # is the string only alphabets? False here due to spaces and digit
print(s.isdigit()) #=> False # is the string only digits? False here due to alphabets and spaces
print(s.isspace()) #=> False # is the string only spaces? False here due to alphabets and digit
print(s.isdecimal())   # => False # is the string only decimal characters? False here due to alphabets and spaces
print(s.capitalize())   # => " py thon1 " # Capitalizes first character
print(s.title())        # => " Py Thon1 " # Capitalizes first character of each word
print(s.count(" "))    # => 3   # counts number of spaces
print(s.count("t"))    # => 1   # counts number of 't'
print(s.index("h"))    # => 5   # index of first occurrence of 'h'
# add and remove a word from the string 
print(s.rindex("n"))   # => 7   # index of last occurrence of 'n'
print(s.center(30))    # => "           py thon1           "
print(s.center(20, '-'))  # => "----- py thon1 -----"
print(s.zfill(15))       # => "00000 py thon1 "
# Note: zfill fills with leading zeros to make the string of given length
# If the string is longer than the specified length, it returns the original string
print(s.swapcase())     # => " pY THON1 " #  Swaps case of each character
print(s.partition("th")) # => (' Py ', 'th', 'on1 ')  # Splits at first occurrence
print(s.rpartition("th")) # => (' Py ', 'th', 'on1 ') # Splits at last occurrence
print(s.splitlines())   # => [' Py thon1 '] # Splits at line breaks
print(s.encode())      # => b' Py thon1 ' # Encodes to bytes here in default 'utf-8'
print(s.islower())     # => True
print(s.isupper())     # => False
print(s.lstrip())      # => "py thon1 " # removes leading spaces
print(s.rstrip())      # => " py thon1" # removes trailing spaces
print(s.expandtabs())  # => " py thon1 " (no tabs to expand here)
print(s.__add__(" is great"))  # => " py thon1  is great" # concatenation
print(s.__contains__("thon"))  # => True 
print(s.__len__())     # => 10