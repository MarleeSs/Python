#Data INTEGER
print("====INTEGER====")
data_int = 10;
data_float = float(data_int)
data_bool = bool (data_int)#akan False jika nilai integer = 0
data_str = str(data_int)
print(data_int)

print("data", data_int, "type :", type(data_int))
print("data", data_float, "type :", type(data_float))
print("data", data_bool, "type :", type(data_bool))
print("data", data_str, "type :", type(data_str))

#Data Float
print("====FLOAT====")
data_float  = 10.5;
data_int    = int(data_float)#akan dibulatkan kebawah
data_bool   = bool (data_float)#akan False jika nilai float = 0
data_str    = str(data_float)
print(data_float)

print("data", data_float, "type :", type(data_float))
print("data", data_int, "type :", type(data_int))
print("data", data_bool, "type :", type(data_bool))
print("data", data_str, "type :", type(data_str))

#Data Boolean
print("====BOOLEAN====")
data_bool    = True;
data_int     = int(data_bool)#jika False maka hasilnya = 0
data_float   = float (data_bool)#jika False maka hasilnya = 0
data_str     = str(data_bool)
print(data_bool)

print("data", data_bool, "type :", type(data_bool))
print("data", data_int, "type :", type(data_int))
print("data", data_float, "type :", type(data_float))
print("data", data_str, "type :", type(data_str))

#Data String
print("====STRING====")
data_str     = "10";
data_int     = int(data_str)#harus angka, jika tidak angka maka akan error
data_float   = float (data_str)#harus angka, jika tidak angka maka akan error
data_bool    = bool(data_str)#jika String kosong maka = False
print(data_str)

print("data", data_str, "type :", type(data_str))
print("data", data_int, "type :", type(data_int))
print("data", data_float, "type :", type(data_float))
print("data", data_bool, "type :", type(data_bool))