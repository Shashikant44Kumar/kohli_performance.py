# import numpy as np
# import matplotlib.pyplot as plt

# Compute x and y coordinates for points on a sine curve
# x = np.arange(0, 3*np.pi, 0.1)
# y = np.sin(x)

# print(x)
# print(y)

# plt.plot(x, y)
# plt.show()
# print("I am Here")

# import numpy as np
# import matplotlib.pyplot as plt

# # Compute x and y coordinates for points on a sine curve
# x = np.arange(0, 3*np.pi, 0.1)
# y_sin = np.sin(x)
# y_cos = np.cos(x)

# # print(x)
# # print(y)

# plt.subplot(2, 1, 1)
# plt.plot(x, y_sin)

# plt.subplot(2, 1, 2)
# plt.plot(x, y_cos)  

# plt.xlabel('x axis label')
# plt.ylabel('y axis label')
# plt.title('Sine and Cosine')
# # plt.legend(['Sine', 'Cosine'])
# plt.show()
# # print("I am Here")

import numpy as np
import matplotlib.pyplot as plt

# Compute x and y coordinates for points on a sine curve
# x = np.arange(0, 3*np.pi, 0.1)

x = np.linspace(-20, 20, 1000)

def func(x):
    y = []
    for elem in x:
        # result = elem**2
        result = -5*(elem**2) + 4 *elem**2
        # result = 1 - (elem**2)/2
        y.append(result)
    return y

y = func(x)

plt.plot(x, y)
plt.show()