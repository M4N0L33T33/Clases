import os

ciclo = 0
print("""este es un programa que te dice si un número es par o no
""")
while ciclo == 0:
    r = int(input("""ingresa un número
    """))
    print("")
    calculo = r % 2
    if calculo == 0:
        print("par")
    else:
        print("impar")
    input("")
    
    os.system("cls")

    r_2 = int(input("""quieres consultar otro número?
    1.- sí
    2.- no
    """))
    if r_2 == 1:
        ciclo = 0
    else: 
        ciclo = 1