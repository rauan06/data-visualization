from collections import Counter
from die import Die

import pygal

# Create D6, D10
die_1 = Die()
die_2 = Die(10)

# Make some rolls, and store the results
results = []
for i in range(50000):
    results.append(die_1.roll() + die_2.roll())

# Analyze the results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the data
histogram = pygal.Bar()

histogram.title = "Results of rolling on D6 and D10 1000 times"
histogram.x_labels = [i for i in range(2, max_result + 1)]
histogram._x_title = "Result"
histogram._y_title = "Frequency of Result"

histogram.add('D6 + D10', frequencies)
histogram.render_to_file('die-bisual.svg')