import math
from decimal import Decimal

# Manejo de valores infinitos----------------------------------------------------------------------------------------------
infinito_positivo = float('inf') #[cadena para inf+  ]    para esto necesita un tipo numero para definir si es un infinito
print(f'infinito_positivo: {infinito_positivo}') # --definimos el valor de infinito +
print(f'Es un infinito positivo?: {math.isinf(infinito_positivo)}') #-- Verifica si es infinito

infinito_negativo = float('-inf')  #[cadena -inf]      --definimos el valor de infinito -
print(f'Infinito negativo: {infinito_negativo}')
print(f'Esun infinito negativo?: {math.isinf(infinito_negativo)}') #-- Verifica si es infinito

# Módulo math<-------------------------(otra manera de definir valores infinitos)---------------------------------
#           Ideal para: funciones matemáticas avanzadas, algotitmos y cáculos rápidos
#           Proporciona una amplia gama de funciones matemáticas y constantes, incluyendo la representación de valores infinitos.
infinito_negativo = math.inf
print(f'-infinito_positivo: {infinito_positivo}')
print(f'Es un infinito positivo?: {math.isinf(infinito_positivo)}')

infinito_negativo = -math.inf
print(f'-infinito_negativo: {infinito_negativo}')
print(f'Es un infinito negativo?: {math.isinf(infinito_negativo)}')

# Módulo Decimal<-------------------------(otra manera de definir valores infinitos)---------------------------------
#             Ideal para: finanzas, cálculos exactos
#             Permite mayor precisión y control sobre la representación de números decimales en comparación con el tipo float.
infinito_positivo = Decimal('Infinity')
print(f'infinito_positivo: {infinito_positivo}')
print(f'Es infinito?: {math.isinf(infinito_positivo)}')

infinito_negativo = Decimal('-Infinity')
print(f'infinito_negativo: {infinito_negativo}')
print(f'Es infinito?: {math.isinf(infinito_negativo)}')