def moveSearchingWindow(T, W, pos):
    shift = 0
    for i in reversed(W):
        shift += 1
        if T[pos] == i:
            return shift
    return 0


def sundaySearch(T, W):
    counter = 0
    result = []
    pos = 0
    while (pos + len(W)) < len(T):
        iterationIndex = pos
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

    return counter

