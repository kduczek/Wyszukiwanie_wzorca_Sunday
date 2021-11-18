counter = 0


def matchesAt(T, W, p):
    global counter
    for i in range(len(W)):
        counter += 1
        if T[p + i] != W[i]:
            return False
    return True


def naiveSearch(T, W):
    result = []
    resetCounter()
    for p in range(len(T) - len(W) + 1):
        if matchesAt(T, W, p):
            result.append(p)
    return result


def getCounter():
    return counter


def resetCounter():
    global counter
    counter = 0
