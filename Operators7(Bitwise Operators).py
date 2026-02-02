# Bitwise Operators: Used to perform bit-level operations on integers.

"""Bitwise Operators:
     &  -> Bitwise AND
     |  -> Bitwise OR
     ^  -> Bitwise XOR
     ~  -> Bitwise NOT
     << -> Left Shift
     >> -> Right Shift"""
a = 10  # In binary: 1010
b = 4   # In binary: 0100   
print(a & b)  # Bitwise AND => 0 (0000) (In binary:
                # 1010
                # 0100
                # -----
                # 0000)
print(a | b)  # Bitwise OR  => 14  (1110) (In binary:
                # 1010
                # 0100
                # -----
                # 1110) 
print(a ^ b)  # Bitwise XOR => 14 (In binary:
                # 1010  
                # 0100
                # ----- 
                # 1110)
print(~a)     # Bitwise NOT => -11 (In binary: ...11110101)
               # Note: The result is - (a + 1) due to two's complement representation.
print(a << 2) # Left Shift  => 40 (In binary: 101000)
               # Shifts bits of a to the left by 2 positions.   
print(a >> 2) # Right Shift => 2 (In binary: 0010)
               # Shifts bits of a to the right by 2 positions.
# Note: Bitwise operations are performed on the binary representations of integers.

