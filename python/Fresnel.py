
  
while True:
    p = int(input("Que necesitas?\nCalculadora: en caso de no seguir necesitando, seleccione salir (0) \n- Sin obstaculos (1)\n- Con obstaculos (2) \nRespuesta: "))

    if p == 1:
        print("")
        print("solo usar en medidas de metros y megahz, saludos puto")
        d = int(input("distancia? (m): "))
        f = int(input("frecuencia? (mHz): "))
        r = 17.32 * ((d / (4 * f))**0.5)
        print("Resultado = ", round(r,3), "km")
        print("\n-----\n-----\n-----")
    
    elif p == 2:
        print("")
        print("solo usar en medidas de metros y megahz, saludos puto")
        d = int(input("distancia? (m): "))
        f = int(input("frecuencia? (mHz): "))
        d1 = int(input("medida del obstaculo?: "))
        d2 = d - d1
        r = 17.32 * (((d1*d2)/(d*f))**0.5)
        print("Resultado = ", round(r,3), "km")
        print("\n-----\n-----\n-----")
    
    elif p == 0:
        break
    
    