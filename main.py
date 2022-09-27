# -*- coding: utf-8 -*-

import time
from Clases.Menu import *
from Clases.Lectura import *

def menu():
    menu = Menu()
    op = menu.ver()
    if op == "1":
        dato = crearLectura()
        registros = input("¿Cuántos registros desea?")
        while (True):
            registrarLectura(dato)
            time.sleep(1)
            registros = registros - 1
            if registros == 0:
                break
        
    elif op == "2":
        op2 = MenuEstadisticas()
    elif op == "3":
        return
    else:
        print("Opcion inválida")
        menu()

menu()

