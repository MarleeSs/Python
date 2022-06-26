#Data INTEGER
print("====Input Data Integer====")
Data = int(input("Masukan Bilangan Bulat : "))
print("Angka",Data,"Adalah Tipe", type(Data), "\n")

#Data FLOAT
print("====Input Data Float====")
Data = float(input("Masukan Bilangan Desimal Dengan '.' : "))
print("Bilangan",Data,"Adalah Tipe", type(Data), "\n")

#Data BOOLEAN
print("====Input Angka Boolean====")
Data = int(input("Masukan Angka Biner (1/0) : "))
Data_bool = bool(Data)
print("Angka",Data,"Adalah",Data_bool, "\n")

#Data STRING
print("====Input Data String====")
Data = str(input("Masukan Huruf/Angka Apa Saja : "))
print((Data), "Adalah Tipe Data", type(Data))