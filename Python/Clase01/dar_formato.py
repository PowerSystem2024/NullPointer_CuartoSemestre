# dar formato un string---------------------------------------------
#-------- (%s -> string, %d -> entero, %f -> float)-----------------

# Parametro posicional de tipo string
nombre= 'Ariel'
edad= 28
mensaje_con_formato= 'Mi nombre es %s y tengo %d años ' % (nombre, edad ) # aqui esta dandole el formato 

# Creamos un tupla
persona= ('Carla', ' Gomez', 5000.00) 
mensaje_con_formato = 'Hola %s %s, Tu sueldo es %.2f' # % persona # aqui le pasamos el objeto que es tupla  
#print(mensaje_con_formato % persona) # le podemos poner en el print o en la variable

# Metodo format()---------------------------------------------------
# Se usa pra insertar valores dentro de cadenas de texto de forma dinamica y ordenada 

nombre = 'Juan'
edad = 30
sueldo = 7500
# mensaje_con_formato = 'Nombre {}, Edad {} y Sueldo {:.2f}'.format(nombre, edad, sueldo) # aqui le pasamos los parametros
# print(mensaje_con_formato)

# PLACE HOLDER: Es un marcador de posición dentro de una cadena, representado por {}. Indica dónde se debe insertar un valor usando format(). 
# Se puede controlar el orden usando indices dentro de los corchetes {}.

# mensaje = 'Nombre {0}, Edad {1} Sueldo {2:.2f}'.format(nombre, edad, sueldo)  
# print(mensaje)

# mensaje = 'Nombre {n} Edad {e} Sueldo {s:.2f}'.format(n= nombre, e=edad, s=sueldo)
# print(mensaje)

# ejempllo dicicionario de terminos 
dicionario = {'nombre': 'Ana', 'edad': 25, 'sueldo': 8000.00}
mensaje = 'Nombre {dic[nombre]} Edad {dic[edad]} Sueldo {dic[sueldo]:.2f}' .format(dic=dicionario) # aqui le pasamos el diccionario
print(mensaje) # con el dic accedemos al valor de las variables del dicionario