# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 13:29:29 2018

@author: Rubens
"""
import numpy as np

" Esse algoritmo apresenta erros na escolha aleatória dos centróides repetidos"


from math import sqrt
def euclidian(v1,v2):
    """
    Essa função recebe duas
       listas e retorna a
       distancia entre elas
    """
    #Armazena o quadrado da distância
    dist = 0.0
    for x in range(len(v1)):
        dist += pow((v1[x] - v2[x]),2)
        
        
    #Tira a raiz quadrada da soma
    eucli = sqrt(dist)
    #print(eucli)
    return eucli


#Cria 3 centróides aleatórias
import random

lista = [[1,2],[3,4],[6,9],[11,32],[13,54],[76,89]]

for b in range(3):
    random.seed(3)
    sorteio = random.choice(lista)
    #print('O elemento sorteado foi:',sorteio)
    if b == 0: b1 = sorteio
    elif b == 1: 
        b2 = sorteio
    elif b == 2: 
        b3 = sorteio


y = [b1,b2,b3]


bestmatchb1 = [b1]
bestmatchb2 = [b2]
bestmatchb3 = [b3]



print('centroide', y)



for z in lista: 
    b = 0
    for w in y:    
        d = (euclidian(w,z))
        b+=1
        if b == 1: d1 = d
        if b == 2: d2 = d
        if b == 3: d3 = d
    d = [d1,d2,d3]
    #print (d)
    minimo = min(d)
    pos = d.index(minimo)
    #print(minimo)
    #print(pos)
    if pos == 0:
        bestmatchb1[1:1] = [z]
    elif pos == 1:
        bestmatchb2[1:1] = [z]
    elif pos == 2:
        bestmatchb3[1:1] = [z]
    
print('cluster1', bestmatchb1)
print('cluster2', bestmatchb2)
print('cluster3', bestmatchb3)



soma1 = 0
soma2 = 0
soma3 = 0
soma4 = 0
soma5 = 0
soma6 = 0
for m in bestmatchb1: 
    for k in range(2):
        if k == 0:
            soma1+=m[k]
        elif k == 1:
            soma2+=m[k]
            
n_elem = len(bestmatchb1)
media1 = soma1/n_elem
media2 = soma2/n_elem
mediaA = [media1,media2]
print('media cluster 1', mediaA)        


for n in bestmatchb2: 
    for k in range(2):
        if k == 0:
            soma3+=n[k]
        elif k == 1:
            soma4+=n[k]
            
            
n_elem = len(bestmatchb2)
media3 = soma3/n_elem
media4 = soma4/n_elem

mediaB = [media3,media4]
print('media cluster 2', mediaB)

for o in bestmatchb3: 
    for k in range(2):
        if k == 0:
            soma5+=n[k]
        elif k == 1:
            soma6+=n[k]
            
n_elem = len(bestmatchb2)
media5 = soma5/n_elem
media6 = soma6/n_elem
mediaC = [media5,media6]
print('media cluster 3', mediaC)



            
media = [mediaA,mediaB,mediaC]
y = media
    
    
for z in lista: 
    b = 0
    for w in y:    
        d = (euclidian(w,z))
        b+=1
        if b == 1: d1 = d
        if b == 2: d2 = d
        if b == 3: d3 = d
    d = [d1,d2,d3]
    minimo = min(d)
    pos = d.index(minimo)
    #print(minimo)
    #print(pos)
    if pos == 0:
        bestmatchb1[1:1] = [z]
    elif pos == 1:
        bestmatchb2[1:1] = [z]
    elif pos == 2:
        bestmatchb3[1:1] = [z]
a = bestmatchb1
b = bestmatchb2
c = bestmatchb3

print('cluster 1', a)
print('cluster 2', b)
print('cluster 3', c)




    
    

