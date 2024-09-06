print("Calculadora de dBm")

cableado = eval(input("ingresa la cantidad de cableado: "))
conectores = eval(input("ingresa la cantidad de conectores: "))
TX = eval(input("ingresa la cantidad de Tx: "))
RX = eval(input("ingresa la cantidad de Rx: "))

calculo = TX + RX - cableado - conectores

print("La totalidad de dBm restante es de: ",round(calculo,3))
