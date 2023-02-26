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
print("index ke-0: ", nama_lengkap[0])
