def calculate_shift(W, pos):
    shift = 0
    for character in reversed(W):
        shift += 1
        if pos == character:
            return shift
    return len(W) + 1


def create_help_table(T, W):
    unique_values = set(T)
    help_table = {}
    for character in unique_values:
        help_table[character] = calculate_shift(W, character)
    return help_table


def sunday_search(T, W):
    help_table = create_help_table(T, W)
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
                pos += help_table[T[pos]]
                break
        else:
            result.append(iterationIndex)
            pos = iterationIndex + help_table[T[iterationIndex]]

    return counter
