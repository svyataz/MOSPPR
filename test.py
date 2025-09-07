import numpy as np
def derivative_1(temp_x):
    temp_x[0] += 1
    return (1 +temp_x[1])

x = np.array([1, 1])
print(derivative_1(x))
print(x)
x += [-1, 1]
print (x)
