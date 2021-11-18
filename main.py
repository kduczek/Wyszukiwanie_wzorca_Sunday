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

for _ in range(10000):
    T += utils.rand_text(alphabet, 1)
    counter = sunday.sundaySearch(T, W)
    Xs.append(len(T))
    Ys.append(counter)

plt.plot(Xs, Ys)

Xn = []
Yn = []
T = ""
W = utils.rand_text(alphabet, 5)
for _ in range(10000):
    T += utils.rand_text(alphabet, 1)
    naive.naiveSearch(T, W)
    counterN = naive.getCounter()
    Xn.append(len(T))
    Yn.append(counterN)

plt.plot(Xn, Yn)
plt.legend(['Sunday', 'Naiwny'], loc='upper left')
plt.suptitle('Zmienna dlugosc tekstu przeszukiwanego')
plt.xlabel('Dlugosc przeszukiwanego tekstu')
plt.ylabel('Ilosc porownan')
plt.show()