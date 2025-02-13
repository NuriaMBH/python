print("ejemplo de librerías")
# Importamos funciones específicas de math
#sintaxis con FROM
from math import floor, ceil, trunc
# Definimos variables
numero1= 20
numero2 = 3
division= numero1/numero2
print("la division es", division)
#DECLARAMOS VARIABLES PARA ALMACENAR LOS VALORES DE LAS OPERACIONES

# Almacenamos los valores de las operaciones
varfloor= floor(division)
varceil= ceil(division)
vartrunc = trunc (division)
# Mostramos los resultados
print("floor", varfloor)
print ("ceil", varceil)
print ("trunc", vartrunc)
print("fin de programa")
# 1. floor(x) → Redondeo hacia abajo
# La función floor(x) devuelve el entero más cercano por debajo del número dado.

from math import floor

print(floor(4.9))  # Devuelve 4
print(floor(-3.7)) # Devuelve -4 (porque es el entero menor más cercano por debajo del número dado.

#2. ceil(x) → Redondeo hacia arriba
#La función ceil(x) devuelve el entero más cercano por encima del número dado.
from math import ceil

print(ceil(4.1))   # Devuelve 5
print(ceil(-3.7))  # Devuelve -3 (el entero mayor más cercano)

#3. trunc(x) → Elimina la parte decimal (truncamiento)
#La función trunc(x) simplemente elimina la parte decimal, sin importar si el número es positivo o negativo.

from math import trunc

print(trunc(4.9))   # Devuelve 4
print(trunc(-3.7))  # Devuelve -3

#Diferencia con floor() y ceil()

# trunc(x) simplemente corta la parte decimal sin redondear.
# floor(x) y ceil(x) sí redondean dependiendo de si el valor es positivo o negativo.