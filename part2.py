import matplotlib.pyplot as plt 

x = [0.25, 0.5, 0.75, 1]
y = [val **2 for val in x]
z = [val **3 for val in x]
k = [val **4 for val in x]
#using subplots with axes
print("using subplots with axes")
#by default returns one row and one columns
print("by default returns one row and one columns")
fig, axes = plt.subplots()
axes.plot(x, y)
axes.set_xlabel("X label")
axes.set_ylabel("Y label")
axes.set_title("TTILE")
plt.show()
print("\n\n")

#we can specify the nrows and ncols 
print("we can specify the nrows and ncols")
fig, axes = plt.subplots(nrows=1, ncols=2)
axes[0].plot(x, y, 'r-', label='SQUARED')
axes[0].plot(x, z, 'b-', label='CUBED')
axes[1].plot(y, x, 'r-', label='INV SQUARED')
axes[1].plot(z, y, 'b-', label='INV CUBED')
#different location codes for legend loc can be used. 0 means 'best' location
axes[0].legend(loc=0)
axes[1].legend(loc=0)
#try to fit all the subplots as much as possible 
plt.tight_layout()
plt.show()
print("\n\n")

#we can specify the nrows and ncols 
print("we can specify the nrows and ncols")
fig, axes = plt.subplots(nrows=2, ncols=2)
axes[0,0].plot(x, y)
axes[0,1].plot(x, z)
axes[1,0].plot(y, z)
axes[1,1].plot(y, k)
#try to fit all the subplots as much as possible 
plt.tight_layout()
plt.show()
print("\n\n")

#using figsize to change the size of canvas
print("using figsize to change the size of canvas")
fig = plt.figure(figsize=(3,2))
axes = fig.add_axes([0.1, 0.1, 1, 1])
axes.plot(x, y)
plt.show()
print("\n\n")

#using figsize to change the size of canvas but on subplots
print("using figsize to change the size of canvas but on subplots")
fig, axes = plt.subplots(figsize=(3,2))
axes.plot(x, y)
plt.show()
print("\n\n")

#saving a figure to local storage. 
# figsize = (layout width, layout height)
#dpi = number of pixels per inch
print("figsize = (layout width, layout height)")
print("dpi = number of pixels per inch")
print("saving a figure to local storage")
fig, axes = plt.subplots(figsize=(3,2), dpi=200)
axes.plot(x, y, 'y-', label='X SQUARED')
axes.legend(loc=1)
axes.set_title(" SAVING IMAGE")
plt.show()
fig.savefig('MYFIGURE', dpi=100)
print("\n\n")