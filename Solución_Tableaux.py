#-*-coding: utf-8-*-


print "Importando paquetes..."
from timeit import default_timer as timer
import Tableaux as T
print "Importados!"
# Guardo el tiempo al comenzar el procedimiento
start = timer()



# Creamos las letras proposicionales
#las letras representaran los circulos tal que a=casilla 1 y hay un circulo y asi sucesivamente
# los numeros a las equis
letrasProposicionales = ["a","b","c","d","e","f","g","h","i"]
for i in range(1, 10):
    letrasProposicionales.append(str(i))
    

print ("Letras proposicionales: ", letrasProposicionales)






# Regla 1: Debe haber exactamente tres figuras en el tablero
conjunciones=''
inicial = True # Para inicializar la primera conjuncion

for p in letrasProposicionales:
    aux1 = [x for x in letrasProposicionales if x != p] # Todas las letras excepto
    # print "aux1: ", aux1
    for q in aux1:
        aux2 = [x for x in aux1 if x != q] # Todas las letras excepto p y q
        # print "aux2", aux2
        for r in aux2:
            literal = r + q + p + 'Y' + 'Y'
            aux3 = [x + '-' for x in aux2 if x != r]
            for k in aux3:
                literal = k + literal + 'Y'
            # print "Literal: ", literal
            if inicial: # Inicializar la primera conjuncion
                conjunciones = literal
                inicial = False
            else:
                conjunciones = literal + conjunciones + 'O'
#print "Conjunciones: ", conjunciones

#Regla 2: 
#la regla es que si hay dos circulos seguidos y con posibilidades de ganar, debe marcarse con equis el siguiente recuadro
conjunciones='1bcY>'+conjunciones+'Y'
conjunciones='2acY>'+conjunciones+'Y'
conjunciones='3abY>'+conjunciones+'Y'
conjunciones='4efY>'+conjunciones+'Y'
conjunciones='5dfY>'+conjunciones+'Y'
conjunciones='6deY>'+conjunciones+'Y'
conjunciones='7hiY>'+conjunciones+'Y'
conjunciones='8giY>'+conjunciones+'Y'
conjunciones='9ghY>'+conjunciones+'Y'
conjunciones='1dgY>'+conjunciones+'Y'
conjunciones='4agY>'+conjunciones+'Y'
conjunciones='7adY>'+conjunciones+'Y'
conjunciones='2ehY>'+conjunciones+'Y'
conjunciones='5bhY>'+conjunciones+'Y'
conjunciones='8beY>'+conjunciones+'Y'
conjunciones='3fiY>'+conjunciones+'Y'
conjunciones='6ciY>'+conjunciones+'Y'
conjunciones='9cfY>'+conjunciones+'Y'
conjunciones='1eiY>'+conjunciones+'Y'
conjunciones='5aiY>'+conjunciones+'Y'
conjunciones='9aeY>'+conjunciones+'Y'
conjunciones='3egY>'+conjunciones+'Y'
conjunciones='5cgY>'+conjunciones+'Y'
conjunciones='7ceY>'+conjunciones+'Y'







##conjunciones=["1x","2o","3o","Y",">"]+conjunciones+["Y"]
##conjunciones=["2x","1o","3o","Y",">"]+conjunciones+["Y"]
##conjunciones=["3x","1o","2o","Y",">"]+conjunciones+["Y"]
##conjunciones=["4x","5o","6o","Y",">"]+conjunciones+["Y"]
##conjunciones=["5x","6o","4o","Y",">"]+conjunciones+["Y"]
##conjunciones=["6x","4o","5o","Y",">"]+conjunciones+["Y"]
##conjunciones=["7x","8o","9o","Y",">"]+conjunciones+["Y"]
##conjunciones=["8x","9o","7o","Y",">"]+conjunciones+["Y"]
##conjunciones=["9x","7o","8o","Y",">"]+conjunciones+["Y"]
##conjunciones=["1x","4o","7o","Y",">"]+conjunciones+["Y"]
##conjunciones=["7x","1o","4o","Y",">"]+conjunciones+["Y"]
##conjunciones=["2x","5o","8o","Y",">"]+conjunciones+["Y"]
##conjunciones=["5x","8o","2o","Y",">"]+conjunciones+["Y"]
##conjunciones=["8x","2o","5o","Y",">"]+conjunciones+["Y"]
##conjunciones=["3x","6o","9o","Y",">"]+conjunciones+["Y"]
##conjunciones=["6x","9o","3o","Y",">"]+conjunciones+["Y"]
##conjunciones=["9x","3o","6o","Y",">"]+conjunciones+["Y"]
##conjunciones=["1x","5o","9o","Y",">"]+conjunciones+["Y"]
##conjunciones=["5x","9o","1o","Y",">"]+conjunciones+["Y"]
##conjunciones=["9x","1o","5o","Y",">"]+conjunciones+["Y"]
##conjunciones=["3x","5o","7o","Y",">"]+conjunciones+["Y"]
##conjunciones=["5x","7o","3o","Y",">"]+conjunciones+["Y"]
##conjunciones=["7x","3o","5o","Y",">"]+conjunciones+["Y"]


#Creo la formula como objeto

A = T.StringtoTree(conjunciones, letrasProposicionales)
#print "Formula: ", T.Inorder(A)

lista_hojas = [[A]] # Inicializa la lista de hojas
print lista_hojas
OK = '' # El tableau regresa Satisfacible o Insatisfacible
interpretaciones = [] # lista de lista de literales que hacen verdadera lista_hojas

OK, INTS = T.Tableaux(lista_hojas, letrasProposicionales)

print "Tableau terminado!"
# Guardo el tiempo al terminar el procedimiento
end = timer()
print u"El procedimiento demoró: ", end - start

if OK == 'Satisfacible':
    if len(INTS) == 0:
        print u"Error: la lista de interpretaciones está vacía"
    else:
        print "Guardando interpretaciones en archivo..."
        import csv
        archivo = 'tableros_automatico.csv'
        with open(archivo, 'w') as output:
            writer = csv.writer(output, lineterminator='\n')
            writer.writerows(INTS)

        print "Interpretaciones guardadas  en " + archivo

##        import visualizacion as V
##        contador = 1
##        for i in INTS:
##            print "Trabajando con literales: ", i
##            V.dibujar_tablero(i,contador)
##            contador += 1

print "FIN"
