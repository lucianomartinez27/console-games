#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import os
import random
from funciones import plantilla_ahorcado

jugando = True
lista_palabras = "armario caja raton escoba caramelo libro mesa guitarra".split()
lista_letras = []
lista_errores = []
palabra = random.choice(lista_palabras).upper()    

os.system('clear')
while jugando:
    print('='* 30)
    print('EL AHORCADO'.center(30))
    print('=' * 30)
    plantilla_ahorcado(palabra, lista_letras, lista_errores)
    letra = input('\nElige una letra: ').upper()
    
    if letra != "":
        if letra in lista_letras or letra in lista_errores:
            os.system('clear')
            print('YA HAS ELEGIDO ESA LETRA'.center(30))
        elif letra in palabra:
            lista_letras.append(letra)
            os.system('clear')
        else:
            lista_errores.append(letra)
            os.system('clear')
    else:
        os.system('clear')
        print('INGRESA UNA LETRA'.center(30))

    if len(lista_errores) == 6:
        print("=" * 30)
        print('HAS PERDIDO'.center(30))
        print(f'LA PALABRA ERA: {palabra}'.center(30))
        print("=" * 30)
        jugando = False
    elif len(lista_letras) == len(set(palabra)):
        print("=" * 30)
        print('ACERTASTE, LA PALABRA ERA:'.center(30))
        print(f"****** {palabra} ******".center(30))
        print("HAS GANADO".center(30))
        print("=" * 30)
        jugando = False
