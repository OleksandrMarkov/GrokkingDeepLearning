import numpy as np

a = np.array([1,2,3])
b = np.array([4,4,5])
c = np.array([[1,1,1], [4,5,6]])

#print(a*b)

#print(a*c)

m = np.zeros((1,4))
n = np.zeros((4,3))

k = m.dot(n)
#print(k.shape)
#print(k)

f = np.zeros((5,4)).T
g = np.zeros((5,6))
h = f.dot(g)
print(h.shape) # 4x6
    