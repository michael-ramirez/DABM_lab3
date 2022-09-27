# -*- coding: utf-8 -*-
class Menu():
  def ver(self):
    print("BIENVENIDO AL SISTEMA".center(50,"*"))
    print("1. Lectura de temperatura")
    print("2. Configurar parámetros de temperatura")
    print("3. Ver estadísticas")
    print("4. Salir")
    op = input(">>>")

    return op


class MenuEstadisticas():
    def ver(self):
        print("1. Gráfica de los datos capturados")
        print("2. Máxima temperatura")
        print("3. Mínima temperatura")
        print("4. Promedio")
        print("5. Volver")
        op = input(">>>")
    
        return op
        
class MenuParametros():
    def ver(self):
        print("1. Fijar nuevos parámetros")
        print("2. Ver parámetros establecidos")
        print("3. Volver")
        op = input(">>>")
    
        return op
