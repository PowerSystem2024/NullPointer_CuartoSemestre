import math
from decimal import Decimal

# NaN (Not a Number) 
# |-> Es un valor de tipo float especial, que representa DATOS INDEFINIDOS, FALTANTES O NO REPRESENTABLES
# Sirve: Datos faltantes, cáculos inválidos, inicializar valores, limpieza de datos.

# Contructor Float -------------------------------------------------
a= float('nan') 
print(f'a: {a}')

# Módulo math---------------------------------------------------------
a= float('NaN')
print(f'Es de tipo NaN (Not a Number)? : {math.isnan(a)} ')

# Módulo Decimal -------------------------------------------------
a = Decimal('NaN') 
print(f'Es de tipo NaN (Not a Number)? : {math.isnan(a)} ')
