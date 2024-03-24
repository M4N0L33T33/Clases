b=[]
# al usar range(6) la variable "i" asume valores
# enteros desde 0 hasta 5
for i in range (6):
n=i+10
b.append(5*0.92**n)
print (f'b({n})={b[i]}')