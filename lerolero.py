#!/usr/bin/python3
"""Gerador de lero-lero.

Gera frases de efeito sem significado real."""

import random

parte1 = [
"O sistema em desenvolvimento",
"O novo protocolo de comunicação",
"O aloritmo otimizado"
]
parte2 = [
"possui excelente desempenho",
"oferece garantias de precisão acima da média",
"preenche uma lacuna significativa"
]
parte3 = [
"nas aplicações a que se destina",
"em relação às opções disponíves no mercado",
", provendo ampla vantagem vantagem competitiva a seus usuários"
]

print(random.choice(parte1) ,random.choice(parte2) , random.choice(parte3)) 
