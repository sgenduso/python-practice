park = []
park.append("golden")
park.append("husky")
park.append("shepherd")
park.append("lab")

# same as:
park2 = ["golden", "husky", "shepherd", "lab"]

list_length = len(park)

print "There are %d items in the park." % (list_length)
print park

# slice: We start at the index before the colon and continue
# up to but not including the index after the colon.
suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]

first  = suitcase[0:2]  # The first and second items (index zero and one)
middle =  suitcase[2:4] # Third and fourth items (index two and three)
last   = suitcase[4:6]  # The last two items (index four and five)

animals = "catdogfrog"
cat  = animals[:3]   # The first three characters of animals
dog  = animals[3:6]  # The fourth through sixth characters
frog = animals [6:]  # From the seventh character to the end

# indexing and inserting
animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index('duck')   # Use index() to find "duck"
animals.insert(duck_index, 'cobra')
animals.remove('aardvark')
print animals # Observe what prints after the insert operation

# ways to remove elements from lists
# pop(index) -- removes element at given index and returns it
# remove(item) -- removes item if it finds it
# del(arr[i]) -- removes element but doesn't return it
n = [1, 3, 5]
def resetN:
    n = [1, 3, 5]

n.pop(1) # removes and returns 3
resetN()
n.remove(1) # removes 1 (element at index 0)
resetN()
del(n[1]) # removes 3 but does not return it

# for loops with indeces
def print_list(x):
    for i in range(0, len(x)):
        print x[i]

# The range function has three different versions:
# range(stop)
# range(start, stop)
# range(start, stop, step)
# In all cases, the range() function returns a list of numbers from start up to (but not including) stop. Each item increases by step.
# If omitted, start defaults to zero and step defaults to one.
range(6) # => [0,1,2,3,4,5]
range(1,6) # => [1,2,3,4,5]
range(1,6,3) # => [1,4]
