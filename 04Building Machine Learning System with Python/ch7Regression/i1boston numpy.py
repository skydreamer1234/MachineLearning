import numpy as np
from sklearn.datasets import load_boston
import pylab as plt

boston = load_boston()
x = np.array([np.concatenate((v, [1])) for v in boston.data])
y = boston.target

print(len(x), len(y),x[0:5], y[0:5])

# np.linal.lstsq implements least-squares linear regression
s, total_error, _, _ = np.linalg.lstsq(x, y)

rmse = np.sqrt(total_error[0] / len(x))
print('Residual: {}'.format(rmse))

# Plot the prediction versus real:
plt.plot(np.dot(x, s), boston.target, 'ro')

# Plot a diagonal (for reference):
plt.plot([0, 50], [0, 50], 'g-')
plt.xlabel('predicted')
plt.ylabel('real')
plt.show()
