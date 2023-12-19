import os

ciclo1 = 1 #llave ciclo1
ciclo2 = 1 #llave ciclo2



while ciclo1 ==1:
    print("ingresa 2 números para imprimir su rango")
    print("")
    n1 = int(input("valor 1: "))
    n2 = int(input("valor 2: "))

    while ciclo2 == 1:
        os.system("cls")
        print(n1)
        input("")
        n1 = n1 + 1
        if n1 > n2:
            ciclo2 = 2

    print("Quiere continuar? ")
    print("1 = sí")
    print("2 = nó")
    print("")
    r = int(input())
    if r == 1:
        ciclo2 = 1
    else:
        ciclo1 = 2

    os.system("cls")
print("Hasta Luego :D")
input("")

    


