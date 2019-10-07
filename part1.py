import matplotlib.pyplot as plt 

x = [0.25, 0.5, 0.75, 1]
y = [val **2 for val in x]
print(x)
print(y)
#simple plot with labels
print("simple plot with labels")
plt.plot(x, y, 'r-')
plt.xlabel("X LABEL")
plt.ylabel("Y LABEL")
plt.title("TITLE")
plt.show()
print("\n\n")

#plot with subplot with one row and 2 columns
print("plot with subplot with one row and 2 columns")

plt.subplot(1, 2, 1)
plt.plot(x ,y ,'r-')
plt.subplot(1, 2, 2)
plt.plot(y, x , 'b-')
plt.show()
print("\n\n")

#figure plot where we can create our axes. It is an object oriented approach
print("figure plot where we can create our axes. It is an object oriented approach")
#create an empty canvas
fig = plt.figure()
#create an axes. [(offset from left), (offset from bottom), (size occupied horizontally), (size occupied vertically)]
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes.set_xlabel("X LABEL")
axes.set_ylabel("Y LABEL")
axes.set_title("TITLE")
axes.plot(x, y, 'g-')
plt.show()
print("\n\n")

#figure plot using multiple axes where one plot is within another
print("figure plot using multiple axes where one plot is within another")
fig = plt.figure()
axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes2 = fig.add_axes([0.4, 0.5, 0.3, 0.3])
axes1.set_xlabel(" AXES 1 X LABEL")
axes1.set_ylabel(" AXES 1 Y LABEL")
axes1.set_title("AXES 1 TITLE")
axes1.plot(x, y, 'g-')
axes2.set_xlabel(" AXES 2 X LABEL")
axes2.set_ylabel(" AXES 2 Y LABEL")
axes2.set_title("AXES 2 TITLE")
axes2.plot(x, y, 'g-')
plt.show()
print("\n\n")
