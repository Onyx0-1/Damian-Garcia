numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo numero: "))
numero3 = float(input("Introduce el tercer numero: "))

resultado = numero1 > numero2 and numero2 > numero3

print(f"¿El primer número es mayor que el segundo y el segundo mayor que el tercero? {resultado}")