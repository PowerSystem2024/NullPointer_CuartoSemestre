# Profundizamos en los Sistemas sde numeración 

# Sistema decimal(BASE 10)---------------------------------------------------------------
#       -Es el que usamos cotidianamente
#       -Usa los idgitos del 0 al 9 (0, 1, 2, 3, 4, 5, 6, 7, 8 y 9)
#       -Cada posición representa una potencia de 10
#       -Ejemplo: 345 = 3*10^2 + 4*10^1 + 5*10^0

a= 10
print(f'a: {a}')

#Sistema binario (BASE 2)------------------------------------------------------------------
#         -Es el lenguaje interno de las computadoras
#         -Usa los dígitos 0 y 1(apagado y encedido)
#         -Cada posición representa una potencia de 2
#         -Ejemplo: 1010 = 1*2^3 + 0*2^2 + 1*2^1 + 0*2^0 = 8 + 0 + 2 + 0 = 10
#         ->El prefijo 0b indica que el número está en formato binario

a = 0b1010  
print(f'a: {a}')

# Sistema octal (BASE 8)------------------------------------------------------------------
#        -Usa los dígitos del 0 al 7 (0, 1, 2, 3, 4, 5, 6 y 7)
#        -Cada posición representa una potencia de 8
#        -Muy usado en sistemas antiguos y para agrupar de 3 bits en 3
#        -Ejemplo: 12 = 1*8^1 + 2*8^0 = 8 + 2 
#        ->El prefijo 0o indica que el número está en formato octal= 10

a = 0o12  # El 12 en octal es igual a 10 en decimal
print(f'a: {a}')

# Sistema hexadecimal(BASE 16)------------------------------------------------------------
#        -Usa los dígitos del 0 al 9 y las letras A, B, C, D, E y F (que representan los valores de 10 a 15)
#        -Cada posición representa una potencia de 16
#        -Cada dígito representa 4 bits
#        -Muy usado en programación y para representar colores, direcciones de memoria, y datos binario de forma compacta
#        -Ejemplo: 0xA = 10*16^0 = 10
#        ->El prefijo 0x indica que el número está en formato hexadecimal

a= 0xA  # El A en hexadecimal es igual a 10 en decimal
print(f'a hexadecinal: {a}')

#Base Decimal
a=int('23',10) # Convertir de cadena en base 10 a entero decimal
print(f'a= base decimal:{a}')

# Base Binaria
a=int('10111',2) # Convertir de cadena en base 2 a entero decimal
print(f'a= base binaria:{a}')

# Base Octal
a= int('27',8) # Convertir de cadena en base 8 a entero decimal
print(f'a= base octal:{a}')

# Base Hexadecimal
a= int('17',16) # Convertir de cadena en base 16 a entero decimal
print(f'a= base hexadecimal:{a}')

# Base 5 susu valores son 0,1,2,3,4
a = int('344',5) # Convertir de cadena en base 5 a entero decimal
print(f'a= base 5:{a}')