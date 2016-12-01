import matplotlib.pyplot as plt

squares =  [1, 4, 9, 16, 25]
plt.plot(squares, linewidth=5)

#set chart title and labels on axes
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

#size of tick labels
plt.tick_params(axis='both', labelsize=14)

plt.show()
