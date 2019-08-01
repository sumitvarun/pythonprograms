#Section 1.2: Creating variables and assigning values
#To create a variable in Python, all you need to do is specify the variable name, and then assign a value to it.
# <variable name> = <value>
#Python uses = to assign values to variables.
#There's no need to declare a variable in advance (or to assign a data type to it),
#assigning a value to a variable itself declares and initializes the variable with that value.
#There's no way to declare a variable without assigning it an initial value.

# Integer
a = 2
print(a) # Output: 2


# Integer
b = 9223372036854775807
print(b) # Output: 9223372036854775807


# Floating point
pi = 3.14
print(pi) # Output: 3.14


# String
c = 'A'
print(c) # Output: A


# String
name = 'John Doe'
print(name) # Output: John Doe


# Boolean
q = True
print(q)
# Output: True


# Empty value or null data type
x = None
print(x) # Output: None


#Variable assignment works from left to right. So the following will give you an syntax error.
#0 = x => Output: SyntaxError: can't assign to literal

#You can not use python's keywords as a valid variable name. You can see the list of keyword by:
import keyword
print(keyword.kwlist)



#Rules for variable naming:
#Variables names must start with a letter or an underscore.1.
x  = True   # valid
_y = True   # valid
#9x = False  # starts with numeral
#=> SyntaxError: invalid syntax  
#$y = False  # starts with symbol
#=> SyntaxError: invalid syntax
#The remainder of your variable name may consist of letters, numbers and underscores.2.
#has_0_in_it = "Still Valid"






























