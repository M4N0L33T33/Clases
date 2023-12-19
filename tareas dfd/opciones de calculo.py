import os
os.system("cls")

#valores a pedir
print("vamos a hacer una calculador en la que puedas realizar el cálculo que quieras sin necesidad de hacerlos todos al mismo tiempo")
input("(presiona enter para continuar)")

os.system("cls")





#opciones

r = 1 

while r==1: 
    print("escoge 2 valores para operar:")
    n1 = int(input("Valor 1: "))
    n2 = int(input("Valor 2: "))

    os.system("cls")

    print("1.-suma")
    print("2.-resta")
    print("3.-multiplicación")
    print("4.-división")
    print("")
    eleccion = int(input("Que operacion quieres realizar? con los números anteriormente elegidos: "))

    os.system("cls")
    
    if eleccion == 1:
        print("la suma de tus valores es: ",n1 + n2)
    if eleccion == 2:
        print("la resta de tus valores es: ",n1 - n2)
    if eleccion == 3:
        print("la multiplicación de tus valores es: ",n1 * n2)
    if eleccion == 4:
        print("la división de tus valores es: ",n1 / n2)
    print("")
    r = int(input("quieres realizar otra operacion? 1 para sí, 2 para no: "))
    os.system("cls")

print("Hasta luego :D")
input("")
     
