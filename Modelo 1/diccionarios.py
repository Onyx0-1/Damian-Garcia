#diccionario


mi_diccionario = {

     "Arianyelina": 15,
     "Brian": 10,
     "Carlos": 18,
     "Damian": 13,
     "Deicel": 13,
     "Elias": 18,
     "Fabian": 17,
     "Franklin": 17,
     "Helianny": 16,
     "Liliana": 14,
     "Maria": 16,
     "Over": 16,
     "Paul": 14,
     "Ronald": 12,
     "Yuliexy": 10

}

print("notas de los estudiantes: ", mi_diccionario)

mi_diccionario["Arianyelina"]=21
mi_diccionario["brian"]=21
mi_diccionario["carlos"]=21
mi_diccionario["Damian"]=20
mi_diccionario["Deicel"]=21
mi_diccionario["franklin"]=20
mi_diccionario["Helianny"]=21
mi_diccionario["Liliana"]=20
mi_diccionario["Elias"]=21
mi_diccionario["Maria"]=25
mi_diccionario["over"]=21
mi_diccionario["Paul"]=21
mi_diccionario["Ronald"]=21
mi_diccionario["Yuliexy"]=21

print("edad de los estudiantes: ", mi_diccionario)

print(" el nombre 'Damian' esta en la lista?", "Damian" in mi_diccionario)

for clave in mi_diccionario:
    print(f"Nombre: {clave}, Nota: ¨{Clave[mi_diccionario]}")


    #Conjuntos

    conjunto={1, 2, 3, 4, 5}
    print("el numero 3 esta en el conjunto?", 3 in conjunto)

    conjunto.add(6)
    print("se añadio en numero 6 al conjunto: ", conjunto)

    conjunto.add(3)
    print(conjunto)

    conjunto.remove(2)
    print("se elimino el numero 2 del conjunto: ", conjunto)

    conjunto.discard(3)
    print("se elimino el 3: ", conjunto)

    #longitud

    print("longitud del conjunto", len (conjunto))

    for elemento in conjunto:
        print("elemento de conjunto", elemento)


#diferente!=    
 
 
conjunto_a={1,2,3}
conjunto_b={3,4,5}
print("union a y b:", conjunto_a | conjunto_b) 
print("union a y b:", conjunto_a & conjunto_b)
    