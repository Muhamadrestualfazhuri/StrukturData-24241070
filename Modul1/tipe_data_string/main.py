a = 'Halo'
b = "Python"
c = """Ini adalah
string multi-baris"""
print(type(a))  # <class 'str'>
print(type(b))  # <class 'str'>
print(type(c))  # <class 'str'>

# indexing dan slicing 
text = "HIKHAM"
print(text[0])     # Output: H
print(text[-1])    # Output: M
print(text[0:3])   # Output: HIK
print(text[:4])    # Output: HIKH
print(text[::2])   # Output: HKA (loncat 2 karakter)

# Operasi penggabungan string
print('Hello ' + 'HIKHAM')

# Operasi pengulangan string
print('HOHO' * 3)

# Operasi Pengecekan string
print('a' in 'data') # menghasilkan boolean (True/False)

# Operasi panjang string
print(len('HIKHAM'))

s = "hikham programming"
print(s.upper())       # 'HIKHAM PROGRAMMING'
print(s.capitalize())  # 'Hikham programming'
print(s.title())       # 'Hikham Programming'
print(s.replace("hikham", "java"))  # 'java programming'
print(s.split())       # ['HIKHAM', 'programming']
print(s.find("gram"))  # 10 

# F-String
# String format menggunakan F-String
name = "Hikham"
age = 21
print(f"Halo, nama saya {name}, umur saya {age}")

# Format Method
# String format dengan format method
print("Halo, nama saya {}, umur saya {}".format(name, age))

