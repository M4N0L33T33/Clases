import os

#limpieza
if os.name == "posix":
    os.system ("clear")
else:
    os.system ("cls")

#diccionario si/no 
diccionario = ['si', 'Si', 'yes', 'SI', 's', 'S', 'y', 'sis', 'so'],['no', 'No', 'NO', 'n0', 'N0', 'n', 'N', 'np', 'non']



#valores servicios
revision_km = 2
cambio_a = 1
revision_f = 0.5
revision_c = 0.5
revision_l = 0.2
revision_d = 0.5
lavado = 0.5

#datos

#info
print("""       Taller de Servicio Automotriz

Ingrese sus datos porfavor""")
Rut = input("Rut: ")
Nombre = input("Nombre Completo: ")
Marca = input("Marca Automovil: ")
Modelo = input("Modelo Automovil:")
print("""Servicios: 
1.- Revisión 1000Km
2.- Cambio Aceite
3.- Revisión Frenos
4.- Revisión Correas
5.- Revisión Luces
6.- Revisión Dirección
7.- Lavado de Auto (Gratis, 30min aprox.)""")

#respuestas
print("Coloque SI o NO dependiendo si es que quiere o no el servicio\n")
r1 = input("1.- ")
r2 = input("2.- ")
r3 = input("3.- ")
r4 = input("4.- ")
r5 = input("5.- ")
r6 = input("6.- ")
r7 = input("7.- ")

#contadores simples
tiempo = 0
cant_s = 0
if r1 in diccionario[0]:
    r1 = "Revisión 1000 Km, "
    cant_s = cant_s+1
    tiempo = tiempo + revision_km 
else:
    r1 = ""
if r2 in diccionario[0]:
    r2 = "Cambio Aceite, "
    cant_s = cant_s+1
    tiempo = tiempo + cambio_a
else:
    r2 = ""
if r3 in diccionario[0]:
    r3 = "Revisión Frenos, "
    cant_s = cant_s+1
    tiempo = tiempo + revision_f
else:
    r3 = ""
if r4 in diccionario[0]:
    r4 = "Revision Correas, "
    cant_s = cant_s+1
    tiempo = tiempo + revision_c
else:
    r4 = ""
if r5 in diccionario[0]:
    r5 = "Revisión Luces, "
    cant_s = cant_s+1
    tiempo = tiempo + revision_l
else:
    r5 = ""
if r6 in diccionario[0]:
    r6 = "Revisión Dirección, "
    cant_s = cant_s+1
    tiempo = tiempo + revision_d
else:
    r6 = ""
if r7 in diccionario[0]:
    r7 = "Lavado Auto."
    cant_s = cant_s+1
    tiempo = tiempo + lavado
else:
    r7 = ""

#limpieza
if os.name == "posix":
    os.system ("clear")
else:
    os.system ("cls")

#resultado
print("""--------------------------------------------------------
SERVICIO AUTOMOTRIZ
--------------------------------------------------------\n""")
print("Cliente: ", Nombre, Rut)
print("Servicios: ",r1,r2,r3,r4,r5,r6,r7) 
print("Cantidad: ", cant_s)
print("Tiempo: ", tiempo,"h.")
print("Estado: Trabajando")