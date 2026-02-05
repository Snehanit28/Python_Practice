# Type conversion 


# Type conversion types implicit and explicit


# Implicit type conversion

#Implicit type conversion examples

x = 5          # int
y = 2.5        # float
sum = x + y      # int is implicitly converted to float
print(sum)          # => 7.5
print(type(sum))    # => <class 'float'>

a = 10       # int
b = 3       # int
result = a / b   # int is implicitly converted to float
print(result)        # => 3.3333333333333335
print(type(result))  # => <class 'float'>



# Explicit type conversion

#Explicit type conversion examples


# Converting int to float
a = 10
b = float(a)
print(b)          # => 10.0
print(type(b))    # => <class 'float'>
# Converting int to complex
c = complex(a)
print(c)          # => (10+0j)
print(type(c))    # => <class 'complex'>
# Converting int to string
d = str(a)
print(d)          # => '10'
print(type(d))    # => <class 'str'>
# Converting int to bool
e = 1
f = bool(e)
print(f)          # => True
print(type(f))    # => <class 'bool'>

# Converting float to int
g = 9.99
h = int(g)
print(h)          # => 9    
print(type(h))    # => <class 'int'>
# Converting float to complex
i = complex(g)
print(i)          # => (9.99+0j)
print(type(i))    # => <class 'complex'>
# Converting float to string
j = str(g)
print(j)          # => '9.99'
print(type(j))    # => <class 'str'>
# Converting float to bool
k = 0.0
l = bool(k)
print(l)          # => False
print(type(l))    # => <class 'bool'>

# Converting complex to int or float will raise an error
# e = 3+4j
# f = int(e)   # TypeError: can't convert complex to int
# g = float(e) # TypeError: can't convert complex to float
# Converting complex to string
m = 3+4j
n = str(m)
print(n)          # => '(3+4j)'
print(type(n))    # => <class 'str'>
# Converting complex to bool
o = 0+0j
p = bool(o)
print(p)          # => False
print(type(p))    # => <class 'bool'>

# Converting string to int
q = "250"
r = int(q)
print(r)          # => 250
print(type(r))    # => <class 'int'>
# Converting string to float
s = "56.78"
t = float(s)
print(t)          # => 56.78
print(type(t))    # => <class 'float'>
# Converting string to complex
u = "2+3j"
v = complex(u)
print(v)          # => (2+3j)
print(type(v))    # => <class 'complex'>
# Converting string to bool
w = ""
x = bool(w)
print(x)          # => False
print(type(x))    # => <class 'bool'>

# Converting boolean to int
bool_val = True 
int_val = int(bool_val)
print(int_val)        # => 1
print(type(int_val))  # => <class 'int'>
# Converting boolean to float
bool_val = False    
float_val = float(bool_val)
print(float_val)        # => 0.0
print(type(float_val))  # => <class 'float'> 
# Converting boolean to complex
bool_val = True
complex_val = complex(bool_val)
print(complex_val)        # => (1+0j)
print(type(complex_val))  # => <class 'complex'>   
# Converting boolean to string
bool_val = True
str_val = str(bool_val)
print(str_val)        # => 'True'
print(type(str_val))  # => <class 'str'>

