funcion1 = [150, 0]
funcion2 = [180, 0]
compradores = []

def comprar_entrada():
    NombreComprador = input("Ingrese su nombre: ")

    while NombreComprador in compradores:
        print("Error: El nombre ya ha sido registrado.")
        NombreComprador = input("Ingrese otro nombre del comprador: ")
    compradores.append(NombreComprador)
    
    print("Seleccione función: \n 1. Cats Día Viernes (150 entradas) \n 2. Cats Día Sábado (180 entradas)")
    while True:
        try:
            funcion = int(input("Función (1 ó 2): "))
            if funcion == 1:
                if funcion1[0] > 0:
                    funcion1[0] -= 1
                    funcion1[1] += 1
                    print(f"Entrada registrada en función 1! Stock restantes: {funcion1[0]}")
                    break
                else:
                    print("No hay entradas disponibles para la función 1.")
            elif funcion == 2:
                if funcion2[0] > 0:
                    funcion2[0] -= 1
                    funcion2[1] += 1
                    print(f"Entrada registrada en función 2! Stock restantes: {funcion2[0]}")
                    break
                else:
                    print("No hay entradas disponibles para la función 2.")
            else:
                print("Error: opción de función inválida.")
        except ValueError:
            print("Error: opción de función inválida.")

def cambio_funcion():
    nombre_comprador = input("-- Cambio de función --\nNombre del comprador: ")
    if nombre_comprador not in compradores:
        print("Error: comprador no encontrado.")
        return
    
    respuesta = input("¿Desea cambiar de función?  (S/N): ").strip().lower()
    if respuesta == "s":
        print("Seleccione nueva función:")
        print("1. Cats Día Viernes")
        print("2. Cats Día Sábado")
        while True:
            try:
                nueva_funcion = int(input("Función (1 ó 2): "))
                if nueva_funcion == 1 and funcion1[0] > 0:
                    funcion1[0] -= 1
                    funcion1[1] += 1
                    funcion2[0] += 1
                    funcion2[1] -= 1
                    print(f"Cambio exitoso. Ahora está en función 1")
                    break
                elif nueva_funcion == 2 and funcion2[0] > 0:
                    funcion2[0] -= 1
                    funcion2[1] += 1
                    funcion1[0] += 1
                    funcion1[1] -= 1
                    print(f"Cambio exitoso. Ahora está en función 2")
                    break
                else:
                    print("Error: No hay entradas disponibles para esta función.")
            except ValueError:
                print("Error: Opción de función inválida.")
    else:
        print("Cambio cancelado.")

def mostrar_stock():
    print("-- Stock de Funciones --")
    print(f"Función 1 (Viernes): Disponibles {funcion1[0]}, Vendidas {funcion1[1]}")
    print(f"Función 2 (Sábado): Disponibles {funcion2[0]}, Vendidas {funcion2[1]}")

def menu():
    while True:
        try:
            opt = int(input("TOTEM AUTOATENCIÓN CAFECONLECHE \n 1.- Comprar entrada a Cats.\n 2.- Cambio de función.\n 3.- Mostrar stock de funciones.\n 4.- Salir \n Ingrese una opcion: "))

            if opt == 1:
                comprar_entrada()
            elif opt == 2:
                cambio_funcion()
            elif opt == 3:
                mostrar_stock()
            elif opt == 4:
                print("Muchas gracias por usar el totem! ")
                break
        except ValueError:
            print("Debe ingresar una opción válida!!")

menu()