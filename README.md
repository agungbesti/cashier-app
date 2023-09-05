# Cashier App Sederhana
## Background Project
Andi merupakan pemilik supermarket besar di salah satu kota di Indonesia. Andi memiliki rencana untuk melakukan perbaikan proses bisnis yaitu membuat sistem kasir _self-service_ di supermarket miliknya. Sehingga customer bisa langsung memasukan item yang dibeli, jumlah item yang dibeli dan harga item yang dibeli serta fitur yang lainnya. Dengan adanya sistem kasir ini, diharapkan customer dapat dengan mudah menambahkan produk dalam daftar belanja, melakukan perubahan dan aktivitas transaksi lainnya melalui sistem kasir yang telah dibuat.

## Objective & Requirements
### Objective
Membuat sistem kasir berbasis _self-service_  pada supermarket Andi untuk mempermudah Customer dalam melakukan proses transaksi belanja secara mandiri melalui aplikasi yang telah disediakan.
### Requirements
Fitur-fitur yang terdapat pada sistem kasir _self-service_ diantaranya:
1. Membuat Pesanan.
2. Menghapus Pesanan.
3. Melakukan update nama pesanan.
4. Melakukan update jumlah pesanan.
5. Melakukan update harga pesanan.
6. Melakukan pengecekan terhadap daftar pesanan
7. Melakukan pembatalan/reset transaksi pesanan 
8. Menghitung pembayaran atas transaksi pesanan.

### Penjelasan Kode Program
* `Transaction` : Class untuk menyimpan seluruh method untuk menjalankan proses transaksi.
* `add_item()` : Method dari class Transaction untuk melakukan penambahan nama item, jumlah dan harga ke dalam daftar belanja.
* `remove_item()` : Method dari class Transaction untuk menghapus nama item dalam daftar belanja.
* `update_item_name()` : Method dari class Transaction untuk melakukan update/perubahan pada nama item yang telah dimasukkan ke dalam daftar belanja.
* `update_item_qty()` : Method dari class Transaction untuk melakukan update/perubahan pada jumlah item yang telah dimasukkan ke dalam daftar belanja.
* `update_item_price()` : Method dari class Transaction untuk melakukan update/perubahan pada harga item yang telah dimasukkan ke dalam daftar belanja.
* `reset_transaction()` : Method dari class Transaction untuk mereset/mengosongkan daftar belanja.
* `list_item()` : Method dari class Transaction untuk menampilkan daftar item list yang ada.
* `total_price_calculate()` : Method dari class Transaksi untuk menghitung total harga barang dari jumlah barang yang dipesan.
* `check_order()` : Method dari class Transaction untuk menampilkan daftar pesanan.
* `total_price()` : Method dari class Transaction untuk menampilkan total pembelian daftar pesanan.
### Penjelasan Alur Program
1. Customer masuk ke sistem dan membuat pesanan
2. Customer memilih menu **"1. Tambah Pesanan"** untuk memasukkan nama-nama item beserta jumlah dan harganya ke dalam daftar pesanan.
3. Apabila Customer salah memasukkan data, Customer dapat:
   - memilih menu **"2. update nama pesanan"** untuk mengganti nama item.
   - memilih menu **"3. update jumlah pesanan"** untuk mengganti jumlah item.
   - memilih menu **"4. update harga pesanan"** untuk mengganti jumlah item.
4. Apabila Customer merasa kurang yakin dengan item yang dibelanjakan, maka Customer dapat memilih **"5. Hapus pesanan"**.
5. Customer dapat melihat daftar belanja dengan memilih menu **"6. Periksa Pesanan "**.
6. Customer ingin mengosongkan daftar belanja dan memasukkan pesanan kembali, maka Customer dapat memilih **"7. Reset pesanan"**.
7. Untuk melihat total pesanan, Customer dapat memilih menu **"8. Total Harga Pesanan"**
8. Jika ingin keluar dari aplikasi, customer dapat memilih menu **"9. Keluar Aplikasi"**.

## Test Case
### Test Case 1
Customer ingin menambahkan 2 item baru menggunakan method `add_item()`. Item yang ditambahkan adalah sebagai berikut:
* Nama item: Ayam goreng, Qty: 2, Harga: 20000
* Nama item: Pasta gigi, Qty: 3, Harga: 15000

![image](https://github.com/agungbesti/cashier-app/assets/35904444/2f623309-fc87-496d-b734-7aa82de82799)

![image](https://github.com/agungbesti/cashier-app/assets/35904444/e9b92eca-167c-41a1-96b0-ea1a8e0b9fd8)

Daftar pesanan setelah ditambahkan:

![image](https://github.com/agungbesti/cashier-app/assets/35904444/13cb7cba-1642-4444-bad9-5016060e9b07)

### Test Case 2
Ternyata Customer salah membeli salah satu item dari belanjaan yang sudah ditambahkan, maka Customer dapat menggunakan method `delete_item()` untuk menghapus item yang dipilih. Item yang ingin dihapus adalah Pasta gigi.

![image](https://github.com/agungbesti/cashier-app/assets/35904444/9f0c4aca-acd1-42d5-9fb1-cbe906f2d329)

Daftar pesanan setelah item dihapus:

![image](https://github.com/agungbesti/cashier-app/assets/35904444/afb92681-2072-4621-8c10-36088f2a5a8b)

### Test Case 3
Ternyata setelah dipikir-pikir, Customer salah memasukkan item yang ingin dibelanjakan. Daripada menghapusnya satu-satu, maka Customer cukup menggunakan method `reset_transaction()` untuk menghapus semua item yang sudah ditambahkan.
Daftar pesanan setelah diperbarui:

![image](https://github.com/agungbesti/cashier-app/assets/35904444/bebba733-5401-482e-bd95-a137b7a7f51d)

### Test Case 4
setelah Customer selesai berbelanja, maka sistem akan menghitung total belanja yang harus dibayarkan menggunakan method `total_payment()`. Sebelum mengeluarkan output total akan menampilkan daftar belanja.
Daftar pesanan ketika melakukan pembayaran:

![image](https://github.com/agungbesti/cashier-app/assets/35904444/3ef4b930-6eb4-41d4-a6f0-4b589d924bf2)

## Conclusion
Project python yang diprogram kali ini merupakan sekumpulan kode yang dibuat untuk mengelola proses transaksi pembelian barang dalam sebuah supermarket. Dalam project ini menggunakan class Transaction dengan beberapa methods di dalamnya :`add_item()`, `update_item_name()`, `update_item_qty()`, `update_item_price()`, `delete_item()`, `reset_transaction()`, `check_order()`, dan `total_payment()`. Method-method tersebut digunakan untuk mengelola data transaksi yang masuk seperti menambah pesanan, mengubah data pesanan, meihat daftar pesanan, mereset daftar pesanan dan menghitung pembayaran total harga semua transaksi.
