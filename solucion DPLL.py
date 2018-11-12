# -*- coding: utf-8 -*
from DPLL import DPLL
import cnf

letrasProposicionales = ["a","b","c","d","e","f","g","h","i","p","q","r"]
for i in range(1, 10):
    letrasProposicionales.append(str(i))
    

#print ("Letras proposicionales: ", letrasProposicionales)


cadenas=['1bcY>','2acY>','3abY>','4efY>','5dfY>','6deY>','7hiY>','8giY>','9ghY>','1dgY>','4agY>','7adY>''2ehY>','5bhY>','8beY>','3fiY>','6ciY>','9cfY>','1eiY>','5aiY>','9aeY>','3egY>','5cgY>','7ceY>']


clausulas=[]
for i in cadenas:
    A = cnf.StringtoTree(i, letrasProposicionales)
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

SAT=[]
for k in clausulas:
    o=DPLL(k, letrasProposicionales)
    SAT.append(o.DO_DPLL())

print SAT





