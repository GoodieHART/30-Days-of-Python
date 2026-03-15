# euclidean distance is found using pythagoras theorem
# we need 4 inputs for x1, x2, y1, y2
# we then negate x1 from x2 and y1 from y2
# we then sum the inputs
# find the sqrt of the sum
x1 = 2
x2 = 10
y1 = 3
y2 = 8

# we define new variables x3 and y3 to hold the values of our computations
x3 = (x2 - x1) ** 2 # (10-2)^2
y3 = (y2 - y1) ** 2 # (8 - 3)^2

# final answer variable 'z'

z = (x3 + y3) ** 0.5
print(z)