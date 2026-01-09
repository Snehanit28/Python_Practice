# Operators are special symbols or keywords that perform operations on one or more operands.
# operands are the values or variables on which the operators act. 
# a+b -> here a and b are operands and + is the operator.

# Operators can be classified into several categories based on their functionality:

"""Arithmetic Operators: Used for mathematical operations like addition, subtraction, multiplication, division, etc.
     + -> Addition
     - -> Subtraction
     * -> Multiplication
     / -> Division
     % -> Modulus
     ** -> Exponentiation
     // -> Floor Division"""

'''priority order of arithmetic operations:

   PEMDAS Rule:
    1. Parentheses ( () )  
    2. Exponents ( ** )
    3. Multiplication ( * ) (from left to right) 
    4. Division ( / ) (from left to right)
    5. Addition ( + ) (from left to right)
    6. Subtraction ( - ) (from left to right)'''

a = 10
b = 3
print(a + b)  # => 13 
print(a - b)  # => 7
print(a * b)  # => 30
print(a / b)  # => 3.3333333333333335
print(a % b)  # => 1 
# modulus gives the remainder after division.
print(a ** b)  # => 1000
# exponentiation raises the first operand to the power of the second operand.
print(a // b)  # => 3
# floor division removes the decimal part from the result.

result = 3 + 5 * 2 - (4 / 2) ** 2  # following PEMDAS rule
#  => 3 + 5 * 2 - 2 ** 2
#  => 3 + 5 *  2 - 4
#  => 3 + 10 - 4
#  => 13 - 4
#  => 9
print(result)  # => 9.0

