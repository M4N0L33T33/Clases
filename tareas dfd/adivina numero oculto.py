#caso
print("adivina el número oculto")
adiv = int(input("ingresa el número que creas que es: "))

if adiv == 3:
    print("atinastea la primera? felicidades!!")
else: 
    int(input("últimom intento: "))
    if adiv == 3:
        print("Felicidades")
    else:
        print("buen intento...")