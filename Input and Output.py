#Input and Output in Python

name = (input("Enter your name: "))     # input from user
age = int(input("Enter your age: "))    # input from user and convert to int

print("Hi" + " " + name)   # output
print("You are ",str(age)," years old.")  # output with type conversion from int to str
print(f"Hello my name is {name} and i am {age} years old.") # output using f-string
print(r"This is a raw string \n no + name + new line")  # raw string output 
print("This is a multi-line  string:\nLine 1\nLine 2\nLine 3")  # multi-line string output
print("Name: {}, Age: {}".format(name, age)) # output using format method

a = 10
b = 20

print(a, b, sep=", ")  # custom separator  #=> 10, 20
print(a, b, end="; ")  # custom end character  #=> 10 20;
print("Hello", end=" ") 
print("World") # => Hello World