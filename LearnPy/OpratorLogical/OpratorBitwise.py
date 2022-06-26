# Bitwise (OR)
print('\n',12*"=", "OR", 12*"=",'\n')

a = 1
b = 2
# Eks
c = a | b

print("nilai :", a, "-> binary :", format(a,'08b'))
print("nilai :", b, "-> binary :", format(b,'08b'))

print(30*"=","(|)")

print("nilai :", c, "-> binary :", format(c,'08b'))

# Bitwise (AND)
print('\n',12*"=", "AND", 12*"=",'\n')

a = 1
b = 2
# Eks
c = a & b

print("nilai :", a, "-> binary :", format(a,'08b'))
print("nilai :", b, "-> binary :", format(b,'08b'))

print(30*"=","(&)")

print("nilai :", c, "-> binary :", format(c,'08b'))

# Bitwise (XOR)
print('\n',12*"=", "XOR", 12*"=",'\n')

a = 1
b = 2
# Eks
c = a ^ b

print("nilai :", a, "-> binary :", format(a,'08b'))
print("nilai :", b, "-> binary :", format(b,'08b'))

print(30*"=","(&)")

print("nilai :", c, "-> binary :", format(c,'08b'))

# Bitwise (NOT)
c = ~a

print('\n',12*"=", "NOT", 12*"=",'\n')

print("nilai :", a, "-> binary :", format(a,'08b'))

print(30*"=","(~)")

print("nilai :", c, "-> binary :", format(c,'08b'))

print(30*"=","(^)")

d = 0b00000001
e = 0b11111111

print("nilai :", d^e, "-> binary :", format(d^e,'08b'))

# Bitwise (Shift Right)
c = a >> 1

print('\n',12*"=", ">>", 12*"=",'\n')

print("nilai :", a, "-> binary :", format(a,'08b'))

print(30*"=","(>>)")

print("nilai :", c, "-> binary :", format(c,'08b'))

# Bitwise (Shift Left)
c = a << 1

print('\n',12*"=", "<<", 12*"=",'\n')

print("nilai :", a, "-> binary :", format(a,'08b'))

print(30*"=","(<<)")

print("nilai :", c, "-> binary :", format(c,'08b'))