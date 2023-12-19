import os
        #limpieza
if os.name == "profix":
    os.system("clear")
else:
    os.system("cls")

l = int(input("hasta que tabla del 7 quieres llegar? "))

for x in range(1,l+1):
    print(7 ," x ", x ,"= ", x*7)
