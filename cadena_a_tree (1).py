print "Funcion que pasa de una formula como cadena a un objeto Tree\n\
Recuerde que la formula debe estar escrita en notacion polaca invertida\n \
Las unicas letras proposicionales permitidas son p, q, r, s, t, v\n \
Claves de escritura para los conectivos:\n \
La negacion se escribe -\n \
La Or se escribe O\n \
El AND se escribe Y\n \
La implicacion se escribe >"

# Definimos la clase de objetos Tree para las formulas
class Tree(object):
    def __init__(self,l,iz,der):
        self.left = iz
        self.right = der
        self.label = l

# Define la funcion de imprimir rotulos Inorder(f)
def Inorder(f):
    # Determina si F es una hoja
    if f.right == None:
#        print "Es una hoja!"
        print f.label,
    elif f.label == '-':
        print f.label,
        Inorder(f.right)
    else:
        print "(",
        Inorder(f.left)
        print f.label,
        Inorder(f.right)
        print ")",

# Solicitamos una cadena

letrasProposicionales = ['p', 'q', 'r']
letrasProposicionales2 = ['p', 'q', 'r', 's', 't']
#, 's', 't', 'v'
conectivos = ['O', 'Y', '>']


pila = [] # inicializamos la pila

def arb1(cadena):
    for c in cadena:
        if c in letrasProposicionales:
            pila.append(Tree(c, None, None))
        elif c == '-':
            aux = Tree(c, None, pila[-1])
            del pila[-1]
            pila.append(aux)
        elif c in conectivos:
            aux = Tree(c, pila[-1], pila[-2])
            del pila[-1]
            del pila[-1]
            pila.append(aux)

    return pila[-1]

## Para el 10%
def arb2(cadena):
    for c in cadena:
        if c in letrasProposicionales2:
            pila.append(Tree(c, None, None))
        elif c == '-':
            aux = Tree(c, None, pila[-1])
            del pila[-1]
            pila.append(aux)
        elif c in conectivos:
            aux = Tree(c, pila[-1], pila[-2])
            del pila[-1]
            del pila[-1]
            pila.append(aux)

    return pila[-1]

## Interpretaciones 90%

inter=[]
aux={}
for a in letrasProposicionales:
    aux[a]=1
inter.append(aux)

for a in letrasProposicionales:
    inter_a=[i for i in inter]
    
    for i in inter_a:
        aux1={}

        for b in letrasProposicionales:
            if a==b:
                aux1[b]=1-i[b]
            else:
                aux1[b]=i[b]
        inter.append(aux1)

## Interpretaciones 10%
inter2=[]
aux2={}
for a in letrasProposicionales2:
    aux2[a]=1
inter2.append(aux2)

for a in letrasProposicionales2:
    inter_b=[i for i in inter2]
    
    for i in inter_b:
        aux22={}

        for b in letrasProposicionales2:
            if a==b:
                aux22[b]=1-i[b]
            else:
                aux22[b]=i[b]
        inter2.append(aux22)


def v1(f,a):
    if f.right == None:
        return inter[a][f.label]
    elif f.label == '-':
        if v1(f.right,a)==1:
            return 0
        else:
            return 1
    elif f.label == 'Y':
        if v1(f.right,a)==1 and v1(f.left,a)==1:
            return 1
        else:
            return 0
    elif f.label == 'O':
        if v1(f.right,a)==0 and v1(f.left,a)==0:
            return 0
        else:
            return 1
    elif f.label == '>':
        if v1(f.right,a)==0 and v1(f.left,a)==1:
            return 0
        else:
            return 1


def v2(f,a):
    if f.right == None:
        return inter2[a][f.label]
    elif f.label == '-':
        if v2(f.right,a)==1:
            return 0
        else:
            return 1
    elif f.label == 'Y':
        if v2(f.right,a)==1 and v2(f.left,a)==1:
            return 1
        else:
            return 0
    elif f.label == 'O':
        if v2(f.right,a)==0 and v2(f.left,a)==0:
            return 0
        else:
            return 1
    elif f.label == '>':
        if v2(f.right,a)==0 and v2(f.left,a)==1:
            return 0
        else:
            return 1

def equivalencia(f,k):
    j=list()
    for a in range(0,len(inter)):
        if v1(f,a)==v1(k,a):
            j.append(1)
        else:
            j.append(0)

    if 0 in j:
        print ("No son equivalentes")

    else:
        print ("son equivalentes")
        
        
                   

        

# Creamos las formulas
cadena11="rqOpY"
cadena12="rpYpqYO"
cadena21="qpO"
cadena22="q-p-Y-"
cadena31="-q-pO-"
cadena32="qpY"
cadena41="qp-O"
cadena42="qp>"
    
formula11=arb1(cadena11)
formula12=arb1(cadena12)
formula21=arb1(cadena21)
formula22=arb1(cadena22)
formula31=arb1(cadena31)
formula32=arb1(cadena32)
formula41=arb1(cadena41)
formula42=arb1(cadena42)


## Lista de Interpretaciones
print (" Esta es la lista de todas las posibles interpretaciones dadas tres letras proposicionales")
print (inter)

print ""
print ""


## Ejercicio 5
print ("primero: py(qor) es equivalente a (pyq) o (pyr)?")
equivalencia(formula11, formula12)

print ""
print ("segundo:")
equivalencia(formula21, formula22)
    
print ""
print ("tercero:")
equivalencia(formula31, formula32)
    
print ""
print ("cuarto:")
equivalencia(formula41, formula42)
    


## 10%

def verdad(f):
    h=list()
    for a in range(0,len(inter2)):
        if v2(f,a)==1:
            h.append(a)
    return h        

cadena10= "trsOpqY->Y"
formula10=arb2(cadena10)



print ""
print (" las interpretaciones que hacen valida la formula")
Inorder(formula10)

print ("son:")
L= verdad(formula10)
o=[]
for j in L:
    print j
    print inter2[j]


