import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import gmean

nvals = range(10, 501, 10)  # the different dimensions we'll be investigating
m = 20  # number of matrices of each dimension

avg_condition_numbers = np.zeros_like(nvals, dtype='float64')

for i, n in enumerate(nvals):
    condition_numbers = np.zeros(m, dtype='float64')  # reserve space for values
    for j in range(m):
        A = np.random.rand(n, n)
        condition_numbers[j] = np.linalg.cond(A)
    avg_condition_numbers[i] = gmean(condition_numbers)  # taking the geometric mean

plt.plot(nvals, avg_condition_numbers)
plt.title('Condition number')
plt.xlabel('n')
plt.ylabel('Average condition number')
plt.show()

"""We can see that as the dimensions increase linearly,
the condition number increases faster than linear."""
