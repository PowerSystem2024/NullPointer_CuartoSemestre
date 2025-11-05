# ACTIVIDAD 1: ANÁLISIS EXPLORATORIO DE DATOS

print("=== ANÁLISIS EXPLORATORIO DE DATOS - GRUPO DE ESTUDIANTES ===\n")

# 1. DEFINIR LOS DATOS
estudiantes = [
    {"nombre": "Ana", "edad": 20, "nota": 8, "carrera": "Sistemas"},
    {"nombre": "Juan", "edad": 22, "nota": 6, "carrera": "Diseño"},
    {"nombre": "Carla", "edad": 21, "nota": 9, "carrera": "Sistemas"},
    {"nombre": "Pedro", "edad": 23, "nota": 5, "carrera": "Marketing"},
    {"nombre": "Sofía", "edad": 20, "nota": 7, "carrera": "Sistemas"}
]

# Mostrar la tabla original
print("TABLA DE ESTUDIANTES:")
print("Nombre | Edad | Nota | Carrera")
print("-" * 35)
for estudiante in estudiantes:
    print(f"{estudiante['nombre']:6} | {estudiante['edad']:4} | {estudiante['nota']:4} | {estudiante['carrera']}")
print()

# 2. IDENTIFICAR TIPOS DE VARIABLES
print("1. TIPOS DE VARIABLES:")
print("   - Variables categóricas: Nombre, Carrera")
print("   - Variables numéricas: Edad, Nota")
print()

# 3. CALCULAR PROMEDIO DE NOTAS
notas = [estudiante["nota"] for estudiante in estudiantes]
promedio_notas = sum(notas) / len(notas)
print("2. PROMEDIO DE NOTAS:")
print(f"   Notas: {notas}")
print(f"   Promedio: {promedio_notas}")
print()

# 4. CONTAR ESTUDIANTES EN SISTEMAS
carreras = [estudiante["carrera"] for estudiante in estudiantes]
cantidad_sistemas = carreras.count("Sistemas")
print("3. ESTUDIANTES EN SISTEMAS:")
print(f"   Carreras: {carreras}")
print(f"   Cantidad en Sistemas: {cantidad_sistemas}")
print()

# 5. ENCONTRAR ESTUDIANTE CON MAYOR NOTA
estudiante_max_nota = max(estudiantes, key=lambda x: x["nota"])
print("4. ESTUDIANTE CON MAYOR NOTA:")
print(f"   {estudiante_max_nota['nombre']} - Nota: {estudiante_max_nota['nota']} - Carrera: {estudiante_max_nota['carrera']}")
print()

# 6. ANÁLISIS ADICIONAL (EXTRA)
print("=== ANÁLISIS ADICIONAL ===")

# Promedio de edad
edades = [estudiante["edad"] for estudiante in estudiantes]
promedio_edad = sum(edades) / len(edades)
print(f"Promedio de edad: {promedio_edad:.1f} años")

# Distribución por carrera
from collections import Counter
distribucion_carreras = Counter(carreras)
print("Distribución por carrera:")
for carrera, cantidad in distribucion_carreras.items():
    print(f"   - {carrera}: {cantidad} estudiante(s)")

# Rango de notas
nota_minima = min(notas)
nota_maxima = max(notas)
print(f"Rango de notas: {nota_minima} - {nota_maxima}")

print("\n=== ANÁLISIS COMPLETADO ===")