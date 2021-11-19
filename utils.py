from random import choice
import naive
import sunday
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


def rand_text(A, l):
    result = ""
    for _ in range(l): result += choice(A)
    return result


def draw_plot_various_text_lengths():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    T = ""
    W = rand_text(alphabet, 5)

    Xs = []
    Ys = []
    Xn = []
    Yn = []

    for _ in range(10000):
        T += rand_text(alphabet, 1)
        counterS = sunday.sunday_search(T, W)
        Xs.append(len(T))
        Ys.append(counterS)

        naive.naive_search(T, W)
        counterN = naive.get_counter()
        Xn.append(len(T))
        Yn.append(counterN)

    plt.plot(Xs, Ys)
    plt.plot(Xn, Yn)
    plt.legend(['Sunday', 'Naiwny'], loc='upper left')
    plt.suptitle('Zmienna dlugosc tekstu przeszukiwanego')
    plt.xlabel('Dlugosc przeszukiwanego tekstu')
    plt.ylabel('Ilosc porownan')
    plt.show()


def draw_plot_various_pattern_lengths():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    T = rand_text(alphabet, 10000)
    W = ""

    Xs = []
    Ys = []
    Xn = []
    Yn = []

    for _ in range(40):
        W += rand_text(alphabet, 1)
        counterS = sunday.sunday_search(T, W)
        Xs.append(len(W))
        Ys.append(counterS)

        naive.naive_search(T, W)
        counterN = naive.get_counter()
        Xn.append(len(W))
        Yn.append(counterN)

    plt.plot(Xs, Ys)
    plt.plot(Xn, Yn)
    plt.legend(['Sunday', 'Naiwny'], loc='center right')
    plt.suptitle('Zmienna dlugosc wzorca')
    plt.xlabel('Dlugosc wzorca')
    plt.ylabel('Ilosc porownan')
    plt.show()


def draw_plot_various_alphabet_lengths():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    Xs = []
    Ys = []
    Xn = []
    Yn = []

    for i in range(10, 26):
        T = rand_text(alphabet[0: i], 10000)
        W = rand_text(alphabet[0: i], 10)
        counterS = sunday.sunday_search(T, W)
        Xs.append(i + 1)
        Ys.append(counterS)

        naive.naive_search(T, W)
        counterN = naive.get_counter()
        Xn.append(i + 1)
        Yn.append(counterN)

    plt.plot(Xs, Ys)
    plt.plot(Xn, Yn)
    plt.legend(['Sunday', 'Naiwny'], loc='center right')
    plt.suptitle('Zmienna dlugosc alfabetu')
    plt.xlabel('Dlugosc alfabetu')
    plt.ylabel('Ilosc porownan')
    plt.show()
