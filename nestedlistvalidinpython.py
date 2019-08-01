#Nested lists are also valid in python. This means that a list can contain another list as an element.

x = [1, 2, [3, 4, 5], 6, 7]
# this is nested list
print x[2]
# Output: [3, 4, 5]
print x[2][1]
# Output: 4
#Lastly, variables in Python do not have to stay the same type as which they were ﬁrst deﬁned -- you can simply use = to assign a new value to a variable,
#even if that value is of a diﬀerent type.
