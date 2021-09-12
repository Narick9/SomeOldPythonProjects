import matplotlib.pyplot as plt

squares = [0, 1, 4, 9, 16, 25]

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
plt.plot(x, y, linewidth=5)

plt.title("Square numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of value", fontsize=14)

plt.tick_params(axis="both", labelsize=14)

plt.show()
