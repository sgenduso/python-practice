# Assigning a dictionary with three key-value pairs to residents:
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}
print residents['Puffin']
print residents['Sloth']
print residents['Burmese Python']

menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50
menu['lasagne'] = 24.00
menu['spam'] = 2.00
menu['pepperoni'] = .24
print "There are " + str(len(menu)) + " items on the menu."
print menu

# key - animal_name : value - location
zoo_animals = { 'Unicorn' : 'Cotton Candy House',
'Sloth' : 'Rainforest Exhibit',
'Bengal Tiger' : 'Jungle House',
'Atlantic Puffin' : 'Arctic Exhibit',
'Rockhopper Penguin' : 'Arctic Exhibit'}

# Removing the 'Unicorn' entry. (Unicorns are incredibly expensive.)
del zoo_animals['Unicorn']
del zoo_animals['Bengal Tiger']
zoo_animals['Rockhopper Penguin'] = 'Pizza Exhibit'
print zoo_animals
