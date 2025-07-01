numero = float(input("Introduce un numero: "))

minimo= 50
maximo = 150

if minimo <= numero <= maximo:
    print(f"El numero {numero} esta dentro del rango de {minimo} a {maximo}.")
else:
    print(f"El numero {numero} esta fuera del rango de {minimo} a {maximo}.")