#!/usr/bin/python3
"""Gerador de lero-lero.

Gera frases de efeito sem significado real."""

import random

parte1 = []
parte2 = []
parte3 = []

lingua = int(input("Escolha a língua: 1 - português; 2 - inglês\n"))

if lingua == 2:
	parte1 = []
	parte2 = []
	parte3 = []
#Combina as partes aleatoriamente
print(random.choice(parte1) ,random.choice(parte2) , random.choice(parte3)) 
