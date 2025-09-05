

# [ Contructor -Bool contiene los valores de True y Flase ](True se comporta como 1 y False como 0)

# Los Tipos Númericos -> es False para el 0 , True para los demas valores

valor = 0
resultado = bool(valor)
print(f'El valor: {valor}, Resultado: {resultado}')

valor = -0.1
resultado = bool(valor)
print(f'El valor: {valor}, Resultado: {resultado}')

# Tipo String -> False ''cadena vacia, True -> los demas valores


valor = ''
resultado = bool(valor)
print(f'El valor: {valor}, Resultado: {resultado}')


valor = 'Hola!'
resultado = bool(valor)
print(f'El valor: {valor}, Resultado: {resultado}')


# Tipo Coleccione-> False para colecciones vacias, True para todas las demas 
# Lista 
valor= []
resultado = bool(valor)
print(f'El valor de una lista vacia: {valor}, Resulatdo: {resultado}')

valor= [2,3,4]
resultado = bool(valor)
print(f'El valor de una lista conn elementos: {valor}, Resulatdo: {resultado}')

# Tupla -> False para tuplas vacias, True para todas las demas 
valor= ()
resultado = bool(valor)
print(f'El valor de una tupla vacia: {valor}, Resulatdo: {resultado}')

valor= (5,6,)
resultado = bool(valor)
print(f'El valor de una tupla con elementos: {valor}, Resulatdo: {resultado}')

#  Dieccionarios -> False para diccionarios vacios, True para todas las demas
valor= { }
resultado = bool(valor)
print(f'El valor de un diccionario vacio: {valor}, Resulatdo: {resultado}')

valor= {'Nombre':'JUAN','Apellido': 'Perez'}
resultado = bool(valor)
print(f'El valor de un diccionario con elementos: {valor}, Resulatdo: {resultado}')

# Sentencias de control con bool
if bool(1):
    print('Regresa Verdadero')
else:
    print('Regresa Falso')

# Ciclos
variable= 1
while variable:
    print('Regresa Verdadero')
    break
else:
    print('Regresa Falso')