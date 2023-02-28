# Operasi dan manipulasi string

# 1. Menyambung string (concatenate)

nama_pertama = 'Alden'
nama_tengah = 'Farrel'
nama_akhir = 'Edria'

nama_lengkap = nama_pertama +" "+ nama_tengah +" "+ nama_akhir
print(nama_lengkap)  

# 2. Menghitung panjang str

panjang = len(nama_lengkap)
print("panjang dari " + nama_lengkap +"= "+str(panjang))

# Operator untuk string

# mengecek apakah ada komponen char atau string pada string

a = 'a'
status = a in nama_lengkap
print(status)

x = 'x'
status = x in nama_lengkap
print(status)

a = 'a'
status = a not in nama_lengkap
print(status)

# mengulang string

print("wk"*10)
print(10*"wk")

# idexing
print("index ke-0: ", nama_lengkap[0:7:2])

#item paling kecil
print("paling kecil" + min(nama_lengkap))

#item paling besar
print("paling kecil" + max(nama_lengkap))

ascii_code = ord(" ")
print("ASCII_code untuk spasi adalah " + str(ascii_code))
data = 117
print("char untuk ASCII 117 adalah " + chr(data))

# 4. Operator dalam bentuk method
data = "ular melingkar diatas pagar"
jumlah = data.count("r")
print("jumlah huruf r " + str(jumlah))

#========================================

print(10*"=" + "Part 2" + "="*10)

# Operator dalam bentuk methods

## merubah case dari string

# merubah semua ke upper
salam = "bro!"
print("Normal = " + salam)
upper = salam.upper()
print("upper = " + upper)

# merubah semua ke lower case
salam = "bro!"
print("Normal = " + salam)
lower = salam.lower()
print("upper = " + lower)

# pengecekan isX method

# contoh pengecekan lower case
salam = "sist"
apakah_lower = salam.islower()
print(salam + " is lower? = " + str(apakah_lower))
# contoh pengecekan upper case
apakah_upper = salam.isupper()
print(salam + " is upper? = " + str(apakah_upper))

# isalpha() <-- untuk mengecek apakah semua huruf
# isalnum() <-- untuk mengecek huruf dan angka
# isdecimal() <-- untuk mengecek apakah angka saja
# isspace() <-- spasi,tab, newline \n
# istitle() <-- semua kata dimulai dengan huruf besar

judul = "Tanam Tanam Ubi Tak Perlu Dibajak"
cek_judul = judul.istitle()
print(judul + " is title? =" + str(cek_judul))

# ngecek komponen startswith () endswith()
cek_start = "Halo apa kabar".startswith("Halo")
print("start = " + str(cek_start))

cek_end = "Halo apa kabar".endswith("kabar")
print("end = " + str(cek_end))

# penggabungan komponen join() split()
# - data akan berubah menjadi str
# ([]) ini adalah list
pisah = ['aku','liat','die']
gabung = ' '.join(pisah)
print(gabung , type(pisah))

pisah = ' - '.join(pisah)
print(pisah , type(pisah))

pisah = "aku masuk liat masuk die"
print(pisah.split('-'), type(pisah))

## alokasi karakter rjust(), ljust() center()

kanan = 'kanan'.rjust(10)
print('\'', kanan ,'\'')

kiri = 'kiri'.ljust(10)
print('\'', kiri ,'\'')

tengah = 'tengah'.center(10,'-')
print('\'', tengah ,'\'')
