#Even though there's no need to specify a data type when declaring a variable in Python,
#while allocating the necessary area in memory for the variable,
#the Python interpreter automatically picks the most suitable built-in type for it:
a = 2
print(type(a))
# Output: <type 'int'>



b = 9223372036854775807
print(type(b))
# Output: <type 'int'>


pi = 3.14
print(type(pi))
# Output: <type 'float'>


c = 'A'
print(type(c))
# Output: <type 'str'>


name = 'John Doe'
print(type(name))
# Output: <type 'str'>



q = True
print(type(q))
# Output: <type 'bool'>


x = None
print(type(x))
# Output: <type 'NoneType'>

