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
