# perulangan (loop)

# for kondisi:
#   aksi

# ini dengan list
angka2_list = [0,2,4,8,10]
for i in angka2_list:
    print(f"i sekarang --> {i}")

print("akhir dari progam 1\n")

# ini dengan range
angka2_range = range(5)
for i in angka2_range:
    print(f"i sekarang --> {i}")

print("akhir dari progam 2 \n")

angka2_range = range(1,5)
for i in angka2_range:
    print(f"i sekarang --> {i}")

print("akhir dari progam 3 \n")

# meggunakan string
data_str = "saya tampan abiees"
for huruf in data_str:
        print(data_str)

# while loop
print("==========while loop==========")

# while kondisi:
#   aksi ini
#   aksi itu
input_user = input("masukan nama anda: ")
angka = 0
while angka < 100:
    angka += 1
    print(f"nomor {angka}")
