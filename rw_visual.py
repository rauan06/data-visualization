import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    # Make a random walk, and plot the points.
    rw = RandomWalk()
    rw.fill_walk()

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, edgecolors='none', 
                c=point_numbers, cmap=plt.cm.Greys, s=10)
    
    # Emphasize the first and last points.
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[int(len(rw.x_values)/2)], rw.y_values[int(len(rw.y_values)/2)], edgecolors='none',
                s=100, c='yellow')
    plt.scatter(rw.x_values[-1], rw.y_values[-1], edgecolors='none',
                s=100, c='red')
    
    # Remove axes
    plt.axis('off')
    plt.savefig('random.png', bbox_inches='tight')
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break

