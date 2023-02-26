#Operasi Komperasi

#Setiap hasil dari Komparasi adalah Booelean

# >,<,>=,<=,==,!=,is,is not

a = 4
b = 2

#Lebih Besar dari >
print("====== Lebih Besar dari (>) ======")

hasil = a > 3
print(a,'>',3,'=', hasil)

hasil = b > 3
print(b,'>',3,'=', hasil)

hasil = b > 2
print(b,'>', 2 ,'=', hasil)

#Kurang dari <
print("====== Kurang dari (<) ======")

hasil = a < 3
print(a,'<',3,'=', hasil)

hasil = b < 3
print(b,'<',3,'=', hasil)

hasil = b < 2
print(b,'<', 2 ,'=', hasil)

#Kurang dari <=
print("====== Kurang dari (<=) ======")

hasil = a <= 3
print(a,'<=',3,'=', hasil)

hasil = b <= 3
print(b,'<=',3,'=', hasil)

hasil = b <= 2
print(b,'<=', 2 ,'=', hasil)

#Kurang dari >=
print("====== Kurang dari (>=) ======")

hasil = a >= 3
print(a,'>=',3,'=', hasil)

hasil = b >= 3
print(b,'>=',3,'=', hasil)

hasil = b >= 2
print(b,'>=', 2 ,'=', hasil)

# Sama dengan ==
print("====== Sama dengan (==) ======")

hasil = a == 4
print(a,'==',4,'=', hasil)

hasil = b == 4
print(b,'==',4,'=', hasil)

# Tidak sama dengan !=
print("====== Sama dengan (!=) ======")

hasil = a != 4
print(a,'!=',4,'=', hasil)

hasil = b != 4
print(b,'!=',4,'=', hasil)

# "is" Sebagai komparasi object Identity
print("====== Object Identity (is) ======")

x = 5
y = 5
z = 7
Hasil = y is z
print("Nilai x = ",x,"id = ",hex(id(x)))
print("Nilai y = ",y,"id = ",hex(id(y)))
print("y is x = ",Hasil)

# "is not" Sebagai komparasi object Identity
print("====== Object Identity (is not) ======")

x = 5
y = 5
z = 7
Hasil = y is not z
print("Nilai x = ",x,"id = ",hex(id(x)))
print("Nilai y = ",y,"id = ",hex(id(y)))
print("y is x = ",Hasil)