import os

ciclo = 0

total = 0
par = 0
impar = 0
os.system("cls")
while ciclo == 0:
    r = int(input("""ingresa un número
    """))
    print("")
    calculo = r % 2
    if calculo == 0:
        print("par")
        par = par + 1 #cuenta de números pares ingresados
    else:
        print("impar")
        impar = impar + 1 #cuenta de números impares ingresados
    input("")

    total = total + 1 #cuenta total de n° consultados

    os.system("cls")
    
    r_2 = int(input("""quieres consultar otro número?
    1.- sí
    2.- no
    
    """))

    os.system("cls")
    
    if r_2 == 1:
        ciclo = 0
    else: 
        ciclo = 1
print("El total de números ingresados fueron ",total,"de los cuales:")
print(par," fueron pares")
print(impar,""" fueron impares
Nos vemos :D
""")
