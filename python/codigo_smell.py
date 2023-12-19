import math 
from colorama import Fore, Back, init
init()

Vacio = 1.000
Aire = 1.0003
Agua = 1.33
Vidrio = 1.6
Diamante = 2.417
Alcohol = 1.36

print(Fore.YELLOW)
print(Back.BLACK)
print("""
medio 1:
Vacio: 1.000
Aire: 1.0003
Agua: 1.33
Vidrio: 1.6
Diamante: 2.417
Alcohol: 1.36 
please put your word of the value
""")
print(Fore.CYAN)
count = 0

try:
    medio = float(input("ingrese medio 1: "))
except ValueError:
    count = 1+count
try:
    angulo = float(input("ingrese angulo 1: "))
except ValueError:
    count = 2+count
try:
    medio_2 = float(input("ingrese medio 2: "))
except ValueError:
    count = 3+count

try:
    angulo_2 = float(input("ingrese angulo 2: "))
except ValueError:
    count = 4+count

# radianes_1 = (angulo * math.pi)/180
# sin_first = math.sin(radianes_1)
# first = medio * sin_first

# second = first/medio_2

# result = math.degrees(second)

print(Fore.YELLOW)

if count==1:
    # Convertir los ángulos de grados a radianes
    angulo = math.radians(angulo)
    angulo_2 = math.radians(angulo_2)

    # Calcular el índice de refracción del primer medio usando la fórmula de Snell
    medio = medio_2 * math.sin(angulo_2) / math.sin(angulo)

    # Imprimir el resultado
    print(medio)
elif count==2:
    # Convertir los ángulos de grados a radianes
    angulo = math.radians(angulo)
    angulo_2 = math.radians(angulo_2)

    # Calcular el índice de refracción del primer medio usando la fórmula de Snell
    medio_2 = medio * math.sin(angulo_2) / math.sin(angulo)

    # Imprimir el resultado
    print(medio_2)
elif count==3:
    # Convertir el ángulo de incidencia de grados a radianes
    angulo_2 = math.radians(angulo_2)

    # Calcular el ángulo de refracción usando la fórmula de Snell
    angulo = math.asin((medio / medio_2) * math.sin(angulo_2))

    # Convertir el ángulo de refracción de radianes a grados
    angulo = math.degrees(angulo)

    print(angulo)

elif count==4:
    # Convertir el ángulo de incidencia de grados a radianes
    angulo = math.radians(angulo)

    # Calcular el ángulo de refracción usando la fórmula de Snell
    angulo_2 = math.asin((medio / medio_2) * math.sin(angulo))

    # Convertir el ángulo de refracción de radianes a grados
    angulo_2 = math.degrees(angulo_2)

    print(angulo_2)
else:
    print("tienes mas de una incognita")

input()




# print(radianes_1)
# print(sin_first)
# print(first)
# print(second)
# print(result)




