counter = 0


def matches_at(T, W, p):
    global counter
    for i in range(len(W)):
        counter += 1
        if T[p + i] != W[i]:
            return False
    return True


def naive_search(T, W):
    result = []
    reset_counter()
    for p in range(len(T) - len(W) + 1):
        if matches_at(T, W, p):
            result.append(p)
    return result


def get_counter():
    return counter


def reset_counter():
    global counter
    counter = 0
