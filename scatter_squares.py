import matplotlib.pyplot as plt

input_values = list(range(1,100))
squares = [i**2 for i in input_values]

plt.scatter(input_values, squares, edgecolors='none', c=squares, cmap=plt.cm.Blues, s=10)
plt.title('Dot of Einstein', fontsize = 10)
plt.xlabel('See here', fontsize = 10)
plt.ylabel('And here', fontsize = 10)


plt.axis([0, 100, 0, 10000])
plt.tick_params('both', which="major", labelsize=10)
plt.savefig('squares_plot.png', bbox_inches='tight')
plt.show()