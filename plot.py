import matplotlib.pyplot as plt
y_axis = [4, 6, 7, 5, 9, 10]
# create y_axis list for y axis
x_axis = list(range(len(y_axis)))
# create x_axis list for x axis

plt.plot(x_axis, y_axis)
# plot the lists on the graph

plt.title("My first Matplotlib Graph")
# set title of the graph

plt.xlabel('X axis label', fontsize=18)
# add label at x axis with fontsize 18
plt.ylabel("Y axis label", fontsize=18)
# add label at y axis with fontsize 18

# finally after all the changes show the graph
plt.show()
