import numpy as np

X1 = np.array([ 1,  1, 1])
X2 = np.array([ 1, -1, 1])
X3 = np.array([ 1, -1, 1])
X4 = np.array([ 1,  1, 1])

X = np.array([X1, X2, X3, X4])
t = np.array([-1, -1, -1, -1])
y = np.array([0, 0, 0, 0])

weight = np.array([0, 0, 0])
print("initial weights:")
print(weight)

while (not np.array_equal(y, t)):
    y = np.array([])
    for i in X:
        S = np.dot(i.T, weight)
        if(S > 0):
            y = np.append(y, 1)
        else:
            y = np.append(y, -1)
        weight = weight + (i * y[-1])

print("final weights are:")
print(weight)
