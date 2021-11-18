import matplotlib

import utils

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


def moveSearchingWindow(T, W, pos):
    shift = 0
    for i in reversed(W):
        shift += 1
        if T[pos] == i:
            return shift
    return 0


def sundaySearch(T, W):
    global counter
    result = []
    pos = 0
    while (pos + len(W)) < len(T):
        iterationIndex = pos
        print("Index:" + str(iterationIndex))
        for char in W:
            counter += 1
            if T[pos] == char:
                pos += 1
            else:
                if T[iterationIndex + len(W)] in W:
                    pos += moveSearchingWindow(T, W, iterationIndex + len(W))
                else:
                    pos = iterationIndex + len(W) + 1
                break
        else:
            result.append(iterationIndex)
            print("Result")
            print(result)

    return result


alphabet = "abcdef"
# alphabet = "abcdefghijklmnopqrstuvwxyz"
T = ""
W = utils.rand_text(alphabet, 3)

X = []
Y = []

for _ in range(100):
    T += utils.rand_text(alphabet, 1)
    print(T)
    # print(W)
    counter = 0
    sundaySearch(T, W)
    # print("Counter: " + str(counter))
    X.append(len(T))
    Y.append(counter)

print("Pattern:")
print(W)
plt.plot(X, Y)
plt.show()
