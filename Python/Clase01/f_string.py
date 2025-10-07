# Ejemplo de f-string en Python (la interpolacion) 
# se usa para mostrar variables en mensajes, mostrar mejor legilibilidad y evitar concatenaciones con + 

nombre = 'Pepe'
edad = 28
sueldo = 3000
mensaje = f'Nombre {nombre} Edad {edad} Sueldo {sueldo:.2f}'
print(mensaje)

# metodo print para dar formato en la salida

print(nombre, edad, sueldo, sep= ' , ')