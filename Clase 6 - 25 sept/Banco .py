import os
os.system("clear")

nombre = input("ingrese su nombre y apellido: ")
rut = input("ingrese su rut porfavor: ")
print("")
            
print(""" LOS PRE-REQUISITOS PARA PEDIR UN PRESTAMO SON:
1.- El monto mínimo del crédito es de $500.000.
2.- El plazo de cuotas es desde 3 a 84 cuotas.
3.- Cumplir con rangos de edad entre 24 y 79 años.
4.- Presentar nacionalidad chilena.
5.- El sueldo mínimo debe ser de $300.000.
6.- Presentar antigüedad laboral. Mínimo 3 años.
7.- No presentar morosidades.      
''Al ingresar los valores, recuerde ingresar los valores como son y tal cual se leen, respetando mayúsculas y minúsculas''
 """)
    
edad = int(input("ingrese su edad: "))
if edad >= 24 and edad <= 79:
    r_2 = 1
else:
    r_2 = 0
print("")

nacionalidad = input(
"""Ud tiene la nacionadad chilena?: 
1.- Si                       
2.- No

""")
print("")

sueldo = int(input("ingrese su sueldo: "))
print("")

tiempo = int(input("cuantos años tiene trabajando: "))
print("")

morosidad = input(
"""¿Presenta morosidad?
1.- Si
2.- No
""")
print("")

if nacionalidad == "Si" and sueldo >= 300000 and tiempo >= 3 and r_2 == 1 and morosidad == "No":
    
    print("Cumple los requisitos básicos, ingrese el monto del credito a pedir y las cuotas:" )
    print("Sueldo: ", sueldo)
    print("Monto máximo para retirar: ",sueldo*10)
    print("La tasa de interes es de 1.46% mensual")
    
    monto = int(input("ingrese monto del crédito: "))
    if monto > sueldo*10 or monto < 500000:
        print("""ingresa nuevamente un monto porfavor: 
              """)
        monto = int(input())
    print("")

    cuotas = int(input("ingrese el número de cuotas(3 a 84): "))
    if cuotas < 3 or cuotas > 84:
        cuotas = int(input("""ingresa nuevamente un número de cuotas: 
                  """))
    total = monto*(1.0146 ** cuotas)
    print("total a pagar $",round(total))

    os.system("clear")
    
    print("--------------------------------------------------------")
    print("  " + nombre + " " + rut + "  ")
    print("--------------------------------------------------------") 
    print("Cumple con los requisitos")
    print("Sueldo: $", sueldo)
    print("Monto Máximo: ", sueldo*10)
    print("Monto Solicitado: $", monto)
    print("Tasa Mensual: 1,46%")
    print("Cuotas: ", cuotas)
    print("Monto a Pagar: $", round(total))
    print("Su monto ya fue depositado en su cuenta rut")
    print("el próximo mes procede a ser el primer pago de las cuotas, cuyo monto es de: $", round(total/cuotas))
    print("--------------------------------------------------------")
    
else:
    print("--------------------------------------------------------")
    print("  " + nombre + " " + rut + "  ")                    
    print("--------------------------------------------------------") 
    print("No cumple con los requisitos")

print("")
print("Hasta luego")