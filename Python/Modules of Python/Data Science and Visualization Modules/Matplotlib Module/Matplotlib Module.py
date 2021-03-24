# Topic: Data Visualization
"""
Data Visualization is the graphical representation of data.
By using charts, graphs, and maps,
data visualization provide an easy way to see
and understand trends and patterns in data.

Matplotlib is used to visual data in 2D format.

Types of plots:
    1.Bar graph
    2.Histograms
    3.Scatter plot
    4.Pie plot
    5.Hexagonal Bin plot
    6.Area plot
"""

from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np

# Topic: Line Graph
style.use("ggplot")

x = [5, 6, 7]
y = [1, 2, 3]

x2 = [1, 4, 3]
y2 = [3, 6, 8]

# Plotting on canvas
# 1. x axis
# 2. y axis
plt.plot(x, y, "g", label="LineOne", linewidth=4, color="red")
plt.plot(x2, y2, "g", label="LineTwo", linewidth=4)

# Details to graph
plt.title("Info")

plt.ylabel("Y Axis")
plt.xlabel("X Axis")

# Adding a legend
plt.legend()

# Adding grid to graph
plt.grid(True, color="black")

# Showing the plot
plt.show()

# Topic: Bar Graph
plt.bar(x, y, label="BarOne")
plt.bar(x2, y2, label="BarTwo")

plt.title("Info")

plt.ylabel("Y Axis")
plt.xlabel("X Axis")

plt.legend()

plt.show()

# Topic: Histogram
plt.hist(87, 98, histtype="bar", rwidth=1)

plt.title("Info")

plt.ylabel("Y Axis")
plt.xlabel("X Axis")

plt.show()

# Topic: Scatter Plot
plt.scatter(x, y, label="Scatter", color="red")

plt.title("Info")

plt.ylabel("Y Axis")
plt.xlabel("X Axis")

plt.show()

# Topic: Stack Plot
plt.plot([], [], label="StackOne", color="red")
plt.plot([], [], label="StackTwo", color="black")
plt.stackplot(x, y, x2, y2, colors=["red", "black"])

plt.title("Info")

plt.ylabel("Y Axis")
plt.xlabel("X Axis")

plt.legend()

plt.show()

# Topic: Pie Plot
slices = [2, 4, 6, 8]

activities = ["playing",
              "sleeping",
              "walking",
              "standing"]

colors = ["red",
          "blue",
          "grey",
          "brown"]

plt.pie(slices,
        labels=activities,
        colors=colors,
        startangle=50,
        shadow=True,
        explode=(0, 0.1, 0, 0),
        autopct="%1.1f%%")

plt.title("Info")

plt.show()


# Topic: Multiple Plots
def f(t):
    return np.exp(-t) * np.cos(2 * np.pi * t)


t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.subplot(211)
plt.plot(t1, f(t1), "bo", t2, f(t2))

plt.subplot(212)
plt.plot(t2, np.cos(2 * np.pi * t2))
plt.show()

# Documentation: https://matplotlib.org/3.1.1/
