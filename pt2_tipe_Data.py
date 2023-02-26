#Tipe data: Angka satuan yg tidak ada koma
#(Integer)

Data_Integer = 11
print("Data : ", Data_Integer)
print("-Bertipe", type(Data_Integer))

#Tipe data: Angka satuan yg ada koma
#(Float)

Data_Float = 1.5
print("Data : ", Data_Float)
print("-Bertipe", type(Data_Float))

#Tipe data: Kumpulan karakter
#(String)

Data_String = "Farrel"
print("Data : ", Data_String)
print("-Bertipe", type(Data_String))

#Tipe data: Biner True/False
#(Booelan)

Data_bool = True
print("Data : ", Data_bool)
print("-Bertipe", type(Data_bool))

## Tipe Data Khusus

#Data Kompleks
Data_Kompleks = complex(5,6)
print("Data : ", Data_Kompleks)
print("-Bertipe", type(Data_Kompleks))

#Tipe data dari bahasa C

from ctypes import c_double
Data_C_Double = c_double(10.5)
print("Data : ", Data_C_Double )
print("- Bertipe", type(Data_C_Double))