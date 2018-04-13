# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 10:39:04 2018

@author: Rubens
"""

import numpy as np

lista = [[1,2],[2,4],[1,9],[10,32],[11,54],[12,89],[10,99]]
lista_aux = list(lista) #[[1,2],[2,4],[1,9],[10,32],[11,54],[12,89]]

#Cria 3 centróides aleatórias
import random 
from random import randrange

centroide = []
semente = 12399

random.seed(semente)
for b in range(2):
    
    random_index = randrange(0,len(lista_aux))
    
    #print('O elemento sorteado foi:',sorteio)
    centroide[1:1] = [lista_aux[random_index]]

    del lista_aux[random_index]
    
print('centroide inicial', centroide)


#print(lista)

from math import sqrt
def euclidian(v1,v2):
    #Essa função recebe duas
    #   listas e retorna a
    #   distancia entre elas
    #Armazena o quadrado da distância
    dist = 0.0
    for x in range(len(v1)):
        dist += pow((v1[x] - v2[x]),2)
        
        
    #Tira a raiz quadrada da soma
    eucli = sqrt(dist)
    #print(eucli)
    return eucli




def group(j):
    # j recebe o centroide
    # group j retorna clusters para o centroide recebido
    del cluster1[:]
    del cluster2[:]
    for z in lista:
        a = []
        for w in j: 
            d = (euclidian(w,z))
            a[1:1] = [d]    
        print('distancias objeto aos centroides', a)
        minimo = min(a)
        pos = a.index(minimo)
        #print(minimo)
        #print(pos)
        if pos == 0:
            cluster1[1:1] = [z]
        elif pos == 1:
            cluster2[1:1] = [z]
    return z


def subs(b):
    b+=1
  
    def summ(v):
        soma1 = 0
        soma2 = 0 
        for h in v:
            for k in range(2):
                if k == 0:
                    soma1+=h[k]    
                elif k == 1:
                    soma2+=h[k]
        sum = [soma1,soma2]
        print('soma elementos cluster', sum)
        return sum

    
    for m in [cluster1]:
        n_elem = len(cluster1)
        somacluster1 = np.array(summ(m))
        #print(somacluster1)
   
    mediacluster1 = somacluster1/n_elem
    print(mediacluster1)

    
    for n in [cluster2]:
        n_elem = len(cluster2)
        somacluster2 = np.array(summ(n))
        
        #print(medd)
        
    mediacluster2 = somacluster2/n_elem
    print(mediacluster2)

    
    centroide = [mediacluster1,mediacluster2]
    print('centroide',centroide)
    group(centroide)
    print(cluster1)
    print(cluster2)
    return b

cluster1 = []
cluster2 = []

group(centroide)
print('cluster1',cluster1)
print('cluster2',cluster2)

b = 0
while b < 6:
    b = subs(b)
    #print(b)
    
    
print('cluster1 resultante', cluster1)
print('cluster2 resultante', cluster2)




import matplotlib.pyplot as plt




a = []
b = []
c = []
d = []

for pts in cluster1:
    a[1:1] = [pts[0]]
    b[1:1] = [pts[1]]

for pts in cluster2:
    c[1:1] = [pts[0]]
    d[1:1] = [pts[1]]

plt.xlim(0, 100)
plt.ylim(0,100)

plt.plot(a,b, 'go')
#plt.plot(a,b, 'k:', color='orange')

plt.plot(c,d, 'r^')
#plt.plot(c,d, 'k--', color='blue')




