import numpy as np

m = int(input('Enter M'))
n = int(input('Enter N'))

new_matrix = np.empty([m, n])

new_matrix.fill(0.5)
np.fill_diagonal(new_matrix, -1)

print(new_matrix)
