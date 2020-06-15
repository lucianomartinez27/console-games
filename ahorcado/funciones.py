#!/usr/bin/env python3
#-*- coding: utf-8 -*-

def plantilla_ahorcado( palabra, lista_letras, lista_errores):
    """ plantilla que crea a partir de una palabra y dos listas con aciertos y errores
    la figura del juego del ahorcado """

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
    =========""".format(horca[0], horca[1], horca[2], horca[3], horca[4], horca[5]).center(40))
    print("Palabra:", end=" ")
    for letra in palabra:
        if letra not in lista_letras:
            print ("_", end=" ")
        else:
            print(letra, end="")

    print()