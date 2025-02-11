print("rango de numeros pares")
print("introduzca un inicio")
inicio= int(input())
print("Introduzca un valor final")
fin=int(input())
#REALIZAMOS UN BUCLE DESDE UN INICIO HASTA UN FINAL +1)
for i in range(inicio, fin+1):
    #preguntamos si el numero es par
    if(i%2==0):
        print(i)
print ("Fin del programa")