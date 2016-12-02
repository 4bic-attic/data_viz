import matplotlib.pyplot as plt

from random_walk import RandomWalk

#keep making random walks as long as the program is active
while True:
    #make arandom walk and plt the points
    rw = RandomWalk(50000)
    rw.fill_walk()

    #set the size of the plotting window
    plt.figure(dpi=128, figsize=(10, 6))
    p
    #Plot points and show the plot
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
        edgecolor='none', s=1)

    #Emphasize the first and last points
    plt.scatter(0, 0, c='green', edgecolor='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none',
        s=100)

    #remove the axes
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = raw_input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
