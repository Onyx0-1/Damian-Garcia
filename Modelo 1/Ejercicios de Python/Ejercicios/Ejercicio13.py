numero = int(input("Dame un numero entero: "))

es_par = numero % 2 == 0

en_rango = 20 <= numero <= 50

if es_par and en_rango:
    print(f"El numero {numero} es par y está dentro del rango de 20 a 50.")
elif es_par and not en_rango:
    print(f"El numero {numero} es par, pero no está en el rango de 20 a 50.")
elif not es_par and en_rango:
    print(f"El numero {numero} está en el rango de 20 a 50, pero no es par.")
else:
    print(f"El numero {numero} no es par ni está dentro del rango de 20 a 50.")