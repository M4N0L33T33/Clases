
  
while True:
    p = int(input("Que necesitas?\nCalculadora: en caso de no seguir necesitando, seleccione salir (0) \n- Sin obstaculos (1)\n- Con obstaculos (2) \nRespuesta: "))

    if p == 1:
        print("")
        print("solo usar en medidas de kilometros y GHz, saludos puto")
        d = int(input("distancia? (km): "))
        f = float(input("frecuencia? (GHz): "))
        r = 17.32 * ((d / 4 * f) **0.5)  
        print("Resultado = ", round(r,3), "km")
        print("\n-----\n-----\n-----")
    
    elif p == 2:
        print("")
        print("solo usar en medidas de kilometros y GHz, saludos puto")
        d = float(input("distancia? (Km): "))
        f = float(input("frecuencia? (GHz): "))
        d1 = float(input("medida del obstaculo?: "))
        d2 = d - d1
        r = 17.32 * (((d1*d2)/(d*f))**0.5)
        print("Resultado = ", round(r,3), "km")
        print("\n-----\n-----\n-----")
    
    elif p == 0:
        break
    
    