import matplotlib.pyplot as plt

from random_walk import RandomWalk

#make arandom walk and plt the points
rw = RandomWalk()
rw.fill_walk()

plt.scatter(rw.x_values, rw.y_values, s=15)
plt.show()
