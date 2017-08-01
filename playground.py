# coding=utf-8

print("Hello world")

# ------
# LISTAS
# ------
fruits = ["Apple", "Orange", "Watermelon"]
print(fruits[0])
print(fruits[-1])

numbers = [0, 1, 2, 3, 4, 5, 6, 7 , 8, 9]

from_2_to_6 = numbers[2:7]
print(from_2_to_6)

greater_than_4 = numbers[5:]
print(greater_than_4)
print(numbers[::2])
print(numbers[1::2])

print( 4 in numbers )

# ------------
# DICCIONARIOS
# ------------
fighter = { "name": "Chuck", "last_name": "Norris", "technique": "Karate" }
# No usar esta forma de acceder. Si la clave no existe, exception
print["name"]
# Usar mejor esta forma
print fighter.get("name")
print fighter.get("nombre")
# None = Null

# ---------
# FUNCIONES
# ---------
def print_fruits(fruits_list):
    for fruit in fruits_list:
        print fruit

print_fruits(fruits)

# OJO A LAS TILDES en los String
# Se soluciona añadiendo en la primera línea del fichero la codificación a usar (ver más arriba)
print("Cagadísima")