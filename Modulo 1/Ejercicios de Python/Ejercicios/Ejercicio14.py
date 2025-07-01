calificacion = int(input("Introduce una calificacion del 1 al 100: "))

if 90 <= calificacion <= 100:
    letra = "A"
elif 80 <= calificacion <= 89:
    letra = "B"
elif 70 <= calificacion <= 79:
    letra = "C"
elif 60 <= calificacion <= 69:
    letra = "D"
elif 0 <= calificacion < 60:
    letra = "F"

    
if letra:
    print(f"Sacaste: {letra}")
else:
    print("No valido, por favor introduce un numero entre 0 y 100.")