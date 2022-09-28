import numpy as np


x = np.array(12) # scalar
x = np.array([12,3,6,14]) # vector

# ndim = 2, form = (3,5)
x = np.array([ [1,24,6,8,9], # matrix
			[0,9,8,7,6],
			[2,1,1,9,9]
	])


# ndim = 3, form = (3,3,5)
x = np.array([ # tensor of rank 3
	[ 	[1,24,6,8,9],
		[0,9,8,7,6],
		[2,1,1,9,9]
	],
	[ 	[1,24,6,8,9],
		[0,9,8,7,6],
		[2,1,1,9,9]
	],
	[ 	[1,24,6,8,9],
		[0,9,8,7,6],
		[2,1,1,9,9]
	]
	])


print(x.ndim)

