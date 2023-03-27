import pandas as pd
import statistics as stat
import numpy as np
from tabulate import tabulate


class soalTK2:
    data = pd.read_csv('./data_tk1.csv')

    # Manual Function of Mean
    def meanFunc(self, deret):
        return sum(deret) / len(deret)

    # Manual Function of Modus
    def modusFunc(self, deret):
        # dictionary untuk mapping nilai terbanyak
        peta_kemunculan = {}

        # perulangan satu-persatu tiap bilangan
        for bilangan in deret:
            # periksa apakah sudah pernah muncul atau belum
            if bilangan in peta_kemunculan:
                peta_kemunculan[bilangan] += 1
            else:
                peta_kemunculan[bilangan] = 1

        # cari kemunculan terbanyak
        bilangan_terbesar = deret[0]  # ambil angka pertama sebagai yg terbanyak
        for bilangan in peta_kemunculan.keys():
            jumlah = peta_kemunculan[bilangan]

            if jumlah > peta_kemunculan[bilangan_terbesar]:
                bilangan_terbesar = bilangan

        return bilangan_terbesar

    def medianFunc(self, deret):
        if int(len(sorted(deret))) % 2 == 0:
            median1 = sorted(deret)[int(len(sorted(deret)) / 2)]
            median2 = sorted(deret)[int(len(sorted(deret)) / 2) - 1]
            return (median1 + median2) / 2
        return sorted(deret)[int(len(sorted(deret)) / 2)]

    def soalABC(self):
        # Menggunakan numpy dan statistics

        # a. Mencari nilai mean dari data ukuran ruang kantor, tarif internet, dan harga sewa per bulan
        print('Soal A:\n')
        print('Menggunakan fungsi dari numpy dan statistics:')

        print(f'Mean Data Ukuran \t\t= {np.mean(self.data.Ukuran)}')
        print(f'Mean Data Ukuran \t\t= {stat.mean(self.data.Ukuran)}\n')

        print(f'Mean Data Tarif_Internet \t= {np.mean(self.data.Tarif_Internet)}')
        print(f'Mean Data Tarif_Internet \t= {stat.mean(self.data.Tarif_Internet)}\n')

        print(f'Mean Data Harga_Sewa \t\t= {np.mean(self.data.Harga_Sewa)}')
        print(f'Mean Data Harga_Sewa \t\t= {stat.mean(self.data.Harga_Sewa)}\n')

        # b. Mencari nilai median dari data ukuran ruang kantor, tarif internet, dan harga sewa per bulan
        print('Soal B:\n')
        print(f'Mean Data Ukuran \t\t= {np.median(self.data.Ukuran)}')
        print(f'Median Data Ukuran \t\t= {stat.median(self.data.Ukuran)}\n')

        print(f'Mean Data Tarif_Internet \t= {np.median(self.data.Tarif_Internet)}')
        print(f'Median Data Tarif Internet \t= {stat.median(self.data.Tarif_Internet)}\n')

        print(f'Mean Data Harga_Sewa \t\t= {np.median(self.data.Harga_Sewa)}')
        print(f'Median Data Harga Sewa \t\t= {stat.median(self.data.Harga_Sewa)}\n')

        # c. Mencari nilai modus dari data ukuran ruang kantor, tarif internet, dan harga sewa per bulan
        print('Soal C:\n')
        print(f'Modus Data Ukuran  \t\t= {stat.mode(self.data.Ukuran)}')
        print(f'Modus Data Tarif Internet \t= {stat.mode(self.data.Tarif_Internet)}')
        print(f'Modus Data Harga Sewa \t\t= {stat.mode(self.data.Harga_Sewa)}\n\n')

    def soalABCManual(self):
        # Menggunakan cara manual seperti di LN
        print('Menggunakan cara manual:')

        # a. Mencari nilai mean dari data ukuran ruang kantor, tarif internet, dan harga sewa per bulan
        print('Soal A:\n')
        print(f'Mean Data Ukuran  \t\t= {self.meanFunc(self.data.Ukuran)}')
        print(f'Mean Data Tarif Internet  \t= {self.meanFunc(self.data.Tarif_Internet)}')
        print(f'Mean Data Harga Sewa  \t\t= {self.meanFunc(self.data.Harga_Sewa)}\n')

        # b. Mencari nilai median dari data ukuran ruang kantor, tarif internet, dan harga sewa per bulan
        print('Soal B:\n')
        print(f'Median Data Ukuran  \t\t= {self.medianFunc(self.data.Ukuran)}')
        print(f'Median Data Tarif Internet  \t= {self.medianFunc(self.data.Tarif_Internet)}')
        print(f'Median Data Harga Sewa  \t\t= {self.medianFunc(self.data.Harga_Sewa)}\n')

        # c. Mencari nilai modus dari data ukuran ruang kantor, tarif internet, dan harga sewa per bulan
        print('Soal C:\n')
        print(f'Modus Data Ukuran  \t\t= {self.modusFunc(self.data.Ukuran)}')
        print(f'Modus Data Tarif Internet  \t= {self.modusFunc(self.data.Tarif_Internet)}')
        print(f'Modus Data Harga Sewa  \t\t= {self.modusFunc(self.data.Harga_Sewa)}\n\n')


    def comparizedFunc(self):
        headers = ["Description", "Manual", "Stat", "Status"]
        row = np.array([
            ["Mean Ukuran", self.meanFunc(self.data.Ukuran), stat.mean(self.data.Ukuran), self.meanFunc(self.data.Ukuran) == stat.mean(self.data.Ukuran)],
            ["Mean Tarif Internet", self.meanFunc(self.data.Tarif_Internet), stat.mean(self.data.Tarif_Internet), self.meanFunc(self.data.Tarif_Internet) == stat.mean(self.data.Tarif_Internet)],
            ["Mean Harga Sewa", self.meanFunc(self.data.Harga_Sewa), stat.mean(self.data.Harga_Sewa), self.meanFunc(self.data.Harga_Sewa) == stat.mean(self.data.Harga_Sewa)],

            ["Median Ukuran", self.medianFunc(self.data.Ukuran), stat.median(self.data.Ukuran), self.medianFunc(self.data.Ukuran) == stat.median(self.data.Ukuran)],
            ["Median Tarif Internet", self.medianFunc(self.data.Tarif_Internet), stat.median(self.data.Tarif_Internet), self.medianFunc(self.data.Tarif_Internet) == stat.median(self.data.Tarif_Internet)],
            ["Median Harga Sewa", self.medianFunc(self.data.Harga_Sewa), stat.median(self.data.Harga_Sewa), self.medianFunc(self.data.Harga_Sewa) == stat.median(self.data.Harga_Sewa)],

            ["Modus Ukuran", self.modusFunc(self.data.Ukuran), stat.mode(self.data.Ukuran), self.modusFunc(self.data.Ukuran) == stat.mode(self.data.Ukuran)],
            ["Modus Tarif Internet", self.modusFunc(self.data.Tarif_Internet), stat.mode(self.data.Tarif_Internet), self.modusFunc(self.data.Tarif_Internet) == stat.mode(self.data.Tarif_Internet)],
            ["Modus Harga Sewa", self.modusFunc(self.data.Harga_Sewa), stat.mode(self.data.Harga_Sewa), self.modusFunc(self.data.Harga_Sewa) == stat.mode(self.data.Harga_Sewa)],
        ])
        table = tabulate(row, headers, tablefmt="fancy_grid")
        print(table)

    def fullAnswer(self):
        self.soalABC()
        self.comparizedFunc()
