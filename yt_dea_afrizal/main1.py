saldo_awal_nasabah = input("masukan jumlah saldo Nasabah: ")
deposit_nasabah = input("Masukan Deposito Nasabah: ")
hutang_nasabah = input("Masukan Hutang Nasabah: ")

jumlah_tabungan = float(saldo_awal_nasabah) + float(deposit_nasabah)
jumlah_total = (jumlah_tabungan) - float(hutang_nasabah)

if  jumlah_total <= 100_000:
    print("Saldo anda tidak cukup")
else:
    print("Transaksi Berhasil")