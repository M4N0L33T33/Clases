import os
        #limpieza
if os.name == "profix":
    os.system("clear")
else:
    os.system("cls")

tabla = int(input("Que tabla de multiplicar quieres tener? "))
l = int(input("Hasta donde quieres llegar? "))

for x in range(1,l+1):
    print(tabla ," x ", x ,"= ", x*tabla)
