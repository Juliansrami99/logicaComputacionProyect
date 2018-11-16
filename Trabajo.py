# -*- coding: utf-8 -*

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
from sys import argv
import csv
from PIL import Image



def dibujar_tablero(f, n):
    # Visualiza un tablero dada una formula f
    # Input:
    #   - f, una lista donde el numero 1 corresponde a la x, el numero 2 al circulo y el 3 si esta vacio
    #   - n, un numero de identificacion del archivo
    # Output:
    #   - archivo de imagen tablero_n.png

    # Inicializo el plano que contiene la figura
    fig, axes = plt.subplots()
    axes.get_xaxis().set_visible(False)
    axes.get_yaxis().set_visible(False)

    # Dibujo el tablero del tic tac toe
    step = 1./3
    tangulos = []
    tangulos.append(patches.Rectangle(*[(0, step), step, step],\
            facecolor='lemonchiffon'))
    tangulos.append(patches.Rectangle(*[(step, 0), step, step],\
            facecolor='lemonchiffon'))
    tangulos.append(patches.Rectangle(*[(2 * step, step), step, step],\
            facecolor='lemonchiffon'))
    tangulos.append(patches.Rectangle(*[(step, 2 * step), step, step],\
            facecolor='lemonchiffon'))
    tangulos.append(patches.Rectangle(*[(2 * step, 2 * step), step, step],\
            facecolor='lemonchiffon'))
    tangulos.append(patches.Rectangle(*[(0, 2 * step), step, step],\
            facecolor='lemonchiffon'))
    tangulos.append(patches.Rectangle(*[(2 * step, 0), step, step],\
            facecolor='lemonchiffon'))
    tangulos.append(patches.Rectangle(*[(step, step), step, step],\
            facecolor='lemonchiffon'))
    tangulos.append(patches.Rectangle(*[(0, 0), step, step],\
            facecolor='lemonchiffon'))

    # Creo las líneas del tablero
    for j in range(3):
        locacion = j * step
        # Crea linea horizontal en el rectangulo
        tangulos.append(patches.Rectangle(*[(0, step + locacion), 1, 0.005],\
                facecolor='black'))
        # Crea linea vertical en el rectangulo
        tangulos.append(patches.Rectangle(*[(step + locacion, 0), 0.005, 1],\
                facecolor='black'))

    for t in tangulos:
        axes.add_patch(t)
    # Cargando imagenes de la equis y del circulo respectivamente
    ruta1=("C:/Users/Julian/Desktop/Universidad/Logica para la ciencias de la computacion/Trabajo en python/equis.png")
    ruta2=("C:/Users/Julian/Desktop/Universidad/Logica para la ciencias de la computacion/Trabajo en python/circulo.png")
    equis = Image.open(ruta1)
    circulo=Image.open(ruta2)
    imagebox1 = OffsetImage(equis, zoom=0.17)
    imagebox1.image.axes = axes
    imagebox2 = OffsetImage(circulo, zoom=0.085)
    imagebox2.image.axes = axes
    

    # Creando las direcciones en la imagen de acuerdo a literal
    direcciones = {}
    direcciones[1] = [0.165, 0.835]
    direcciones[2] = [0.5, 0.835]
    direcciones[3] = [0.835, 0.835]
    direcciones[4] = [0.165, 0.5]
    direcciones[5] = [0.5, 0.5]
    direcciones[6] = [0.835, 0.5]
    direcciones[7] = [0.165, 0.165]
    direcciones[8] = [0.5, 0.165]
    direcciones[9] = [0.835, 0.165]

    lista=['1','2','3','4','5','6','7','8','9']
    lista2=['a','b','c','d','e','f','g','h','i']
    #Colocamos x en el tablero si el literal es igual a 1,si es igual a 2 colocamos 2 y si es igual a 3 vacio
    for hola in f:   
        if '-'  not in hola:
            if hola in lista:
                ab = AnnotationBbox(imagebox1, direcciones[int(hola)], frameon=False)
                axes.add_artist(ab)
            elif hola in lista2:
                if hola=='a':
                    h=1
                elif hola=='b':
                    h=2
                elif hola=='c':
                    h=3
                elif hola=='d':
                    h=4
                elif hola=='e':
                    h=5
                elif hola=='f':
                    h=6
                elif hola=='g':
                    h=7
                elif hola=='h':
                    h=8

                elif hola=='i':
                    h=9
                    
                
                ab = AnnotationBbox(imagebox2, direcciones[h], frameon=False)
                axes.add_artist(ab)
    # Agregamos el titulo al tablero
    plt.title("Tablero" +str(n)) 
    #fig.savefig("tablero_" + str(n) + ".png")


##with open("C:/Users/Julian/Desktop/Universidad/Logica para la ciencias de la computacion/Trabajo en python/Archivo.csv",'r')as archivo:
##    lineas=archivo.read().splitlines()
##    lineas.pop(0)
##    print len(lineas)
##    contador=1
##    for l in lineas:
##        linea=l.split('\t')
##        print linea
##        print "Dibujando tablero:", linea
##        b=dibujar_tablero(linea, contador)
##        contador += 1
##        plt.show()
        
                
    
    
