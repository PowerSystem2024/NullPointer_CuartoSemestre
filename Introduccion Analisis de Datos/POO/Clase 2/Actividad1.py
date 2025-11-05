# 1. Definir la clase Auto
class Auto:
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color
    
    def mostrar_info(self):
        return f"Marca: {self.marca}, Color: {self.color}"

# 2. Crear dos objetos (instancias) de la clase Auto
auto1 = Auto("Ford", "rojo")
auto2 = Auto("Toyota", "azul")

# 3. Mostrar en pantalla el color y marca de cada auto
print("=== INFORMACIÓN DE LOS AUTOS ===")
print("Auto 1:", auto1.mostrar_info())
print("Auto 2:", auto2.mostrar_info())

# También se puede acceder directamente a los atributos
print("\n=== ACCESO DIRECTO A ATRIBUTOS ===")
print(f"Auto 1 - Marca: {auto1.marca}, Color: {auto1.color}")
print(f"Auto 2 - Marca: {auto2.marca}, Color: {auto2.color}")

# 4. Explicación sobre qué es una instancia
print("\n=== EXPLICACIÓN ===")
print("""
¿Qué es una instancia?

Una instancia es un objeto concreto creado a partir de una clase.
- La clase 'Auto' es como un molde o plantilla
- Las instancias 'auto1' y 'auto2' son objetos reales creados desde ese molde
- Cada instancia tiene sus propios valores para los atributos (marca y color)
""")