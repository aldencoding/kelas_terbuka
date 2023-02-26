# Merubah dari satu tipe ke tipe lain
#tipe data = int, float, string, bool

## INTEGER

Data_int = 9    
print("Data: ", Data_int, "Type: ", type(Data_int))

Data_float = float(Data_int)
Data_str = str(Data_int)
Data_bool = bool(Data_int) #Akan False bila data: 0

print("Data: ", Data_float, "Type: ", type(Data_float))
print("Data: ", Data_str, "Type: ", type(Data_str))
print("Data: ", Data_bool, "Type: ", type(Data_bool))

## Float
print("========FLOAT========")

Data_float = 9.5
print("Data: ", Data_float, "Type: ", type(Data_float))

Data_int = int(Data_float)
Data_str = str(Data_float)
Data_bool = bool(Data_float) #Akan False bila data: 0

print("Data: ", Data_int, "Type: ", type(Data_int))#Akan dibulatkan Ke Bawah
print("Data: ", Data_str, "Type: ", type(Data_str))
print("Data: ", Data_bool, "Type: ", type(Data_bool))

## Float
print("========STRING========")

Data_str = "0"
print("Data: ", Data_str, "Type: ", type(Data_str))

Data_int = int(Data_str)#String harus Angka
Data_float = float(Data_str)#String harus Angka
Data_bool = bool(int(Data_str)) #Akan False bila String kosong

print("Data: ", Data_int, "Type: ", type(Data_int))
print("Data: ", Data_float, "Type: ", type(Data_float))
print("Data: ", Data_bool, "Type: ", type(Data_bool))

## Bool
print("========BOOL========")

Data_bool = True
print("Data: ", Data_bool, "Type: ", type(Data_bool))

Data_int = int(Data_bool)
Data_float = float(Data_bool)
Data_str = str(Data_bool) #Akan False bila data: 0

print("Data: ", Data_int, "Type: ", type(Data_int))
print("Data: ", Data_float, "Type: ", type(Data_float))
print("Data: ", Data_str, "Type: ", type(Data_str))

