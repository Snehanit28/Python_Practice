# Assignment Operators: Used to assign values to variables.

"""Assignment Operators:
     =   -> Simple assignment
     +=  -> Add and assign
     -=  -> Subtract and assign
     *=  -> Multiply and assign
     /=  -> Divide and assign
     %=  -> Modulus and assign
     **= -> Exponentiation and assign
     //= -> Floor division and assign"""
x = 10  # Simple assignment
print(x)  # => 10       
x += 5  # x = x + 5
print(x)  # => 10 + 5 = 15  
x -= 3  # x = x - 3  
print(x)  # => 15 - 3 = 12
x *= 2  # x = x * 2
print(x)  # => 12 * 2 = 24 
x /= 4  # x = x / 4
print(x)  # => 24 / 4 = 6.0  
x %= 4  # x = x % 4 
print(x)  # => 6.0 % 4 = 2.0 
x **= 3  # x = x ** 3
print(x)  # => 2.0 ** 3 = 8.0 
x //= 3  # x = x // 3
print(x)  # => 8.0 // 3 = 2.0
# Note: After the first division operation, x becomes a float.

