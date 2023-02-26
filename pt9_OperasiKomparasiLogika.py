'''#Operasi logika Komparasi

# Membuat gabungan area rentang dari angka

# +++++++3----------10+++++++++

inputuser = float(input("Masukan Angka yang bernilai\nkurang dari 3\natau\nlebih dari 10 : "))

# ++++++++++3-------------------
# Memeriksa angka kurang dari 3

IsKurangDari = inputuser < 3
print("kurang dari 3 = ", IsKurangDari)

# -----------------10++++++++++
# Memeriksa angka lebih dari 10

IsLebihDari = inputuser > 10
print("Lebih dari 10 = ", IsLebihDari)

# ++++++3-----------------10+++++++

IsCorrect = IsKurangDari or IsLebihDari
print("Angka yang anda masukan : ", IsCorrect)

# ------3+++++++++++10---------
# Kasus Irisan

print("======Irisan======")

InputUser = float(input("Masukan Angka yang bernilai\nlebih dari 3\nKurang dari 10\n: "))

IsLebihDari = InputUser > 3
print("Lebih dari 3 = ", IsLebihDari)

IsKurangDari = InputUser < 10
print("Kurang dari 10 = ", IsKurangDari)

IsCorrect = IsLebihDari and IsKurangDari
print("Angka yang anda masukan: ",IsCorrect)
'''
print("==== PR ====")

#----0++++++5------8++++++11-------

InputUser = float(input("Masukan angka\nlebih dari 0 kurang dari 5\natau\nlebih dari 8 kurang dari 11\n: "))

# Range 0-5
IsLebihDari = InputUser > 0
IsKurangDari = InputUser < 5

IsCorrect1 = IsLebihDari and IsKurangDari
print("Range 0-5: ", IsCorrect1)

# Range 8-11
IsLebihDari = InputUser > 8
IsKurangDari = InputUser < 11

IsCorrect2 = IsLebihDari and IsKurangDari
print("Range 8-11: ", IsCorrect2)

IsCorrectInti = IsCorrect1 or IsCorrect2
print("Hasil: ", IsCorrectInti) 

##+++++0-------5+++++++8--------11++++++++

InputUser = float(input("Masukan angka\nkurang dari 0 lebih dari 5\natau\nkurang dari 8 lebih dari 11\n: "))

# Range 0-5
IsKurangDari = InputUser < 0
IsLebihDari = InputUser > 5 

IsCorrect1 = IsLebihDari or IsKurangDari
print("Range 0-5: ", IsCorrect1)

# Range 8-11
IsKurangDari = InputUser < 8
IsLebihDari = InputUser > 11

IsCorrect2 = IsLebihDari or IsKurangDari
print("Range 8-11: ", IsCorrect2)

IsCorrectInti = IsCorrect1 and IsCorrect2
print("Hasil: ", IsCorrectInti) 