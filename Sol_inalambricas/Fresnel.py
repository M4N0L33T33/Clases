
  
while True:
    p = int(input("Que necesitas?\nCalculadora: en caso de no seguir necesitando, seleccione salir (0) \n- Sin obstaculos (1)\n- Con obstaculos (2)\nRespuesta: "))

    if p == 1:
        print("")
        print("solo usar en medidas de kilometros y GHz, saludos puto")
        d = int(input("distancia? (km): "))
        f = float(input("frecuencia? (GHz): "))
        r = 17.32 * ((d / (4 * f)) **0.5)  
        print("Resultado = ", round(r,4), "m")
        print("\n-----\n-----\n-----")
    
    elif p == 2:
        print("")
        print("solo usar en medidas de kilometros y GHz, saludos puto")
        d = float(input("distancia total? (Km): "))
        d1 = float(input("distancia TX? (Km): "))
        d2 = float(input("distancia RX? (Km): "))
        f = float(input("frecuencia? (GHz): "))
        r = 17.32 * (((d1*d2)/(d*f))**0.5)
        print("paso 1: d1*d2= ",d1*d2)
        print("paso 2: d*f= ",d*f)
        print("paso 3: (paso 1/paso 2)= ",(d1*d2)/(d*f))
        print("paso 4: (√paso 3)= ", ((d1*d2)/(d*f))**0.5)
        print("Resultado final = ", round(r,3), "m")
        print("\n-----\n-----\n-----")
    
    elif p == 0:
        break
    
    print(hola)
    