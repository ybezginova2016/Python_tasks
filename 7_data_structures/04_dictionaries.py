Colors = {'Sam': 'Blue', 'Amy': 'Red', 'Sarah': 'Yellow'}

for Item in Colors.keys():
    print("{0} likes the color {1}.".format(Item, Colors[Item]))

# update the value
Colors['Sarah'] = 'Purple'
print(Colors)

# add a new line in the dict
Colors.update({'Harry': 'Orange'})
print(Colors)