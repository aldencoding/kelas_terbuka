data = "ini adalah string"
print(data)
print(type(data))

# 1. cara membuat string

'''
    1. Dengan cara single quote '...'
    2. Dengan cara double quote "..."

'''

print("Halo apa kabar?")
print('Halo apa kabar?')

# 2. Menggunakan tanda \

# membuat tanda ' string
print('mari shalat jum\'at')
print('g\'day, is isn\'t it?')

# backlash
print("c:\\user\\Ucup")

# tab
print("Nama Saya\tFarrel")

#backspace
print("Nama Saya \bFarrel")

# newline
print("Baris pertama. \nbariskedua.")
print("Baris pertama. \rbariskedua.")
print("Baris pertama. \r\nbariskedua.")

# 3. String literal atau raw

# hati hati
print('c:\new folder') # akan salah pathnya

# menggunakan raw string
print(r'c:\user\nama')

# multiline literal string
print("""
nama: Alden
usia: 20
web: https\ncom
""")

# multiline literal string dan raw
print(r"""
nama: Alden
usia: 20
web: https\ncom
""")