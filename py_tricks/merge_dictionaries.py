# Merge two dictionaries

x_val = {'a': 1, 'b': 2}
y_val = {'c': 3, 'd': 4}

xy_val = {**x_val, **y_val}

print(xy_val)  # prints the merged dict

# what if the keys are same?
# the right side wins
z_val = {'c': 7, 'e': 5}

yz_val = {**y_val, **z_val}

print(yz_val)  # the value of c in z_val is chosen
