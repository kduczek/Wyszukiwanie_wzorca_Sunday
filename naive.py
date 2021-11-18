import matplotlib

import utils

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


def matchesAt(T, W, p):
    global counter
    for i in range(len(W)):
        counter += 1
        if T[p + i] != W[i]:
            return False
    return True


def naiveSearch(T, W):
    result = []
    for p in range(len(T) - len(W) + 1):
        if matchesAt(T, W, p):
            result.append(p)
    return result

T = ""
W = utils.rand_text("abc", 3)

X = []
Y = []
for _ in range(10000):
    T += utils.rand_text("abc", 1)
    counter = 0
    naiveSearch(T, W)
    X.append(len(T))
    Y.append(counter)

plt.plot(X, Y)
plt.show()

