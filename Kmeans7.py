# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 16:49:22 2018

@author: Rubens
"""
"algoritmo para clusterização em 3 clusters"

import xlrd
import numpy as np

data = [[1,2,5,8],[2,4,7,3],[1,9,89,76],[10,32,87,56],[11,54,89,34],[12,89,90,27],[10,99,67,45]]
data_aux = list(data)
#Cria 3 centróides aleatórias

data_aux = list(data)
#Cria 3 centróides aleatórias
import random 
from random import randrange

centroide = []
semente = 13773

random.seed(semente)
for b in range(3):
    
    random_index = randrange(0,len(data_aux))
    
    #print('O elemento sorteado foi:',sorteio)
    centroide[1:1] = [data_aux[random_index]]

    del data_aux[random_index]
    
print('centroide inicial',centroide)

np.array(centroide)

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
    del cluster3[:]
    for z in data:
        a = []
        for w in j: 
            d = (euclidian(w,z))
            a.append(d)    
        #print(z , a)
        minimo = min(a)
        pos = a.index(minimo)
        #print(minimo)
        #print(pos)
        if pos == 0:
            cluster1[1:1] = [z]
        elif pos == 1:
            cluster2[1:1] = [z]
        elif pos == 2:
            cluster3[1:1] = [z]
    clusters = [cluster1,cluster2,cluster3]
    return clusters


def err(centroide_anterior,centroide):
    
    for i in range(3):
        distancias = []
        distancias.append(euclidian(centroide_anterior[i],centroide[i]))
            
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
    #print('mediacluster1',mediacluster1)

    
    for n in [cluster2]:
        n_elem = len(cluster2)
        somacluster2 = summ(n)
        
        
    mediacluster2 = somacluster2/n_elem
    #print('mediacluster2',mediacluster2)
    
    
    for n in [cluster3]:
        n_elem = len(cluster3)
        somacluster3 = summ(n)
        
        
    mediacluster3 = somacluster3/n_elem
    #print('mediacluster3',mediacluster3)
    
    
    centroide = [mediacluster1,mediacluster2,mediacluster3]
    group(centroide)
    print('cluster1',cluster1)
    print('cluster2',cluster2)
    print('cluster3',cluster3)
    
    return centroide

cluster1 = []
cluster2 = []
cluster3 = []

group(centroide)
print('cluster1',cluster1)
print('cluster2',cluster2)
print('cluster3',cluster3)




b = 0
while b < 6:
    b+=1
    centroide_anterior = centroide[:]
    
    centroide = subs(centroide)
    
    
    
    #print('centroide anterior',centroide_anterior)
    #print('centroide novo',centroide)
    #epsilon = err(centroide_anterior,centroide)
    #print('epsilon',epsilon)
    
    

    
    
print('cluster1 resultante',cluster1)
print('cluster2 resultante',cluster2)
print('cluster3 resultante',cluster3)



