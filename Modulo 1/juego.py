#Apocalypse

print("Estas siendo perseguido por una horda la cual te esta dejando sin muchas opciones con respecto a donde ir")
print("Despues de correr por un rato te encuentras con tres opciones las cuales parecen viables para esconderte:")

print("Un callejon oscuro el cual parece desierto a primera vista")

print("Una casa que parece estar abandonada")

print("Un minimarket que puede que tenga algo de valor")

opcion = input("¿En donde prefieres esconderte? 1. CALLEJON    2. CASA   3. MINIMARKET: ").strip().lower()

if opcion == "callejon": 
    print("Te metes en el callejon y vez pasar algunos de los infectados pero sabes que los siguientes puede que te vean. Piensas en irte a la otra calle o esperar detras de un tacho de basura a que pase la horda")
    
    opcion = input("¿Que decides?   1. QUEDARSE   2. IRSE: ").strip().lower()
    
    if opcion == "quedarse":
        print("Te quedaste y debido a que la horda es muy grande algunos infectados te vieron y no corriste con la misma suerte del principio. Fin")
    elif opcion == "irse":
        print("Decidiste tomar una ruta de emergencia y lograste salir vivo de esta")
    else:
        print("Como no tomaste ninguna decision los infectados te acorralaron y encontraste tu fin.")
        
elif opcion == "casa":
    print("Decidiste entrar en la casa pero al cerrar la puerta escuchas lo que parecen ser pasos en el segundo piso. ¿Quieres inspeccionar la casa o prefieres quedarte en la sala?")
    
    
    opcion = input("¿que prefieres? 1. INSPECCIONAR   2. QUEDARSE: ").strip().lower()
    if opcion == "inspeccionar":
        print("Te armas con un bate y al inspeccionar la casa te encuentras una pistola en una mesa pero tambien a un infectado. Tienes que eliminar la amenaza antes de que te detecte")
        
        opcion = input("¿Que decides usar? 1. BATE   2. PISTOLA: ").strip().lower()
        
        if opcion == "bate": 
            print("Le das un golpe certero detras de la cabeza al infectado eliminandolo en un instante. Al ver por una ventana del segundo piso ves como la horda va pasando y pierde tu rastro. Fin")

        elif opcion == "pistola":
            print("Tomaste la pistola y le diste un tiro certero al infectado derribandolo al instante, pero no contaste con que el sonido del disparo fuera tan fuerte como para dejarte sordo por un rato y que tambien atraeria la atencion de los demas infectados. La horda entro a la casa y no hubo escapatoria. Fin.")             
    
    elif opcion == "quedarse":
        print("Te quedaste en la sala de la casa y no te diste cuenta de que un infectado habia bajado del segundo piso  te ataco por sorpresa. Fin")
elif opcion == "minimarket":
        print("Entraste en el minimarket, afortunadamente lograste encontrar comida y demas suministros. Mientras guardabas lo que podias en tu mochila escuchas pasar a la horda pero tambien viste que algo se movio en la parte de atras del minimarket. ¿iras a investigar o prefieres salir del establecimiento?")
        
        opcion = input("¿Que haras ahora? 1. INVESTIGAR   2. SALIR: ").strip().lower()
            
        if opcion == "investigar":
                print("Al investigar el movimiento que viste resulto que era simplemente un mapache. Cierras las puertas principales, saqueas lo que puedes y sobrevives. Fin")
        elif opcion == "salir":
                print("Decidiste salir y por mal azar coincidiste con la horda que estaba pasando. Agotado y desesperanzado simplemente aceptas tu destino. Fin")
else:
    print("No tomaste ninguna decision y fuiste alcanzado por la horda.Fin")