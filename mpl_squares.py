import matplotlib.pyplot as plt

squares = [i*i for i in range(1, 6)]
input_values = [i for i in range(1, 6)]
plt.plot(input_values, squares, linewidth=5)

# Set chart title and label axes.
plt.title("Function of squres", fontsize=24)
plt.xlabel("Value", fontsize=12)
plt.ylabel("Square of Value", fontsize=10)

# Set tick size of labels.
plt.tick_params(axis='both', labelsize=14)
plt.show()