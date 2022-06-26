a = 8
b = 3

#Oprasi Pertambahan +
hasil = a + b
print(a, '+', b, '=' , hasil)

#Oprasi Pengurangan -
hasil = a - b
print(a, '-', b, '-' , hasil)

#Oprasi Pembagian /
hasil = a / b
print(a, '/', b, '=' , hasil)

#Oprasi Perkalian *
hasil = a * b
print(a, '*', b, '=' , hasil)

#Oprasi Eksponen (Pangkat) **
hasil = a ** b
print(a, '**', b, '=' , hasil)

#Oprasi Modulus %
# Sisa bagi
hasil = a % b
print(a, '%', b, '=' , hasil)

#Oprasi Floor Division //
# Dibulatkan kebawah
hasil = a // b
print(a, '//', b, '=' , hasil)


#Prioritas Oprasi
'''
    1.()
    2.Exponent **
    3.Perkalian dan Batur-baturnya * / % //
    4.Pengurangan dan Pertambahan + -
'''

x = 7
y = 3
z = 16

hasil = x ** y * z / x + y // y - z % y
# print(x, '**', y, '*', z, '/', x, '+', y, '//', y, '-', z, '%', y, '=', hasil)

#Kurung akan mengambil langka pertama
# hasil = (x-y) * z
# print('(', x, '-', y, ')', '*', z, '=', hasil)