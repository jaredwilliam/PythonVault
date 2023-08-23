from itertools import product 

x = [1, 2, 3]
y = [10, 20, 30]
z = [100, 200, 300]

combinations = list(product(x, y, z))

print(combinations)