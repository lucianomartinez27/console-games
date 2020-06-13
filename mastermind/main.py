#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
Juego : MUERTOS Y HERIDOS - MASTERMIND
"""

import random
import os
from funciones import *

numeros_jugador = []

lista_resultados = []
lista_intentos = []
intentos = 1
jugando = True

# Presentación

os.system('clear')
print('MUERTOS Y HERIDOS (MASTERMIND) - EL JUEGO'.center(80))
print('-' * 80)
print()
print('Adivina un número de 4 dígitos, si aciertas el número, pero no la posición')
print('tienes un herido. Si aciertas el número y su posición tienes un muerto.')
print('Tendrás 15 intentos. Para salir pulsa "q"')
print()

n_computadora = generar_numero()
# Bucle principal
while jugando:
    n_usuario = pedir_numero(lista_intentos)

    if n_usuario == False:
        jugando = False
    elif n_usuario != None:
        jugando = comprobar_numero(n_computadora, n_usuario, lista_intentos, lista_resultados)
        intentos +=1
        
        
        
