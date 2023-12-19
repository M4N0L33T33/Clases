import os
os.system("pip install colorama")
if os.name == "posix":
    os.system ("clear")
else:
    os.system ("cls")

# Crear un diccionario de palabras mal escritas y sus correcciones
diccionario = ['si', 'Si', 'yes', 'SI', 's', 'S', 'y'],['no', 'No', 'NO', 'n0', 'N0', 'n', 'N']

#variable de los ciclos
si_no = 1
si_no2 = 1

#datos de entrada
nombre = input("ingrese su nombre y apellido: ")
rut = input("ingrese su rut porfavor: ")
print("")

#requerimiento    
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

#pool de datos de entrada
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

if nacionalidad in diccionario[0]:
    nacionalidad = 'Si'
else:
    nacionalidad='No'
if morosidad in diccionario[1]:
    morosidad = 'No'
else:
    morosidad ='Si'

#limpieza
if os.name == "posix":
    os.system ("clear")
else:
    os.system ("cls")


#comprobación de datos
if nacionalidad == "Si" and sueldo >= 300000 and tiempo >= 3 and r_2 == 1 and morosidad == "No":
    
    print("Ud cumple los requisitos básicos, ingrese el monto y las cuotas:" )
    print("")
    print("Sueldo: $", sueldo)
    print("Monto máximo para retirar: $",sueldo*10)
    print("La tasa de interes es de 1.46% mensual")
    
    #ciclo crédito    
    while si_no == 1:

        monto = int(input("ingrese monto del crédito: "))

        while monto > sueldo*10 or monto < 500000:
            monto = int(input("""ingresa nuevamente un monto porfavor: 
                """))           
        print("")
        #opciones normales
        print("Opciones más comunes de cuotas (puedes escojer las cuotas que quieras) \n")
        print("3 Cuotas: $",round(monto*(1.0146 ** 3))," --------- 6 Cuotas: $",round(monto*(1.0146 ** 6)))
        print("")
        print("12 Cuotas: $",round(monto*(1.0146 ** 12))," --------- 24 Cuotas: $",round(monto*(1.0146 ** 24)))
        print("")
        print("36 Cuotas: $",round(monto*(1.0146 ** 36))," --------- 48 Cuotas: $",round(monto*(1.0146 ** 48)))
        print("")
        print("60 Cuotas: $",round(monto*(1.0146 ** 60))," --------- 72 Cuotas: $",round(monto*(1.0146 ** 72)))
        print("")
        print("84 Cuotas: $",round(monto*(1.0146 ** 84)),"\n")
        print("")

        si_no = input("""Estas seguro de querer ese monto?
        1.- si
        2.- no 
        
        """)

        if si_no == "si":
            si_no = 0
        else:
            si_no = 1
        
    print("")

    #ciclo cuotas
    while si_no2 == 1:

        cuotas = int(input("Ingrese el número de cuotas(3 a 84): "))
        total = monto*(1.0146 ** cuotas)

        while cuotas < 3 or cuotas > 84:
            cuotas = int(input("""ingresa nuevamente un número de cuotas: 
                  """))
        
        print("Tu valor total es de $",round(total))
        print("Tu valor por cuota será de: $",round(total/cuotas))
        print("Quieres tener ese valor cuota?")
        print("1.- si")
        print("2.- no")

        si_no2 = input()

        if si_no2 == "si":
            si_no2 = 0
        else:
            si_no2 = 1
            if os.name == "posix":
                os.system ("clear")
            else:
                os.system ("cls")

   
    print("total a pagar $",round(total))

    #limpieza
    if os.name == "posix":
        os.system ("clear")
    else:
        os.system ("cls")

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
    print("Valor cuota será de: $",round(total/cuotas))
    print("--------------------------------------------------------")
    
else:
    print("--------------------------------------------------------")
    print("  " + nombre + " " + rut + "  ")                    
    print("--------------------------------------------------------") 
    print("No cumple con los requisitos")

input("Presiona 'Enter' pata terminar.")


