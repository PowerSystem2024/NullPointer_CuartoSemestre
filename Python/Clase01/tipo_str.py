import math
# Profundizamos  en el tipo String
#Concatenación automatica en Python
#    podemos ir concatenando cadenas de texto concatenandole variables o texto con el operador += 

variable= 'Adios'
mensaje= 'Hola ''Alumnos! ' + variable
mensaje+= ', Terminamos la clase'
#print(mensaje)

#--->Usamos la clase HELP para ayuda o documentación , (no se debe importar, porque ya viene incluida,--> built-in  )

# La clase STR, define como se crean, almacenan y manipulan las cadenas, es inmutable(una vez craeda no se puede modificar directamente)
# permite usar operadores como +(concatenación) y * (repetición)
help(str.capitalize)

# Usamos MATH para realizar operaciones matemátivcas comunes sin tener que escribir desde cero, como la raiz cuadrada, potencia,
# max. min, funciones.
help(math.isnan)