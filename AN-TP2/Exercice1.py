import matplotlib.pyplot as plt

abs = [

]

ord = [

]

for j in range(0, 100):
    ord.append(j)
    abs.append(1.2**j)


plt.plot(abs, ord, '+g')
plt.show()