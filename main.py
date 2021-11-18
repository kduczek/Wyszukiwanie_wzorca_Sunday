import naive
import sunday
import matplotlib
import utils

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

alphabet = "abcdefghijklmnopqrstuvwxyz"
T = ""
W = utils.rand_text(alphabet, 5)

Xs = []
Ys = []
Xn = []
Yn = []

for _ in range(10000):
    T += utils.rand_text(alphabet, 1)
    counterS = sunday.sundaySearch(T, W)
    Xs.append(len(T))
    Ys.append(counterS)

    naive.naiveSearch(T, W)
    counterN = naive.getCounter()
    Xn.append(len(T))
    Yn.append(counterN)

plt.plot(Xs, Ys)
plt.plot(Xn, Yn)
plt.legend(['Sunday', 'Naiwny'], loc='upper left')
plt.suptitle('Zmienna dlugosc tekstu przeszukiwanego')
plt.xlabel('Dlugosc przeszukiwanego tekstu')
plt.ylabel('Ilosc porownan')
plt.show()