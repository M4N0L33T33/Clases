
print("""esta es una calculadora de números pares o impares:
      1.- pares
      2.- impares
       """)
r_1 = int(input())

if r_1 == 1: #sumar pares
    r_2 = int(input("""ahora, tu número incial será par o impar?: 
              1.- par
              2.- impar
               """))
    if r_2 == 1:
        v1 = int(input("valor 1: "))
        v2 = int(input("valor 2: "))

        cont = 0
        while v1 <= v2:
            cont = cont + v1
            print(v1)
            v1 = v1 + 2
        print("tu suma de numeros pares es: ",cont)
    else:
        v1 = int(input("valor 1: "))
        v2 = int(input("valor 2: "))
        v1 = v1 + 1
        cont = 0
        while v1 <= v2:
            cont = cont + v1
            print(v1)
            v1 = v1 + 2
        print("tu suma de numeros pares es: ",cont)
if r_1 == 2:
    r_2 = int(input("""ahora, tu número incial será par o impar?: 
          1.- par
          2.- impar
               """))
    if r_2 == 1:  
        v1 = int(input("valor 1: "))
        v2 = int(input("valor 2: "))
        v1 = v1 + 1
        cont = 0
        while v1 <= v2:
            cont = cont + v1
            print(v1)
            v1 = v1 + 2
        print("tu suma de números impares es: ",cont)
    else:
        v1 = int(input("valor 1: "))
        v2 = int(input("valor 2: "))
        cont = 0
        while v1 <= v2:
            cont = cont + v1
            print(v1)
            v1 = v1 + 2
        print("tu suma de números impares es: ",cont)
    
   






