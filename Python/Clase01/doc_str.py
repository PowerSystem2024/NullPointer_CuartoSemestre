from mi_clase import MiClase


# help(MiClase)

#print(MiClase.__doc__) # aqui solo se ve la documentaciónb de la clase de MiClase.
# ! recordar que NO hace falta los parentesis , porque no estamos llamado al método sino queremos ver la documentación de los objetos creados
#print(MiClase.__init__.__doc__)  # aqui puedo ver una documentación especifica ej: documentación del dunder init

#print(MiClase.mi_metodo.__doc__)

print(MiClase.mi_metodo) # 
print(type(MiClase.mi_metodo)) # con esto podemos ver que tipo es mi_metodo