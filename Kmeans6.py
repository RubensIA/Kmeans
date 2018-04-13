# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 10:39:04 2018

@author: Rubens
"""

import numpy as np

lista = [[1,2],[2,4],[1,9],[10,32],[11,54],[12,89],[10,99]]
lista_aux = list(lista)
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
    
print('centroide inicial',centroide)

np.array(centroide)
dif1 = [centroide[0]]
dif2 = [centroide[1]]

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
        #print(a)
        minimo = min(a)
        pos = a.index(minimo)
        #print(minimo)
        #print(pos)
        if pos == 0:
            cluster1[1:1] = [z]
        elif pos == 1:
            cluster2[1:1] = [z]
    clusters = [cluster2,cluster2]
    return clusters


def err(centroide_anterior,centroide):
    
    distancias = []
    distancias.append(euclidian(centroide_anterior[0],centroide[0]))
   
    distancias.append(euclidian(centroide_anterior[1],centroide[1]))
    
    maxdist = max(distancias)
    
    return maxdist
    
    
    
        
    return erro


def subs(centroide):
  
    def summ(v):
        soma = sum(np.array(v))
        #print(soma)
        return soma

    
    for m in [cluster1]:
        n_elem = len(cluster1)
        somacluster1 = summ(m)
        #print(somacluster1)
   
    mediacluster1 = somacluster1/n_elem
    #print(mediacluster1)

    
    for n in [cluster2]:
        n_elem = len(cluster2)
        somacluster2 = summ(n)
        
        
    mediacluster2 = somacluster2/n_elem
    #print(mediacluster2)
    
    
    centroide = [mediacluster1,mediacluster2]
    group(centroide)
    #print('cluster1',cluster1)
    #print('cluster2',cluster2)
    
    return centroide

cluster1 = []
cluster2 = []

group(centroide)
#print('cluster1',cluster1)
#print('cluster2',cluster2)



epsilon = 1000
while epsilon >= 0.1:
    centroide_anterior = centroide[:]
    b+=1
    
    centroide = subs(centroide)
    
    #print('centroide anterior',centroide_anterior)
    #print('centroide novo',centroide)
    epsilon = err(centroide_anterior,centroide)
    print('erro entre centroides - epsilon',epsilon)
    
    

    
    
print('cluster1 resultante',cluster1)
print('cluster2 resultante',cluster2)



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







