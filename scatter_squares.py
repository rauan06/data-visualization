import matplotlib.pyplot as plt

input_values = list(range(1,1001))
squares = [i**2 for i in input_values]

plt.scatter(input_values, squares, edgecolors='none', c='red', s=1)
plt.title('Dot of Einstein', fontsize = 10)
plt.xlabel('See here', fontsize = 10)
plt.ylabel('And here', fontsize = 10)


plt.axis([0, 500, 0, 100000])
plt.tick_params('both', which="major", labelsize=10)
plt.show()