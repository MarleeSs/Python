# NOT, OR, AND, XOR

# Jika(NOT)nya merujuk ke <a>, maka kebalikannya.
print('====  NOT  ====\n')
a = False
c = not a
print('Data Boolean = ', a)
print('Data (NOT) = ', c)

# OR
# Jika salah satu True, maka hasilnya True, Seperti pertambahan
print('\n====   OR   ====\n')
a = False
b = False
c = a or b
print(a, ' OR ', b, ' = ', c)
a = True
b = False
c = a or b
print(a, '  OR ', b, ' = ', c)
a = False
b = True
c = a or b
print(a, ' OR ', b, '  = ', c)
a = True
b = True
c = a or b
print(a, '  OR ', b, '  = ', c)

# AND
# Jika dua buah nilai True, maka hasilnya True. Dan sama seperti Dikalikan.
print('\n====   AND   ====\n')
a = False
b = False
c = a and b
print(a, ' AND ', b, ' = ', c)
a = True
b = False
c = a and b
print(a, '  AND ', b, ' = ', c)
a = False
b = True
c = a and b
print(a, ' AND ', b, '  = ', c)
a = True
b = True
c = a and b
print(a, '  AND ', b, '  = ', c)

# XOR(^)
# Akan True jika salah satu True sisanya False
print('\n====   XOR(^)   ====\n')
a = False
b = False
c = a ^ b
print(a, ' XOR(^) ', b, ' = ', c)
a = True
b = False
c = a ^ b
print(a, '  XOR(^) ', b, ' = ', c)
a = False
b = True
c = a ^ b
print(a, ' XOR(^) ', b, '  = ', c)
a = True
b = True
c = a ^ b
print(a, '  XOR(^) ', b, '  = ', c)