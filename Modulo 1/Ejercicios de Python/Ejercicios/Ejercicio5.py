monto_original = float(input("Por favor, dame el monto original de la compra: "))

porcentaje_descuento = float(input("Por favor, dame el porcentaje de descuento: "))

monto_descuento = monto_original * (porcentaje_descuento / 100)

precio_final = monto_original - monto_descuento

print("El monto del descuento es: ", monto_descuento)
print("El precio final despues del descuento es: ", precio_final)