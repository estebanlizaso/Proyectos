import sys

#########################################################################################################################
#########################################################################################################################
################################################## FUNCIONES ############################################################
#########################################################################################################################
#########################################################################################################################

###################################################
###################################################
############ ANALISIS DE DOCUMENTO ################
###################################################
###################################################


def asignarPrimario(texto,primario,numpag):                     #Funcion que asigna a una palabra primaria su numero de pagina, cuando esta pertenece a un diccionario previo
    if primario not in texto:                                   #generado a partir de la funcion crearEstructura
        texto[primario]=[[],{}]                                 #Se crea una lista vacia donde la ubicacion 0 es una lista para las palabras primarias y la ubicacion 1 es
        texto[primario][0].append(numpag+1)                     #un diccionario vacio. Luego ubica a las palabras.
    else:
        texto[primario][0].append(numpag+1)    

def asignarSecundario(texto,primario,secundario,numpag):        #Funcion que asigna a una palabra secundaria su numero de pagina dentro de un diccionario correspondiente de una
    if primario not in texto:                                   #palabra primaria, cuando esta pertenece a un diccionario previo generado a partir de la funcion crearEstructura
        texto[primario]=[[],{}]                                 #creamos el diccionario y especificamos como va a ser el diccionario para las palabras secundarias dentro de la
        texto[primario]=[[],{secundario:[numpag+1]}]            #lista creada, luego se le indica que valor va a tomar la entrada secundaria.
    else:
        if secundario not in texto[primario][1]: 
            texto[primario][1][secundario]=[]
            texto[primario][1][secundario].append(numpag+1)
        else:
            texto[primario][1][secundario].append(numpag+1)    

def crearEstructura(lista):                                     #funcion que devuelve un diccionario para analizar a partir de la lista creada por la primer parte
                                                                #de la funcion analyzeDoc(). Ej: crearEstructura([[pescado$rojo,pescado$verde],[pescado$azul],[dr. pescador]])
                                                                #devuelve {'pescado': [ [ ] , {'verde': [1], 'rojo': [1], 'azul': [2] } ], 'dr. pescador': [ [3], { } ] }
	numpag=0  
	texto={}  
	j=0                                                        #j cuenta el numero de palabra dentro de la entrada
	while numpag< len (lista):                                 #el primer ciclo se fija que se esta dentro del texto, el segundo que uno esta en una pagina dada del texto
		while  j<len (lista[numpag]):
		    if '$' in lista[numpag][j] and '%' in lista[numpag][j]:           #Se analiza que tipo de entrada se tiene. El '%' devuelve la palabra que sigue al '%' como
		        previoaprimario=str.strip(lista[numpag][j].split('%')[1])     #salida, el '$'indica que se tiene una palabra primaria y secundaria. Para separar la entrada
				primario=str.strip(previoaprimario.split('$')[0])             #se separa el string por medio de la funcion str.strip, y se guardan las palabras en la variable
		        secundario= str.strip(previoaprimario.split('$')[1])          #que correspondan, llegado el caso que en la entrada se tenga tanto '%' y '$' se va a utilizar
		        asignarSecundario(texto,primario,secundario,numpag)           #una variable auxiliar. Se utilizan las funciones de asignacion definidas anteriormente para
		    elif "$" in lista[numpag][j]:                                     #agregar las palabras al diccionario con su correspondiente numero de pagina
		        primario=str.strip(lista[numpag][j].split('$')[0])
		        secundario= str.strip(lista[numpag][j].split('$')[1])
		        asignarSecundario(texto,primario,secundario,numpag)
		    elif '%' in lista[numpag][j]: 
		        primario=str.strip(lista[numpag][j].split('%')[1])
		        asignarPrimario(texto,primario,numpag)
		    else:
		        primario=str.strip(lista[numpag][j])
		        asignarPrimario(texto,primario,numpag)
		    j=j+1 
		j=0 
		numpag=numpag+1 
	return texto	

def analyzeDoc(curdoc):                                         #funcion que devuelve un diccionario ordenado de la siguiente manera: 
                                                                #{'primaria1':[ [nros de pag] , { 'sec1': [pags] , 'sec2': [pags] ,'sec3': ....]} , 'primaria2': ........}

	lines=curdoc.split('&')	

	curline=0                                                 #guardo el numero de la linea que estoy analizando para llamar a la linea como lines[curline]
	words_in_doc=[]                                           #lista que contiene sublistas con las palabras a indexar que encuentra en el documento, cada sublista corresponde
                                                                #a una pagina distinta, ej: [[pescado$rojo,pescado$verde],[pescado$azul],[dr. pescador]]
	while curline<len(lines):
		curword=0     	                                   #en 'curword' se guarda un contador de cuantas palabras a indexar analice
		words_in_line=[]                                    #para cada linea del documento guardo las palabras a indexar encontradas
		aux=lines[curline]                                  #contador que dice en que palabra a indexar estoy de mi linea
		while curword<lines[curline].count('{'):            #contando los '{' puedo saber cuantas palabras a indexar tiene la linea
			words_in_line.append(aux[aux.find('{')+1:aux.find('}')])         #extraigo la primer palabra a indexar en la linea
			aux=aux[aux.index('}')+1:]                    #redefino la variable aux para borrar la palabra que indexe en la instruccion anterior
			curword=curword+1
		words_in_doc = words_in_doc + [words_in_line]       #concateno las palabras a indexar en cada linea
		curline = curline + 1
	return crearEstructura(words_in_doc)                      #una vez se obtiene la lista words_in_doc creo el diccionario correspondiente con la funcion crearEstructura

###################################################
###################################################
################# OUTPUT GRAFICO ##################
###################################################
###################################################

def swap(lista,i,j):                                        #Funcion que intercambia de posicion dos elementos de una lista, entre si.
	lista[i], lista[j] = lista[j], lista[i]

def indiceDelMenor(lista,desde):                            #Funcion que devuelve la posicion del elemento mas chico (lexicograficamente) de una lista.
	imin = desde                                          #Para esto barre la lista desde una determinada posicion ('desde') y se fija si el elemento de la posicion
	j = desde+1                                           #siguiente ('desde + 1') es menor a este. Si no lo es, sigue barriendo hasta encontrar uno o llegar al
	n = len(lista)                                        #final de la lista. Si lo es, lo marca como minimo y sigue barriendo, pero comparando ahora con el nuevo minimo.
	while j < n:
		if lista[j] < lista[imin]:
			imin= j
		j= j+1
	return imin
                                	
def selectionSort(lista):                               #Funcion que ordena los elementos de una lista lexicograficamente. Para esto barre la lista y llama a la funcion
  	i = 0                                               #indiceDelMenor para saber cual es el menor. Luego lo intercambia con la funcion swap y lo lleva a la posicion 0.
   	n = len(lista)                                      #Hecho esto comienza a barrer la lista ahora desde la posicion siguiente y busca al menor de los elementos restantes,
 	while i < n:                                        #intercambiandolo con la posicion 1. Sigue asi sucesivamente hasta haber reubicado todo los elementos en orden
 		imin = indiceDelMenor(lista,i)                  #creciente.
 		swap(lista,i,imin)
 		i= i+1
  
def guardarDiccionario(texto, docnum, nombreArchivo):       #Funcion que genera el archivo "nombreArchivo" y escribe en el las claves de la variable
    if docnum == 1:                                         #"texto" (tipo diccionario) ordenadas lexicograficamente, seguido de las paginas en que aparecen.
        archivo = open(nombreArchivo, 'w')                  #En la linea siguiente a cada clave se escriben las palabras asociadas a cada una, tambien ordenadas
    else:                                                   #lexicograficamente y nuevamente seguido de las paginas en que aparecen dichas palabras asociadas.
        archivo = open(nombreArchivo, 'a')
    archivo.writelines('DOCUMENTO '+ str(docnum)+ '\n')
    input_prim=texto.keys()
    selectionSort(input_prim)
    for x in input_prim:
        archivo.writelines(x)
        for pags_prim in texto[x][0]:
            archivo.writelines (", "+str(pags_prim))
        archivo.writelines("\n")
        input_secun=texto[x][1].keys()
        selectionSort(input_secun)
        for y in input_secun:
            archivo.writelines("+ "+str(y))
            for pags_secun in texto[x][1][y]:
                archivo.writelines (", "+str(pags_secun))
            archivo.writelines("\n")
    archivo.close()
    
#########################################################################################################################
#########################################################################################################################
######################################### PROGRAMA PRINCIPAL ############################################################
#########################################################################################################################
#########################################################################################################################

f=open(sys.argv[1],'r')  
docnum = 1  #contador de documentos leidos

curline=f.readline()		#leo la primer linea para arrancar la iteracion
while curline != '':		#mientras la linea leida sea distinta a '' voy a seguir leyendo el documento
	curdoc = ''				#en curdoc se van a ir guardando las lineas del documento que estoy analizando
	curline=curline.rstrip('\n')
	while curline != '*' and curline != '':		#mientras no encuentre un delimitador * y la linea no sea vacia(porque se termino el documento), concateno lineas leidas en curdoc
		curdoc=curdoc + curline
		curline=f.readline().rstrip('\n')

	if curdoc != '':				#si el documento no esta vacio, la analizo y hago el output grafico

		output=analyzeDoc(curdoc) #analizo el documento, obteniendo como resultado el diccionario ordenado
		guardarDiccionario(output,docnum,sys.argv[2])	#esta funcion realiza el output sobre el archivo de salida
		docnum = docnum + 1
	
	curline=f.readline()

f.close()
