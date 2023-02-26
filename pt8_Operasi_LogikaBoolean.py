# Operasi logika / Boolean

# not, or, and, xor

# (not) kebalikan dari hasil boolean pada assigment
print('====NOT====')
a = True
b = False
c = not a
d = not b

print('data a = ', a)
print('Setelah diberi (not)')
print('Data c = ', c)
print('------------------')
print('Data b = ', b)
print("Setelah diberi (not)")
print('Data d = ', d)

# (or) ibarat +1 
print('====OR====')
a = False
b = False
c = a or b

print(a,"or", b ,"=", c)
a = True
b = False
c = a or b

print(a,"or", b ,"=", c)
a = False
b = True
c = a or b

print(a,"or", b ,"=", c)
a = True
b = True
c = a or b

print(a,"or", b ,"=", c)

# (and) ibarat 0*
print('====AND====')
a = False
b = False
c = a and b

print(a ,"and", b , "=", c)
a = True
b = False
c = a and b

print(a ,"and", b , "=", c)
a = False
b = True
c = a and b

print(a ,"and", b , "=", c)
a = True
b = True
c = a and b

print(a ,"and", b , "=", c)

# (xor) ia akan True jika hanya salah satu 
# dari nilai True,jika tidak maka False
print('====XOR====')
a = False
b = False
c = a ^ b

print(a ,"and", b , "=", c)
a = True
b = False
c = a ^ b

print(a ,"and", b , "=", c)
a = False
b = True
c = a ^ b

print(a ,"and", b , "=", c)
a = True
b = True
c = a ^ b

print(a ,"and", b , "=", c)