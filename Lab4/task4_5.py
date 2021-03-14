import numpy as np

m = int(input('Enter M'))
n = int(input('Enter N'))

new_matrix = np.empty([m, n])

new_matrix.fill(0)
np.fill_diagonal(new_matrix, 5)
new_matrix = np.fliplr(new_matrix)

print(new_matrix)
