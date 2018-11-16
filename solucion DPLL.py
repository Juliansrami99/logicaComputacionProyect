# -*- coding: utf-8 -*
from DPLL import DPLL
import cnf
import matplotlib.pyplot as plt

letrasProposicionales = ["a","b","c","d","e","f","g","h","i"]
for i in range(1, 10):
    letrasProposicionales.append(str(i))
    

#print ("Letras proposicionales: ", letrasProposicionales)

## Reglas que se deben cumplir
cadenas=['1bcY>4-5-Y6-7-Y8-9-YYYY','2acY>4-5-Y6-7-Y8-9-YYYY','3abY>4-5-Y6-7-Y8-9-YYYY',\
         '4efY>1-2-Y3-7-Y8-9-YYYY','5dfY>1-2-Y3-7-Y8-9-YYYY','6deY>1-2-Y3-7-Y8-9-YYYY',\
         '7jiY>1-2-Y3-4-Y5-6-YYYY','8giY>1-2-Y3-4-Y5-6-YYYY','9ghY>1-2-Y3-4-Y5-6-YYYY',\
         '1dgY>2-3-Y5-6-Y8-9-YYYY','4agY>2-3-Y5-6-Y8-9-YYYY','7adY>2-3-Y5-6-Y8-9-YYYY',\
         '2ehY>1-3-Y4-6-Y7-9-YYYY','5bhY>1-3-Y4-6-Y7-9-YYYY','8beY>1-3-Y4-6-Y7-9-YYYY',\
         '3fiY>1-2-Y4-5-Y7-8-YYYY','6ciY>1-2-Y4-5-Y7-8-YYYY','9cfY>1-2-Y4-5-Y7-8-YYYY',\
         '1eiY>2-3-Y4-6-Y7-8-YYYY','5aiY>2-3-Y4-6-Y7-8-YYYY','9aeY>2-3-Y4-6-Y7-8-YYYY',\
         '3egY>1-2-Y4-6-Y8-9-YYYY','5cgY>1-2-Y4-6-Y8-9-YYYY','7ceY>1-2-Y4-6-Y8-9-YYYY']
## Colocamos una condicion inicial
## En este caso estamos diciendo que hay dos circulos en las dos primeras casillas
cond_inicial='egY'
## Lo que hacemos es buscar cual regla se tendria que cumplir dada la situacion inicial
cad=[]
for i in cadenas:
    if cond_inicial in i:
        formula=cond_inicial+i
        cad.append(formula)

lis=[]        
u=cad[0]


# Aca lo que hacemos es crear una cadena larga con la condicion inicial
for i in range(0,len(u)):
    if u[i]=='>':
        m=u[:i+1]+'Y'+u[i+1:]
        lis.append(m)

clausulas=[]
# Convertimos la cadena en CNF
A = cnf.StringtoTree(lis[0], letrasProposicionales)
A = cnf.quitarDobleNegacion(A)
A = cnf.reemplazarImplicacion(A)
A = cnf.quitarDobleNegacion(A)
OK = True
while OK:
    aux1 = cnf.Inorder(A)
    B = cnf.deMorgan(A)
    B = cnf.quitarDobleNegacion(B)
    aux2 = cnf.Inorder(B)
    if  aux1 != aux2:
        OK = True
        A=B
    else:
        OK = False
OK = True
while OK:
    OK, A = cnf.aplicaDistributiva(A)
    conjuntoClausulas = cnf.formaClausal(A)
clausulas.append(conjuntoClausulas)    

k=clausulas[0]
o=DPLL(k,{})
U,L=o.DO_DPLL()
print "Satisfacible?"
print U
print "Interpretacion:"
print L


lista=[]
for i in L:
    if L[i]==False:
        h='-'+i
        lista.append(h)
    else:
        lista.append(i)

if U == 'satisfacible':
##    if len(lista) == 0:
##        print u"Error: la lista de interpretaciones está vacía"
##    else:
##        print "Guardando interpretaciones en archivo..."
##        import csv
##        archivo = 'tableros_automatico.csv'
##        with open(archivo, 'w') as output:
##            writer = csv.writer(output, lineterminator='\n')
##            writer.writerows(lista)
##
##        print "Interpretaciones guardadas  en " + archivo

        import Trabajo as V
        contador = 1
        
        print "Trabajando con literales: ", i
        V.dibujar_tablero(lista,contador)
        contador += 1
        plt.show()

print "FIN"


