import pandas as pd
import csv
from operator import itemgetter
import itertools
import random
import matplotlib.pyplot as plt


def soalA():
    a_data = pd.read_csv('./data_tk1.csv')
    # print (a_data.Ukuran, a_data.Harga_Sewa)

    plt.plot(a_data.Ukuran, a_data.Harga_Sewa, marker='o', ms=10)

    plt.title("Ukuran dan Harga Sewa")
    plt.xlabel("Ukuran (" + str(r'm $^{2}$') + ")   ")
    plt.ylabel("Harga Sewa (Rupiah)")
    plt.grid(color='green', linestyle='--', linewidth=0.5)

    plt.show()


def soalB():
    number_of_colors = 8
    color = ["#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])
             for i in range(number_of_colors)]
    data = []
    with open("./data_tk1.csv", 'r') as file:
        csvreader = list(csv.reader(file))
        csvreader.pop(0)
        csvreader.sort(key=itemgetter(4))
        key_func = lambda x: x[4]
        for key, group in itertools.groupby(csvreader, key_func):
            # print(key + " :", list(group))
            data.append([key, list(group)])
    for idx, d in enumerate(data):
        d[1].sort(key=itemgetter(3))
        keyFuncD = lambda x: x[3]
        rentFee = []
        roomType = []
        for key, group in itertools.groupby(d[1], keyFuncD):
            rentFee.append(int(key))
            roomType.append(len(list(group)))
        print(rentFee, roomType)
        plt.scatter(roomType, rentFee, color=color[idx])
    plt.xlabel("Jumlah")
    plt.ylabel("Tarif Internet")
    plt.show()


def soalC():
    number_of_colors = 8
    color = ["#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])
             for i in range(number_of_colors)]
    data = []
    with open("./data_tk1.csv", 'r') as file:
        csvreader = list(csv.reader(file))
        csvreader.pop(0)
        csvreader.sort(key=itemgetter(4))
        print(csvreader)
        key_func = lambda x: x[4]
        for key, group in itertools.groupby(csvreader, key_func):
            # print(key + " :", list(group))
            data.append([key, list(group)])
    for idx, d in enumerate(data):
        d[1].sort(key=itemgetter(5))
        keyFuncD = lambda x: x[5]
        rentFee = []
        roomType = []
        for key, group in itertools.groupby(d[1], keyFuncD):
            rentFee.append(int(key))
            roomType.append(d[0])
        print(rentFee, roomType)
        plt.scatter(roomType, rentFee, color=color[idx])
    plt.xlabel("Tipe Kamar")
    plt.ylabel("Biaya sewa")
    plt.show()


def startTKA():
    soalA()
    soalB()
    soalC()