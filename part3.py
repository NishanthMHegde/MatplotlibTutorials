import matplotlib.pyplot as plt 

x = [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4]
y = [val **2 for val in x]
z = [val **3 for val in x]
k = [val **4 for val in x]


fig, axes = plt.subplots(nrows=1, ncols=3)
axes[0].plot(x, y, color='red', linestyle='-', linewidth=2, alpha= 0.1, marker='o', markersize=2, markerfacecolor='yellow', markeredgewidth=3, markeredgecolor='orange')
axes[1].plot(x, z, color='blue', linestyle=':', linewidth=0.5, alpha = 0.25,marker='2', markersize=5, markerfacecolor='green', markeredgewidth=10, markeredgecolor='black')
axes[2].plot(x, k, color='green', linestyle='--', linewidth=10,alpha = 0.75, marker='+', markersize=10, markerfacecolor='blue', markeredgewidth=20, markeredgecolor='brown')
plt.show()

fig, axes = plt.subplots(nrows=1, ncols=3)
axes[0].plot(x, y, color='red', linestyle='-', linewidth=2, alpha= 0.1, marker='o', markersize=2, markerfacecolor='yellow', markeredgewidth=3, markeredgecolor='orange')
axes[0].set_xlim([0, 3])
axes[1].plot(x, z, color='blue', linestyle=':', linewidth=0.5, alpha = 0.25,marker='2', markersize=5, markerfacecolor='green', markeredgewidth=10, markeredgecolor='black')
axes[1].set_xlim([0, 2])
axes[2].plot(x, k, color='green', linestyle='--', linewidth=10,alpha = 0.75, marker='+', markersize=10, markerfacecolor='blue', markeredgewidth=20, markeredgecolor='brown')
axes[2].set_xlim([0, 3.5])
plt.show()