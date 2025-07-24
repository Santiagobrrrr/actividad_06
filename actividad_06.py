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
            print(f"La suma es de {sum_user}\n")

        case "2":
            sum_user = 0

            for i in range(how_numbers):
                numbers_user = float(input(f"Ingrese su número: "))
                sum_user += numbers_user
            print(f"El promedio es de {sum_user/how_numbers}\n")

        case "3":
            count_positive = 0
            count_negative = 0
            for i in range(how_numbers):
                if i > 0:
                    count_positive += 1
                if i < 0:
                    count_negative += 1
            print(f"Cantidad de positivos es de {count_positive}\n"
                  f"Cantidad de negativos es de {count_negative}\n")

        case _:
            print(f"VALOR INVÁLIDO")

def area_triangle():
    l1 = int(input("Ingrese la longitud de la base: "))
    l2 = int(input("Ingrese la longitud de la altura: "))
    return print(f"El área del triángulo es de {(l1 * l2) / 2} unidades^2\n")

def even_or_odd():
    user_number = float(input(f"Ingrese un número: "))
    if user_number % 2 == 0:
        print(f"El numero {user_number} es par\n")
    else:
        print(f"El numero {user_number} es impar\n")

def avg_qualification():
    sum_qualification = 0
    qualification_number = int(input("Ingrese la cantidad de calificaciones a ingresar: "))
    for i in range(qualification_number):
        number_qualification = float(input(f"Ingrese la calificación {i + 1}: "))
        sum_qualification += number_qualification
    return print(f"El promedio de las {qualification_number} es de {sum_qualification/qualification_number}\n")

def greater_and_less():
    how_numbers = int(input("¿Cuántos números desea ingresar?: "))
    number_user = float(input(f"Ingrese el numero 1: "))
    number_user_greater = number_user
    number_user_less = number_user
    for i in range(1,how_numbers):
        number_user = float(input(f"Ingrese el numero {i + 1}: "))
        if number_user > number_user_less:
            number_user_greater = number_user
        elif number_user < number_user_less:
            number_user_less = number_user
    print(f"El numero mas grande es {number_user_greater}")
    print(f"El numero menor es {number_user_less}\n")


while True:
    print(f"MENÚ")
    print(f"1. SUMA - PROMEDIO - POSTITIVO O NEGATIVO")
    print(f"2. CALCULAR ÁREA DEL TRIÁNGULO")
    print(f"3. VERIFICACIÓN DE PAR O IMPAR")
    print(f"4. PROMEDIO DE CALIFICACIONES")
    print(f"5. VERIFICACIÓN DE NUMERO MAYOR Y MENOR")
    print(f"6. SALIR")

    option_user = input(f"Ingrese una de las opciones (1-6): ")

    match option_user:
        case "1":
            enter_numbers()

        case "2":
            print(f"Calcular área del triángulo")
            area_triangle()

        case "3":
            print(f"Verificación de numeros (par o impar)")
            even_or_odd()

        case "4":
            print(f"Promedio de calificaciones")
            avg_qualification()

        case "5":
            print(f"Verificación de numero mayor o menor")
            greater_and_less()

        case "6":
            print(f"Ha salido del programa, nos vemos...")
            break

        case _:
            print(f"Valor erroneo ingresado, intente de nuevo")