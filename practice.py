# ratedAvengerList2D=[
#     ["Spiderman",8],
#     ["Groot",7],
#     ["Blach Widow",8]
# ]
# for i in range(0, len(ratedAvengerList2D)):
#     # print(ratedAvengerList2D[i])
#     for j in range(0, len(ratedAvengerList2D[i])):
#         print(ratedAvengerList2D[i][j])

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 3*np.pi, 0.1)
y = np.sin(x)

print(x)
print(y)

plt.plot(x, y)
plt.show()

# import matplotlib.pyplot as plt

# x = [0, 2, 3, 5]
# y = [6, 7, 9, 10]

# plt.plot(x, y)
# plt.axis([0, 6, 0, 20])
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt

# x = np.arange(0, 3*np.pi, 0.1)
# y_sin = np.sin(x)
# y_cos = np.cos(x)

# plt.plot(x, y_sin)
# plt.plot(x, y_cos)
# plt.xlabel('x axis label')
# plt.ylabel('y axis label')
# plt.title('Sine and Cosine')
# plt.legend(['Sine', 'Cosine'])
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt

# x = np.arange(0, 3*np.pi, 0.1)
# y_sin = np.sin(x)
# y_cos = np.cos(x)

# # setting up a subplot grid having
# # height 2 and width 1 and set the first
# # subplot as active
# plt.subplot(2, 1, 1)

# # Creating the first subplot
# plt.plot(x, y_sin)
# plt.title("Sine wave")

# # Creating the second subplot
# plt.subplot(2, 1, 2)
# plt.plot(x, y_cos)
# plt.title("Cosine wave")

# plt.show()