# Soal pertama

saldo_awal = input("Masukan saldo awal: ")
deposit = input("Masukan Deposit: ")

saldo_akhir = int(saldo_awal) + int(deposit)
print("Total saldo anda: " + str(saldo_akhir),"Rupiah","hehe")
# print bisa mengekskusi variabel apapun bila menggunkan ,

# PR (buat perkodisian tentang status usia)

print("Halo selamat datang\nditerminal")
usia = float(input("Silahkan masukan usia anda"))

if usia <= 0:
    print("Anda belum lahir")
elif usia >= 1 and usia <= 5:
    print("Anda adalah Balita")
elif usia > 5 and usia <= 12:
    print("Anda adalah anak-anak")
elif usia > 12 and usia <= 20:
    print("Anda adalah Remaja")
elif usia > 20 and usia <= 35:
    print("Anda adalah orang Dewasa")
elif usia > 35 and usia <= 70:
    print("Anda adalah Orang Tua")
else:
    print("Anda adalah Lansia")

#
