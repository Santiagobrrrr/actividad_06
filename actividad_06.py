while True:
    print(f"MENÚ")
    print(f"1. SUMA - PROMEDIO - POSTITIVO O NEGATIVO")
    print(f"2. CALCULAR ÁREA DEL TRIÁNGULO")
    print(f"3. VERIFICACIÓN DE PAR O IMPAR")
    print(f"4. PROMEDIO DE CALIFICACIONES")
    print(f"5. VERIFICACIÓN DE NUMERO MAYOR O MENOR DE LISTA")
    print(f"6. SALIR")

    option_user = input(f"Ingrese una de las opciones (1-6): ")

    match option_user:
        case "1":
            print(f"Ingrese una de las opciones disponibles: ")

        case "2":
            print(f"Calcular área del triángulo")

        case "3":
            print(f"Verificación de numeros (par o impar)")

        case "4":
            print(f"Promedio de calificaciones")

        case "5":
            print(f"Verificación de numero mayor o menor")

        case "6":
            print(f"Ha salido del programa, nos vemos...")
            break

        case _:
            print(f"Valor erroneo ingresado, intente de nuevo")