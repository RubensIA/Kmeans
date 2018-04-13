# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 10:39:04 2018

@author: Rubens
"""

import numpy as np

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


#Cria 3 centróides aleatórias
import random 
from random import randrange

#lista = [[1,2],[3,4],[6,9],[11,32],[13,54],[76,89]]
lista = [[1,2],[2,4],[1,9],[10,32],[11,54],[12,89]]
lista_aux = [[1,2],[2,4],[1,9],[10,32],[11,54],[12,89]]
y = []
semente = 1237

random.seed(semente)
for b in range(2):
    
    random_index = randrange(0,len(lista_aux))
    
    #print('O elemento sorteado foi:',sorteio)
    y[1:1] = [lista_aux[random_index]]

    del lista_aux[random_index]
    
print('centroide inicial', y)




bestmatchb1 = [y[0]]
bestmatchb2 = [y[1]]



def group(j):
    del bestmatchb1[:]
    del bestmatchb2[:]
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
            bestmatchb1[1:1] = [z]
        elif pos == 1:
            bestmatchb2[1:1] = [z]
    return z

group(y)
#print(bestmatchb1)
#print(bestmatchb2)


def subs(b):
    b+=1
    def somma(s):
        soma1 = 0
        soma2 = 0
        for k in range(2):
            if k == 0:
                soma1+=s[k]
            elif k == 1:
                soma2+=s[k]
            
        n_elem = len(bestmatchb1)
        media1 = soma1/n_elem
        media2 = soma2/n_elem
        media = [media1,media2]
        #print(media)        
        return media
    
    for m in bestmatchb1:
        med = somma(m)
        #print(med)
        

    for n in bestmatchb2: 
        medd = somma(n)
        #print(medd)
    
    meddia = [med,medd]
    y = meddia
    group(y)
    return b

b = 0
while b < 6:
    b = subs(b)
    
    
print('cluster1 resultante', bestmatchb1)
print('cluster2 resultante', bestmatchb2)




