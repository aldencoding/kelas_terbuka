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
