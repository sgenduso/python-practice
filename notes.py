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
