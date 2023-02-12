<h1>Cashier Project ThrustMart</h1>

<h2>LATAR BELAKANG PROJECT</h2>

Super Cashier Project merupakan sistem kasir sederhana menggunakan bahasa pemrograman python untuk memudahkan pembeli melakukan transaksi di sebuah toko.

<h2>REQUIREMENT/ OBJECTIVES</h2>
1. Menginput iitem yang ingin dibeli
2. Menampilkan keranjang berisi barang yang akan dibeli
3. Edit barang yang akan dibeli pada   keranjang
    * Update nama item
    * Update qty
    * Update harga
4. Menghapus barang yang akan dibeli pada keranjang
    * Delete salah satu item yang tidak jadi dibeli
5. Reset seluruh item yang tidak jadi dibeli (reset/ kosongkan keranjang)
6. Check order barang yang akan dibeli 
    * Jika benar, menampilkan pesan “Pemesanan sudah benar”
    * Jika ada kekeliruan, menampilkan pesan “Terdapat kesalahan input data”
7. Menampilkan pemesanan yang fix dibeli (check out)
8. Menghitung total belanja yang sudah dibeli
9. Memberikan diskon
    * Jika pembelian > Rp 200.000 mendapatkan diskon 5%
    * Jika pembelian > Rp 300.000 mendapatkan diskon 8%
    * Jika pembelian > Rp 500.000 mendapatkan diskon 10%

<h2>FLOWCHART SEDERHANA PROGRAM</h2>

Berikut flowchart sederhana program yang dibuat
![Gambar Flowchart](flowchart.jpg "Flowchart cashier")



<h2>SNIPPED CODE</h2>


<h3>INISIASI CLASS</h3>
Method dan atribut pada program cashier ini disimpan pada sebuah class bernama Transaction.

berikut ini tampilan saat inisiasi kelas

![inisiasi kelas](./img/class.JPG "Code Class")

<h3>FITUR MAIN MENU</h3>

code menampilkan menu untuk input transaksi program
![Gambar Menu](./img/menu.JPG "Code Menu")

output ketika code dijalankan

![Gambar Output Menu](./img/menu_hasils.JPG "Output Menu")


<h3>FITUR TAMBAH BARANG</h3>

code untuk melakukan input tambah barang 
![Gambar Tambah Barang](./img/input.JPG "Code Tambah barang")

output ketika code dijalankan

![Gambar Output input barang](./img/input_hasil_a.JPG "Output tambah barang")

output ketika menambah barang berupa Nama Barang: Ikan Qty: 3 Harga: Rp 10.000

![Gambar Output hasil input barang](./img/input_hasil_a.JPG "Output tambah barang")

Hasil setelah berhasil ditambahkan ke keranjang 

![Gambar Output hasil input barang b](./img/input_hasil_b.JPG "Output tambah barang")

Update hasil setelah berhasil menambahkan lagi Nama Barang: ayam bakar Qty: 3 Harga: Rp 30.000 ditambahkan ke keranjang 
![Gambar Output hasil input barang c](./img/input_hasil_c.JPG "Output tambah barang")

<h3>FITUR UPDATE QTY BARANG</h3>

code untuk melakukan input update qty barang 
![Gambar update qty Barang](./img/qty.JPG "Code update qty barang")

output ketika code dijalankan dan ingin mengubah nama barang: **"IKAN"**

![Gambar update qty  barang](./img/qty_hasil_a.JPG "Output update qty barang")

output ketika mengubah qty barang berupa Nama Barang: Ikan **Qty baru : 5**

![Gambar Output hasil update qty barang](./img/qty_hasil_b.JPG "Output update qty barang")

<h3>FITUR UPDATE HARGA BARANG</h3>

code untuk melakukan input update harga barang 
![Gambar update harga Barang](./img/harga.JPG "Code update harga barang")

output ketika code dijalankan dan ingin mengubah harga barang: **"AYAM BAKAR"**

![Gambar update harga  barang](./img/harga_hasil_a.JPG "Output update harga barang")

output ketika mengubah harga barang berupa Nama Barang: Ayam Bakar **Harga baru : Rp50.000**

![Gambar Output hasil update harga barang](./img/harga_hasil_b.JPG "Output update harga barang")

<h3>FITUR DELETE/HAPUS SALAH SATU BARANG</h3>

code untuk melakukan delete/hapus barang 
![Gambardelete/hapus Barang](./img/delete.JPG "Code delete/hapus barang")

output ketika code dijalankan dan ingin delete/hapus barang: **"IKAN"**

![Gambar delete/hapus  barang](./img/delete_hasil_a.JPG "Output delete/hapus barang")

output ketika selesai delete/hapus Nama Barang: **IKAN**

![Gambar Output hasil delete/hapus barang](./img/delete_hasil_b.JPG "Output delete/hapus barang")

<h3>FITUR RESET SELURUH BARANG DI KERANJANG</h3>

code untuk melakukan reset barang di keranjang
![Gambar Reset Barang di Keranjang](./img/reset.JPG "Code Reset Barang di Keranjang")

output ketika code dijalankan  **reset seluruh barang di keranjang**

![Gambar Reset Barang di Keranjang](./img/reset_hasil_a.JPG "Output Reset Barang di Keranjang")

output ketika selesai **reset seluruh barang di keranjang**

![Gambar Output hasil Reset Barang di Keranjang](./img/reset_hasil_b.JPG "Output Reset Barang di Keranjang")


output ketika code dijalankan  **reset seluruh barang di keranjang**

![Gambar cekout Barang di Keranjang](./img/reset_hasil_a.JPG "Output cekout Barang di Keranjang")

output ketika selesai **reset seluruh barang di keranjang**

![Gambar Output hasil cekout Barang di Keranjang](./img/reset_hasil_b.JPG "Output cekout Barang di Keranjang")

<h3>FITUR CEKOUT BARANG DI KERANJANG</h3>

code untuk melakukan pengecekan barang di keranjang
![Gambar cekout Barang di Keranjang](./img/cekout_a.jpg "Code cekout Barang di Keranjang")

code untuk melakukan pengecekan check order/ checkout di keranjang
![Gambar cekout Barang di Keranjang](./img/cekout.JPG "Code cekout Barang di Keranjang")

output ketika code dijalankan  **check order/ checkout**

![Gambar cekout Barang di Keranjang](./img/cekout_hasil.JPG "Output cekout Barang di Keranjang")


<h3>FITUR TOTAL HARGA</h3>

code method untuk melakukan perhitungan total belanja dan final price.

jika mencapai total belanja mencapai suatu nilai, akan mendapatkan diskon sehingga final price = total belanja * (1-discount)

![Gambar Total belanja](./img/total.jpg "Code Total belanja")

code method untuk melakukan pengecekan besaran diskon yang didapatkan oleh pelanggan
![Gambar Diskon belanja](./img/total_a.JPG "Code Diskon belanja")

output ketika method  **Total Harga** dijalankan

![Gambar hasil final price](./img/total_hasil.JPG "Output hasil final price")
