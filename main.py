from tabulate import tabulate
from cashier import Transaction


#Jalankan program cashier#
print(tabulate([ ],headers=['Selamat Datang di Self Service Thrust Mart']))

#buat input kode transaksi by input name user 
data_transaksi=input("Silakan Masukkan nama Anda: ").title()
print('-'*44)
print(f'Selamat berbelanja, Kak {data_transaksi}!' )
print('-'*44)

#jalankan menu transaksi dari modul Transaction
data_transaksi=Transaction()
data_transaksi.pilihan_menu()