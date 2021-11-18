from random import choice


def rand_text(A, l):
    result = ""
    for _ in range(l): result += choice(A)
    return result
