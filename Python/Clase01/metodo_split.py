
# El método split(significa: dividir)-------------
# Hace: -Devuelve una lista con las subcadenas del string, usando sep como separador.
#       - por !defaul divide por espacios en blanco, pero se puede especificar el separador
#       - se puede dividir todo lo que se puedaa

# help(str.split)

# separado por sin coma --hace que los espacios en blanco esten separados pro una coma
curso= 'Java JavaScript Node Python Diseno'
lista_curso= curso.split()
print(f'Lista de cursos: {lista_curso}')
print(type(lista_curso))

# separado por coma--hace que sino se encuentra un espacio en balnco se vuelva una sola lista/elemento
curso_separado_coma= 'Java,Python,Node,JavaScript,Spring'
lista_curso= curso_separado_coma.split(',',2) # ahora, poniendo la coma como separador identifica los elementos por separado y el segundo parametro(2)determina en cuantos espacios se va a separar  
print(f'Lista de cursos: {lista_curso}')
print(len(lista_curso))
