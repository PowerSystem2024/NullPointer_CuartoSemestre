# Profundizamos en el TIPO FLOAT
# Representa un número decimal o de punto flotante, es decir, un número que puede tener una parte fraccionaria separada por un punto decimal.
#
a= 3.0105
print(f'{a:.4f}')  # Formateo a 4 decimales

# Contructor de tipo float----->pude recibir enteros de tipo string

a=float(10) # Le pasamos un tipo entero(int)
a= float('10')
print(f'a: {a:.2f}') 

# Notaciones exponencial (valores positivos o negativos)
#   VALORES +                     |->permiten simplicalos los números muy grandes o muy pequeños
a= 3e5
print(f'a:{a:.2f}')  # 3*10^5 = 300000.0 

#   VALORES NEGATIVOS
a= 3e-5
print(f'a:{a:.5f}')  # 3*10^-5 = 0.00003

# Cualquier calculo que  incluya un float, todo cambia a float  ! Ejemplo:
# toda variable o literqal que se utilice en una expresencion donde se involucre un tipo float, el resultado final de esta es una CONVERSION de tipo FLOAT 
a= 4.0 + 5
print(a)
print(type(a))