import os

#ingreso de datos
print("esta es una calculadora básica, donde se muestran los resultados de suma, resta, multiplicación y división")

n1 = int(input("ingresa el primer valor: "))
n2 = int(input("ingresa el segundo valor: "))

os.system("clear")

#variables
suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
div = n1 / n2

#operaciones
print("Resultado de la suma: ",suma)
print("Resultado de la resta: ",resta)
print("Resultado de la multiplicación: ",multi)
print("Resultado de la división: ",div)
input()
