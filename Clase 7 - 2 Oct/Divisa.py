import os

#limpieza
if os.name == "posix":
    os.system ("clear")
else:
    os.system ("cls")


dolar =  801.6
euro = 857.4
uf = 28993.7

for x in range(1,4):
        print("""Banco Oeste, que moneda quiere cambiar?
    1.- Dolares ($ 801.6)
    2.- Euro ($857.4)
    3.- UF ($28993.7)
    4.- Salir 
    """)
        r = int(input())
        if r==1: #dolar
            r2 = int(input("""1.- Peso chileno a dólar
2.- Dólar a peso chileno\n"""))
            if r2 == 1:
                op = int(input("Ingresa cantidad de pesos chilenos deseas cambiar a dolar: "))
                print("Total en Dolar: $", op/dolar)
                input()
            else:
                input("Presione enter para hacer de nuevo la operación.")
            if r2 == 2:
                op = int(input("Ingresa cantidad de dolares deseas cambiar a pesos chilenos: "))
                print("Total en Pesos chilenos: $", op*dolar)   
                input()
            else:
                input("Presione enter para hacer de nuevo la operación.")


        if r==2: #euro
            r2 = int(input("""1.- Peso chileno a euro
2.- Euro a peso chileno\n"""))
            if r2 == 1:
                op = int(input("Ingresa cantidad de pesos chilenos deseas cambiar a euros: "))
                print("Total en Euro: $", op/euro)
                input()
            if r2 == 2:
                op = int(input("Ingresa cantidad de euros deseas cambiar a pesos chilenos: "))
                print("Total en Pesos chilenos: $", op*euro)
                input()
            if r2 < 1 or r2 > 2:
                input("Presione enter para hacer de nuevo la operación.")


        if r==3: #UF
            r2 = int(input("""1.- Peso chileno a UF
2.- UF a peso chileno\n"""))
            if r2 == 1:
                op = int(input("Ingresa cantidad de pesos chilenos deseas cambiar a UF: "))
                print("Total en UF: $", op/uf)
                input()
            if r2 == 2:
                op = int(input("Ingresa cantidad de UF deseas cambiar a pesos chilenos: "))
                print("Total en Pesos chilenos: $", op*uf)
                input()
            if r2 < 1 or r2 > 2:
                input("Presione enter para hacer de nuevo la operación.")
            
                #limpieza
        if os.name == "posix":
            os.system ("clear")
        else:
            os.system ("cls")
            
print("Ha llegado al límite de intentos")