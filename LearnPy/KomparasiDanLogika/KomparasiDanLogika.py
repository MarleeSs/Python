# Latihan Logika dan Komparasi

print('\n', 50*"=",'\n')

# ++++++10---------20+++++++
while True:
    try:
        InputUser = float(input("\nMasukan angka yang bernilai\n/Kurang dari 10/\n (atau)\n/Besar dari 20../\n>>> "))
    except ValueError:
        print("\n!!Silahkan Masukan angka!!\n")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        continue
    else:
        break

print('\n', 50*"=",'\n')

# ++++++++10--------
isKurangDari = InputUser < 10
print('Kurang dari = ', isKurangDari)

# --------20++++++++
isLebihDari  = InputUser > 20
print('Lebih dari  = ', isLebihDari)

# +++++++10---------20+++++++
isCorrect = isKurangDari or isLebihDari
print("Angka yang anda masukan adalah ", isCorrect)

print('\n', 50*"=",'\n')

# Lanjut
while True:
    try:
    
     get_jawab = input("Lanjut? (y/t) ")

    except ValueError:
        continue
    
    if get_jawab in(''):
        continue

    else:
        if  get_jawab in('y'):    
            break
        if get_jawab in('t'):
            exit()

print('\n', 50*"=",'\n')

# -------10+++++++++20-------
while True:
    try:
        InputUser = float(input("\nMasukan angka yang bernilai\n/Lebih dari 10/\n (dan)\n/Kurang dari 20../\n>>> "))
    except ValueError:
        print("\n!!Silahkan Masukan angka!!\n")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        continue
    else:
        break

print('\n', 50*"=",'\n')

# ---------10+++++++
IsLebihDari_1  = InputUser > 10
print('Lebih dari = ', IsLebihDari_1)

# +++++++20--------
isKurangDari_1  = InputUser < 20
print('Kurang dari  = ', isKurangDari_1)

# -------10++++++++20--------
isCorrect_1 = IsLebihDari_1 and isKurangDari_1
print("Angka yang anda masukan adalah ", isCorrect_1)

print('\n', 50*"=",'\n')

# Lanjut
while True:
    try:
    
     get_jawab = input("Lanjut lagi? (y/t) ")

    except ValueError:
        continue
    
    if get_jawab in(''):
        continue

    else:
        if  get_jawab in('y'):    
            break
        if get_jawab in('t'):
            exit()

print('\n', 50*"=",'\n')

# -----0+++++5----8+++++11-----
while True:
    try:
        InputUser = float(input(
            "\nMasukan angka yang bernilai\n/Lebih dari 0 kurang dari 5/\n (atau)\n/Lebih dari 8 Kurang dari 11../\n>>> ")
            )
    except ValueError:
        print("\n!!Silahkan Masukan angka!!\n")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        continue
    else:
        break

print('\n', 50*"=",'\n')

# -----0+++++5-----
IsLebihDari_2  = InputUser > 0 
IsKurangDari_2 = InputUser < 5
IsCorrect_2 = IsLebihDari_2 and IsKurangDari_2

print('Lebih dari 0 kurang dari 5   = ', IsCorrect_2)

# ----8+++++11-----
IsLebihDari_3  = InputUser > 8
IsKurangDari_3 = InputUser < 11
IsCorrect_3 = IsLebihDari_3 and IsKurangDari_3

print('Lebih dari 8 Kurang dari 11  = ', IsCorrect_3)

IsCorrect_3a = IsCorrect_2 or IsCorrect_3

print("Angka yang anda masukan adalah ", IsCorrect_3a)

print('\n', 50*"=",'\n')

# Lanjut
while True:
    try:
    
     get_jawab = input("Lanjut nih? (y/t) ")

    except ValueError:
        continue
    
    if get_jawab in(''):
        continue

    else:
        if  get_jawab in('y'):    
            break
        if get_jawab in('t'):
            exit()

print('\n', 50*"=",'\n')

# +++++0-----5+++++8-----1+++++
while True:
    try:
        InputUser = float(input(
            "\nMasukan angka yang bernilai\n/Kurang dari 0 Lebih dari 5/\n (atau)\n/Kurang dari 8 Lebih dari 11../\n>>> ")
            )
    except ValueError:
        print("\n!!Silahkan Masukan angka!!\n")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        continue
    else:
        break

print('\n', 50*"=",'\n')

# +++++0-----5+++++
IsKurangDari_4  = InputUser < 0
IsLebihDari_4 = InputUser > 5
IsCorrect_4 = IsKurangDari_4 or IsLebihDari_4

print('Kurang dari 0 Lebih dari 5   = ', IsCorrect_4)

# +++++8-----11+++++
IsKurangDari_5  = InputUser < 8
IsLebihDari_5 = InputUser > 11
IsCorrect_5 = IsKurangDari_5 or IsLebihDari_5

print('Kurang dari 8 Lebih dari 11  = ', IsCorrect_5)

IsCorrect_5a = IsCorrect_4 and IsCorrect_5

print("Angka yang anda masukan adalah ", IsCorrect_5a)

print('\n', 50*"=",'\n')