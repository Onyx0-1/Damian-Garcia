numero1 = float(input("Dame el primer numero: "))
numero2 = float(input("Dame el segundo numero: "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2

if numero2 != 0:
    division = numero1 / numero2
else:
    division = "No se puede dividir entre cero"

print(f"Resultados:")
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicacion: {multiplicacion}")
print(f"Division: {division}")