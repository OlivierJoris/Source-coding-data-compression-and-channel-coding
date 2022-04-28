import matplotlib.pyplot as plt

values = {1: 1.8453760141417006, 2: 1.709244636409876, 5: 1.5083299285410534, 10: 1.245440218796121}

x = []
y = []

for key in values.keys():
    x.append(key)
    y.append(values[key])

plt.title("Evolution empirical average length")
plt.xlabel("Input text length")
plt.ylabel("Empirical average length")
plt.ylim([1.0, 2.0])
plt.plot(x, y)
plt.show()