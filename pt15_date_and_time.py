### date and time (latihan)

import datetime as dt

print("Silahkan masukan Tanggal, Bulan, Tahun lahir anda: ")
tanggal = int(input("Tanggal: \t"))
bulan = int(input("Bulan: \t\t"))
tahun = int(input("Tahun: \t\t"))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(tanggal_lahir)

hari_ini = dt.date.today()
print(f"Hari ini adalah :\t{hari_ini:}")

umur_hari = hari_ini - tanggal_lahir
print(umur_hari.days)

umur_tahun = umur_hari.days // 365
print(f"Umur anda adalah :\t{umur_tahun} Tahun")

umur_bulan = (umur_hari.days % 365) // 30
print(f"Umur anda adalah :\t{umur_bulan} Bulan")
