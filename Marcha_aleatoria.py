import numpy as np
import matplotlib.pyplot as plt
import random

"""
Problema: Una partıcula sigue una marcha aleatoria sobre el eje x. A cada paso de tiempo τ 
puede dar un salto de longitud a a la derecha o la izquierda con igual probabilidad.
En el instante inicial t = 0 está en x = 0.

Este ejercicio describe una tipica distribución binomial, ya que la particula puede caminar hacia
la izquierda o hacia la derecha, es un sí o no. Despues de que la particula ha dado N pasos, n hacia
la dereche y N-n hacia la izquierda, se calcula la posición en donde termina la particula respecto a la
posicion inicial.

Antes de empezar con el cogido es importante responder las siguientes preguntas:

1. ¿Cuál es la probabilidad P(n, N) para que en N pasos la partícula haya efectuado n pasos
a la derecha y N − n pasos a la izquierda?
    
    rta: Como este ejercicio obedece el comportamiento de una distribución binomial,
        P(n,N)=N!/(n!(N-n)!)*(P(paso a la derecha)**n)*(P(paso a la izquierda)**N-n)
        P(n,N)= N!/(n!(N-n)!) *(0.5**N)    

2. ¿Cuál es la posición x después de N pasos en función de n, N y a?

    rta: x=a(n-(N-n))
         x=a(2n-N), considerando los pasos hacia la derecha como positivos y los pasos hacia la
         izquierda como negativos.

3. ¿Cuál es el número de pasos promedio de pasos hacia la derecha y el promedio de la posicion final?
    
    rta: Aplicando un poco las definiciones de fisica estadistica se obiente lo siguiente:
        <n>=n*P(paso a la derecha)
        <n>=(0.5)*N
        Evaluando este resultado en el punto 2 se encuentra la posición promedio, asi:
        <x>=a(2<n>-N)
        <x>=0

4. ¿Cuál es la varianza?
    
    rta: var(n)=N(0.5**2)
         var(x)=a((N)^(1/2)-N)
"""





"""
Declaración de parametros. Asi se definira que tan grande será la muestra
de pasos a considerar en la distribución binomial y el punto de partida x
para un tiempo t=0.
"""
N=100 #número de pasos
t=N
x=0 #posición inicial
a=1 #Longitud de los pasos
iteraciones=10000 #Cantidad de veces que obtendré una posición final

def generar_posiciones(N,t,x,a,iteraciones):
    """
    Se generan los pasos aleatorios en donde cero equivale a izquierda y 1
    equivale a derecha.
    """
    posicion_final=[] #Lista que contendra todas las posiciones finales obtenidas
    
    for j in range(0,iteraciones):
        pasos=[]
        
        for i in range(0,t):
            paso=random.randint(0,1)
            pasos.append(paso)
        
        """
        Ahora se calcula la posicion en el eje x de la particula sumado los pasos
        hacia la derecha como positivos y los pasos hacia la izquierda como 
        negativos. expresamos a x en terminos de N el numero total de pasos y los
        pasos hacia la derecha, como en el taller.
        """
        x=a*(2*pasos.count(1)-N)
        posicion_final.append(x)
    return posicion_final

def graficar_distribucion(posicion_final):
    """
    Ahora graficamos el histograma con las frecuencias de las posiciones finales
    """
    intervalos= range(min(posicion_final), max(posicion_final)+2) #calculamos los extremos de los intervalos
    
    plt.hist(x=posicion_final, bins=intervalos, density=True, color='#F2AB6D', rwidth=0.85)
    plt.title('Histograma de posiciones')
    plt.xlabel('posicion')
    plt.ylabel('Frecuencia')
    plt.xticks(intervalos)
    
    plt.show()

"""
Para demostrar computacionalmente el teorema central limite se realizaran 
100000 iteraciones para demostrar que la distribucion de la suma de variables
aleatorias tiende a una distribucion normal:

"""
iteraciones=100000
posicion_final=generar_posiciones(N,t,x,a,iteraciones)
graficar_distribucion(posicion_final)


"""
Se puede apreciar, alterando las iteraciones de la siguiente manera:
10,100,1000,10000,..., que a medida en que estas iteraciones o varibales
aleatorias tiende a infinito su suma tiene como distribución de probabilidad
una distribución normal, tal como lo predice el teorema central limite
""" 

"""
Para el inciso 8 se correra el programa para varios valores de N, definidos 
en la siguiente lista, y con menos iteraciones, ya que no contamos con mucho
poder computacional:
"""

N=[5,10,15,20,25,50,100, 1000]
iteraciones=10000
r_media=[] #Contiene en el mismo orden que la lista N los valores de la posicion media
r_2_media=[] #Contiene en el mismo orden que la lista N los valores de la varianza media

for m in N: #Este primer for calula las posiciones y las <x> medias de las posiciones finales por cada N
    posicion_final=generar_posiciones(m,m,x,a,iteraciones)
    x_media=np.mean(posicion_final)
    r_media.append(x_media)

    x_2=[]
    for k in posicion_final: #Este segundo for calcula x^2
        x_2.append(k**2)
    x_2_media=np.mean(x_2) #Aqui se calcula la me dia <x^2>
    r_2_media.append(x_2_media-((x_media)**2)) #Aqui se calcula la varianza

print("lista de valores N: ")
print(N)
print("lista de <x> por cada valor N: ")
print(r_media)
print("lista de varianzas por cada valor N: ")
print(r_2_media)
    
"""
El valor esperado para la posicion x converge a cero, ya que la probabilidad
de obtener un paso a la derecha es la misma que la de obtener un paso hacia la
izquierda en cada instante de tiempo.
Por otro lado, los valores de <x^2>, la varianza de x, es proporcional al numero
de pasos N. Finalmente, de solucionar la ecuacion de difusion encontramos que la cosntante
D de difusion se puede hayar asi: D=<x^2>/(2N), entonces para cada valor de N la conste de
difusion es:
"""
D=[] #contiene en el mismo orden que la lista N, sus constantes de difusion.

for g in range(len(N)):
    d=r_2_media[g]/(2*N[g])
    D.append(d)

print("lista de valores cte de difusion D: ")
print(D)
    