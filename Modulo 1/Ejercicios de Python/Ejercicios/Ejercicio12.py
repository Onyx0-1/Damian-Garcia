respuesta1 = input("¿Tienes licencia de conducir? 1.si 2.no: ").strip().lower()
respuesta2 = input("¿Tienes más de 18 años? 1.si 2.no: ").strip().lower()

respuesta1 = input("¿Tienes licencia de conducir? 1.si 2.no: ").strip().lower()
respuesta2 = input("¿Tienes mas de 18 años? 1.si 2.no: ").strip().lower()

tiene_licencia = respuesta1 == "si"
es_mayor_de_edad = respuesta2 == "si"

if tiene_licencia and es_mayor_de_edad:
    print(" Puedes conducir: tienes licencia y eres mayor de edad.")
elif tiene_licencia or es_mayor_de_edad:
    print(" solo se cumple uno de los requisitos. Se necesita tener ambos para poder conducir.")
else:
    print(" No puede conducir: no cumples con ninguno de los requisitos.")

if not tiene_licencia:
    print("No tienes licencia de conducir.")
if not es_mayor_de_edad:
    print("No eres mayor de edad.")