cesta = []

while True:
    print("\n   MENU   ")
    print("1. Agregar un nuevo elemento")
    print("2. Mostrar cesta de la compra")
    print("3. Eliminar un elemento")
    print("4. Calcular el total")
    print("5. Renunciar")

    opcion = input("Elige una opcion (1-5): ")

    if opcion == "1":
        nombre = input("Nombre del producto: ")
        precio = float(input("Precio del producto: "))
        cesta.append((nombre, precio))
        print(f"'{nombre}' agregado a la cesta por ${precio}")

    elif opcion == "2":
        if not cesta:
            print("La cesta esta vacia.")
        else:
            print("Cesta de la compra:")
            for i, (nombre, precio) in enumerate(cesta, 1):
                print(f"{i}. {nombre} - ${precio}")

    elif opcion == "3":
        if not cesta:
            print("No hay elementos para eliminar.")
        else:
            for i, (nombre, precio) in enumerate(cesta, 1):
                print(f"{i}. {nombre} - ${precio}")
            indice = int(input("¿Que numero de producto deseas eliminar?: "))
            if 1 <= indice <= len(cesta):
                eliminado = cesta.pop(indice - 1)
                print(f"'{eliminado[0]}' eliminado de la cesta.")
            else:
                print("Numero invalido.")

    elif opcion == "4":
        total = sum(precio for _, precio in cesta)
        print(f"Total a pagar: ${total}")

    elif opcion == "5":
        print("Hasta luego.")
        break

    else:
        print("Opción invalida. Intenta otra vez.")