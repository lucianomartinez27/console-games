#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import random
import os

jugando = True
lista_palabras = "armario caja raton escoba caramelo libro mesa guitarra".split()
lista_letras = []
lista_errores = []
palabra = random.choice(lista_palabras).upper()

def plantilla_ahorcado( palabra, lista_letras, lista_errores):
    persona = ("O", "|", "/", "\\","/", "\\")
    horca = [" ", " ", " ", " ", " ", " "]

    for i in range(len(lista_errores)):
        horca[i] = persona[i]

    print(
"""
      +---+
      |   |
      {0}   |
     {2}{1}{3}  |
     {4} {5}  |
          |
    =========""".format(horca[0], horca[1], horca[2], horca[3], horca[4], horca[5]))

    for letra in palabra:
        if letra not in lista_letras:
            print ("_", end=" ")
        else:
            print(letra, end="")

    print()
    

while jugando:
    print('='* 30)
    print('EL AHORCADO'.center(30))
    print('=' * 30)
    plantilla_ahorcado(palabra, lista_letras, lista_errores)
    letra = input('Elige una letra: ').upper()
    
    if letra != "":
        if letra in lista_letras or letra in lista_errores:
            os.system('clear')
            print()
            print('YA HAS ELEGIDO ESA LETRA')
        elif letra in palabra:
            lista_letras.append(letra)
            os.system('clear')
        else:
            lista_errores.append(letra)
            os.system('clear')
    else:
        os.system('clear')
        print()
        print('INGRESA UNA LETRA')

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
