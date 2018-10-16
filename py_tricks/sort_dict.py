# Sort a Python dict by value

x = {'a': 4, 'b': 3, 'c': 2, 'd': 1}

sorted_x = sorted(x.items(), key=lambda x: x[1])
print(sorted_x)

# Or:

import operator
sorted_x = sorted(x.items(), key=operator.itemgetter(1))
print(sorted_x)
