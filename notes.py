# Variable naming conventions
# snake_case
# no 'var', $, etc

# Whitespace
# Bad:
def spam():
eggs = 12
return eggs
print spam()

# Good:
def spam():
    eggs = 12
    return eggs

print spam()

"""Multi
   Line
   Comments"""

# Exponents
eight = 2 ** 3

# Modulo
one = 5 % 2

# Methods that use dot notation only work with strings.
"PARROT".lower()
"parrot".upper()

# On the other hand, len() and str() can work on other data types.
len("parrot")
str(1991)

# Boolean operators 

"""
Boolean Operators
------------------------
True and True is True
True and False is False
False and True is False
False and False is False

True or True is True
True or False is True
False or True is True
False or False is False

Not True is False
Not False is True

not is evaluated first;
and is evaluated next;
or is evaluated last.

"""

# Conditionals
# elif == 'else if'

