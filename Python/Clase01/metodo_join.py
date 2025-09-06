


help(str.join)
# Hace: une cualquier cantidad de strings en uno solo, lo hace llamando al metodo separador entre cada 
# elemento del iterable (como una lista o tupla de strings). Resulatdao es un nuevo string.

tupla_str= ('Hola', 'alumnos','Tecnicatura','Universidad') # transforma una tupla en una osla cadena
mensaje= ' '.join(tupla_str)
print(f'Mensaje: {mensaje}') # se ve aqui 

lista_cursos= ['Java', 'Python','Angular','Spring']
mensaje= ', '.join(lista_cursos) # agrega un espacio y una coma a la lista en una sola cadena
print(f'Mensaje: {mensaje}') # se ve aqui 

cadena= 'HolaMundo'
mensaje= '.'.join(cadena) # le agrega un punto en cada letra
print(f'Mensaje: {mensaje}')

diccionario= {'nombre': 'JUAN', 'apellido': 'Orellana', 'edad': '18'}
llaves= '-'.join(diccionario.keys()) # va listar en una cadena solas las llaves
valores= '-'.join(diccionario.values()) # va listar en una sola cadena los valores , ambos con al concatenación del guion medio(en este caso)
print(f'Llaves: {llaves}, Type:{type(llaves)}')
print(f'Valores: {valores}, Type: {type(valores)}')