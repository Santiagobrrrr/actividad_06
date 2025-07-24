def enter_numbers():
    how_numbers = int(input("¿Cuántos números desea ingresar?: "))
    print(f"¿Qué opción desea ingresar?")
    print(f"1. Sumar")
    print(f"2. Promedio")
    print(f"3. Cantidad de Positivos o Negativos")
    option_do = input(f"Ingrese la opción a realizar: ")

    match option_do:
        case "1":
            sum_user = 0
            for i in range(how_numbers):
                numbers_user = float(input(f"Ingrese su número: "))
                sum_user += numbers_user
            print(f"La suma es de {sum_user}")
        case _:
            print(f"VALOR INVÁLIDO")

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
            enter_numbers()

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