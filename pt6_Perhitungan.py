#Latihan Konversi ke satuan Suhu

print("\nPROGRAM KONVERSI TEMPERATUR\n")

Celcius = float(input("Masukan Suhu dalam Celcius: "))
print("Suhu Adalah: ", Celcius, " Celcius")

#Reamur
Reamur = (4/5) * Celcius
print("Suhu dalam Reamur: ", Reamur)


#Fahrenheit
Fahrenheit = ((9/5) * Celcius) + 32
print("Suhu dalam Fahrenheit: ", Fahrenheit)


#Kelvin
Kelvin = Celcius + 273
print("Suhu dalam Kelvin: ", Kelvin)

print("========PE ER========")

#Fahrenheit ke Kelvin
print("====Dalam Satuan Fahrenheit====")

Fahrenheit = float(input("Masukan Suhu dalam Fahrenheit: "))
print("Suhu dalam Fahrenheit: ", Fahrenheit)

Kelvin = (Fahrenheit + 459.67) * 5/9
print("Suhu dalam Kelvin: ", Kelvin)

#Kelvin ke Fahrenheit
print("====Dalam Kelvin====")

Kelvin = float(input("Masukan Suhu dalam Kelvin: "))
print("Suhu dalam Kelvin: ", Kelvin)

Fahrenheit = (Kelvin * 9/5) - 459.67
print("Suhu dalam Fahrenheit: ", Fahrenheit)