while True:
    p = 0

    p = int(input("Que quieres calcular?\n1.- Longitud de Onda?\n2.- Frecuencia de Onda?\n3.- Cerrar programa\nRespuesta: "))

    while p == 1:
        print("Haz seleccionado longitud de onda\n ")
        vel_luz = 300000000

        hz = int(input("ingresa los Hz a calcular: "))

        calculo = vel_luz/hz

        print(round(calculo,2))

        break

    while p == 2:
        kHz = 10**3
        MHz = 10**6
        GHz = 10**9

        print("Haz seleccionado frecuencia de onda\n ")

        p_2 = int(input("que quieres calcular? Khz(1), MHz(2), GHz(3)\nRespuesta: "))

        while p_2 == 1:
            print("Haz seleccionado KHz.\n ")
            r = float(input("Por cuanto necesitas multiplicarlo?\nRespuesta: "))
            calculo = kHz*r
            print(round(calculo), "\n ")
            input("Presione para continuar")
            break

        while p_2 == 2:
            print("Haz seleccionado MHz.\n ")
            r = float(input("Por cuanto necesitas multiplicarlo?\nRespuesta: "))
            calculo = MHz*r
            print(round(calculo), "\n ")
            input("Presione para continuar")
            break
    
        while p_2 == 3:
            print("Haz seleccionado GHz.\n ")
            r = float(input("Por cuanto necesitas multiplicarlo?\nRespuesta: "))
            calculo = GHz*r
            print(round(calculo), "\n ")
            input("Presione para continuar")
            break

    if p == 3:
        break
