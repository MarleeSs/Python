# menyambung string
namaPertama = 'Marli'
namaTengah  = 'Sumarli'
namaAkhir   = 'Ganteng'

namaLengkap = namaPertama + namaTengah + namaAkhir
print(namaLengkap)

namaLengkaps = namaPertama +" "+ namaTengah +" "+ namaAkhir
print(namaLengkap)


# Menghitung panjang string
panjang = len (namaPertama)
print(panjang)

# Indexing
print("index ke-0 >>", namaLengkap[0])
print("index ke-1 >>", namaLengkap[1])
print("index ke-2,3 >>", namaLengkap[1:3])
print("index ke-(-1,-0) >>", namaLengkap[-9])

# item paling besar
print("Karakter paling besar adalah " + max(namaLengkap))
# item paling kecil
print("Karakter paling kecil adalah " + min(namaLengkap))

# Melihat Value dari karakter String
ascii_code = ord("G")
print("Ascii code untuk G adalah " + str(ascii_code))
data = 5
print("Char untuk ASCII adalah " + chr(data))

# oprator dalam bentuk method

data1 = '0xAAs01jAhd99MHD9xaIDojASKxjzijAi'
jumlah = data1.count('A')
print("Jumlah char huruf A pada (" + data1 + ") = " + str(jumlah))