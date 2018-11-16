# -*- coding: utf-8 -*
import itertools as it

# Definimos las clase que nos permitira resolver el algoritmo DPLL
class DPLL:
    # Para ello requerimos las formulas esten de forma clausual y necesitamos la lista de los literales de la formula
    def __init__ (self, cnf, literales):
        self.cnf=cnf
        self.literales=literales

    # De esta forma aplicamos el algortimo
    def DO_DPLL(self):
        # Solucionaremos el SAT problem a traves de DPLL
        sas,inter= self.solucionar_DPLL(self.cnf, self.literales)
        # si lo que nos retorna la solucion es 'True' entonces la formula es satisfacible, de lo contrario es insatisfacible
        if sas==True:
            return 'satisfacible',inter
        else:
            return 'insatisfacible'
        
    # Para solucionar el problema a traves del DPLL
    def solucionar_DPLL(self,cnf,literales):
        # Recorremos el conjunto de clausulas para buscar clausulas unitarias o con un solo literal
        for clausula in cnf:
            if len(clausula)==1:
                # Si encontramos una clausula unitaria aplicaremos Unit propagation sobre el conjunto de clausulas y obtendremos un S prima y unas interpretaciones
                cnf,literales=self.unit_propagation(cnf,literales)
        # Si despues de aplicar el unit propagation dentro del conjunto de las clausulas resultantes esta la clausula vacia, entonces tendremos una formula insatisfacible        
        if [] in cnf:         
            return False
        # De lo contrario si despues de aplicar el unit propagation el conjunto S prima esta vacio entonces la formula es satisfacible
        if len(cnf)==0:
            if '' in literales:
                literales.pop('')
            return True,literales
        # Si aun la funciona aun no retorna nada vamos a seguir el siguiente proceso:
        # buscaremos entre todas las clausulas el literal que mas se repita y que aun no haya sido asignado en las interpretaciones para seguir con el algoritmo
        # La variable lista almacena toda las lista de clausulas como si fuera una sola lista tal que podemos buscar el que mas se repite    
        lista=list(it.chain(*cnf))
        # la variable k sera el listeral que mas se repita dentro de la variable lista
        k=max(set(lista),key= lista.count)
        # Creamos una variable temporal con los literales que aun no tienen asignada una interpretacion
        literal_temp=literales
        # Igual con el conjunto S
        cnf_temp=cnf
        # Definiremos el conjunto s prima que se obtiene de eliminar de s las clausulas con el literal k y que tambien tengan su complemento    
        if '-' in k:
            j=k.replace('-',"")
            s_prima=self.eliminar(cnf, j)
            s_prima_1=self.eliminar(cnf, k)
            if j not in literal_temp:
                literal_temp[j]=False
            return (self.solucionar_DPLL(s_prima,literal_temp) or self.solucionar_DPLL(s_prima_1,literal_temp))
        else:
            s_prima=self.eliminar(cnf, k)
            # Tener en cuenta que '-'+k hace referencia al complemento de k
            s_prima_1=self.eliminar(cnf_temp, '-'+k)
            # Aca lo que hacemos es hacer los que hace el algoritmo donde primero mira si la formula es satisfacible eliminando el literal y en caso de que no lo sea.....
            #...... lo que hace es mirar si eliminando su complemento la formula sea satisfacible, en caso de ninguna forma lo sea, retornara insatisfacible
            if k not in literal_temp:
                literal_temp[k]=True
            return (self.solucionar_DPLL(s_prima,literal_temp) or self.solucionar_DPLL(s_prima_1,literal_temp))


    # Explicamos el metodo de realiza el Unit Propagation
    def unit_propagation(self, cnf,literales):
        # Basicamente empezaremos creando una serie de variables que requerimos mas adelante
        literal=''
        clausulas_literal=[]
        temp=cnf
        lit=literales
        # Buscamos la clausula unitaria que esta dentro del conjunto de clausulas
        for clausula in cnf:
            if len(clausula)==1:
                # la variable "literal" sea la variable que contenga el literal de la clausula unitaria
                literal=clausula[0]
                break
        # Buscamos todas las clausulas que contegan el literal de la clausula unitaria
        for clausula in cnf:
            if literal in clausula:
                # Guardamos todas es clausulas en una lista que sera "clausulas_literal"
                clausulas_literal.append(clausula)

        # Lo que hacemos aca es crear otra lista de clausulas sin las clausulas que contienen el literal, esa lista sera 'temp'
        if (len(clausulas_literal))>0:
            temp=[i for i in temp if i not in clausulas_literal]
        # Lo que hacemos aca es ahora buscar las clausulas que tengan el complemtento del literal y las eliminamos de nuestra lista de clausulas nueva
        if '-' in literal:
            j= literal.replace('-',"")
            for clausula in cnf:
                if j in clausula:
                    clausulas_literal=[]
                    clausula.remove(j)
                    temp.append([x for x in clausula if i!= j])
            if j not in lit:
                lit[j]=False
            
            return temp, lit

        else:
            for clausula in cnf:
            
                if ('-'+literal) in clausula:
                    clausulas_literal=[]
                    clausula.remove('-'+literal)
                    temp.append([x for x in clausula if i!= ('-'+literal)])
            # Marcamos como asignado el literal, basicamente eliminandolo de los literales que aun no han sido asignados 
            if literal not in lit:
                lit[literal]=True
            # Retornamos el conjunto nuevo de clausulas y los literales que aun no han sido asignados
            return temp, lit

    # Con esta funcion podremos eliminar del conjunto de clausulas, las clausulas q¿con un literal especifico
    def eliminar(self, cnf ,literal):
            # Nuevamente creamos variables que trabajaremos, conj_clau sera el conjunto nuevo de clausulas que resultara despues aplicar el proceso 
            temp=[]
            conj_clau=cnf
            # Buscamos las clausulas que cntengan el literal y estas clausulas las agregamos a temp
            for clausula in conj_clau:
                if literal in clausula:
                    temp.append(clausula)
            # El nuevo S prima, llamado como conj_clau, sera el que se obtiene sin las clausulas que contenian al literal
            if len(temp)>0:
                conj_clau=[x for x in conj_clau if x not in temp]

            # Tambien eliminaremos las clausulas que contienen el complemtento del literal y obtendremos completamente el nuevo s prima

            if '-' in literal:
                j=literal.replace('-',"")
                for clausula in cnf:
                    if j in clausula:
                        temp=[]
                        clausula.remove(j)
                        conj_clau.append([x for x in clausula if x!=j ])
                return conj_clau

            else:
                for clausula in cnf:
                    if ('-'+literal) in clausula:
                        temp=[]
                        clausula.remove('-'+literal)
                        conj_clau.append([x for x in clausula if x!=('-'+literal)])
                return conj_clau
                    
                                    
            
            
            
        



            
        
        
        
                
                
    




