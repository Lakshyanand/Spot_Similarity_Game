# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 18:17:53 2020

@author: HP
"""

import string
import random

symbols=[]
symbols=list(string.ascii_letters)

card1=[0]*5
card2=[0]*5

samesymbol=random.choice(symbols)
symbols.remove(samesymbol)

pos1=random.randint(0,4)
pos2=random.randint(0,4)

if(pos1==pos2):
    card1[pos1]=samesymbol
    card2[pos1]=samesymbol
    
else:
    card1[pos1]=samesymbol
    card2[pos2]=samesymbol
    # card1[pos2]=random.choice(symbols)
    # symbols.remove(card1[pos2])
    # card2[pos1]=random.choice(symbols)
    # symbols.remove(card2[pos1])
    
i=0
j=0
while(i<5):
    if(i!=pos1):
        alphabet1=random.choice(symbols)
        card1[i]=alphabet1
        symbols.remove(alphabet1)
        
    i=i+1
while(j<5):
    if(j!=pos2):
        alphabet2=random.choice(symbols)
        card2[j]=alphabet2
        symbols.remove(alphabet2)
    j=j+1
    
print(card1)
print(card2)
ch=input("enter the similarity: ")
if(ch==samesymbol):
    print("write ans")
else:
    print("wrong ans")