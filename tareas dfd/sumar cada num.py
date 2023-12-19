print("sumaremos cada uno de los numeros que coloques en el rango designado")

v1 = int(input("valor 1: "))
v2 = int(input("valor 2: "))

llave = 1
#de aqui
cont = 0
while v1 <= v2:
    cont = cont + v1
    print(v1)
    v1 = v1 + 1
print(cont)
#hasta aqui es como se hace un contador en python

