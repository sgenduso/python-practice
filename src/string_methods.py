# length
parrot = "Norwegian Blue"
print len(parrot)

# lowercase
print parrot.lower()

# uppercase
print parrot.upper()

# check if string is all alphabetic and there is at least one character
print parrot.isalpha()

# convert to string
pi = 3.14
print str(pi)

# concatenation
print "Spam " + "and " + "eggs"

# explicit string conversion
# BAD:
print "The value of pi is around " + 3.14
# GOOD:
print "The value of pi is around " + str(3.14)

# string formatting with %
string_1 = "Camelot"
string_2 = "place"
print "Let's not go to %s. 'Tis a silly %s." % (string_1, string_2)

name = raw_input("What is your name?")
quest = raw_input("What is your quest?")
color = raw_input("What is your favorite color?")
print "Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color)

# concatenate in loop 
n = ["Michael", "Lieberman"]
def join_strings(words):
    result = ''
    for word in words:
        result += word
    return result

print join_strings(n)
