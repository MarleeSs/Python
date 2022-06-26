# Convert Celcius
print("~~~ Celcius Converter ~~~\n")

celcius = float(input("Input Celcius : "))
print("Temp Celcius      = ", celcius,'C')

# Reamur
reamur = (4/5)*celcius
print("Temp Reamur       = ", reamur,'R')

# Fahrenheit
faherenheit = ((9/5)*celcius)+32
print("Temp Fahrenheit   = ", faherenheit,'F')

# Kelvin
kelvin = celcius + 273
print("Temp Kelvin       = ", kelvin,'K\n')

# CONVERTER REAMUR
print("~~~ Reamur Converter ~~~\n")

reamur = float(input("Input Reamur : "))
print("Temp Reamur       =", reamur,'R')

# Celcius
celcius = 5/4*reamur
print("Temp Celcius      =", celcius,'C')

# Fahrenheit
faherenheit = ((9/4)*reamur)+32
print("Temp Fahrenheit   =", faherenheit,'F')

# Kelvin
kelvin = ((5/4)*reamur) + 273
print("Temp Kelvin       =", kelvin,'K\n')

# CONVERTER FAHRENHEIT
print("~~~ Fahrenheit Converter ~~~\n")

faherenheit = float(input("Input Fahrenheit : "))
print("Temp Fahrenheit       =", faherenheit,'F')

# Celcius
celcius = 5/9*(faherenheit-32)
print("Temp Celcius      =", celcius,'C')

# Reamur
reamur = 4/9*(faherenheit-32)
print("Temp reamur   =", reamur,'F')

# Kelvin
kelvin = 5/9*(faherenheit-32) + 273
print("Temp Kelvin       =", kelvin,'K\n')

# CONVERTER KELVIN
print("~~~ Kelvin Converter ~~~\n")

kelvin = float(input("Input Kelvin : "))
print("Temp Kelvin       =", kelvin,'K')

# Celcius
celcius = kelvin-273
print("Temp Celcius      =", celcius,'C')

# Reamur
reamur = 4/5*(kelvin-273)
print("Temp reamur   =", reamur,'R')

# Fahrenheit
faherenheit = 9/5*(kelvin-273)+32
print("Temp Fahrenheit       =", kelvin,'F\n')