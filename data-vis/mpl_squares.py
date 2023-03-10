import matplotlib.pyplot as plt

import inspect

squares =[1,4,9,16,25]

fig, ax = plt.subplots()
ax.plot(squares)

mytup = plt.subplots()

print(mytup,mytup[0],mytup[1])

#print(inspect.getsource(plt.Figure))
