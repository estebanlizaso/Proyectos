import sys

##########################################################################################################################
##########################################################################################################################
#######################################           	FUNCIONES		  ########################################
##########################################################################################################################
##########################################################################################################################
#Funcion que determina si el numero n es primo o no.
#La variable i varia (en un ciclo while) entre 2 y n-1, buscando divisores de n.
#Si el resto de dividir n por i es 0, significa que n tiene un divisor distinto
#de 1 y de si mismo, entonces no es primo, la funcion devuelve "False"
#y se corta el ciclo. Sino, se recorre el ciclo hasta n-1
#y al no encontrar ningun divisor, se determina que n es primo (se devuelve "True").

def esPrimo(n):
	if n==1:
		return False
	else:
	    i = 2
	    while i < n:
	        a = n%i
	        if a == 0:
		    return False  #el return dentro del if me corta el ciclo
	        i = i + 1
	    return True

#Funcion que halla el enesimo numero primo.
#Se crea una  variable contador y una variable i,
#Usando la funcion esPrimo, busca los i que son primos y cada vez que la funcion encuentra un i que es primo, la variable contador aumenta en 1, siguiendo la funcion while mientras el valor de la variable contador sea menor a n, que es el enesimo primo, siendo este el elemento buscado (que va a ser el elemento n-1).

def enesimoPrimo(n):
	contador= 0
    	i = 2
    	while contador < n:
        	if esPrimo(i):
        	    contador=contador+1
        	i = i + 1
    	return i-1

#Funcion que comprueba si dos numeros son coprimos. Primero busco el maximo comun divisor entre 2 numeros n y m. Supongo que n>m, sino hago un swap entre n y m para que asi sea.
#Luego empiezo un ciclo que, a traves del uso de un indice i, busque divisores comunes entre n y m; si son comunes, los guardo en una variable mcd.
#El ciclo va hasta m pues a lo sumo el maximo comun divisor entre ambos es el mas chico de los mismos. Entonces el valor de la variable mcd es el del maximo comun divisor a ambos numeros. Luego, si el maximo comun divisor es 1, la funcion devuelve True, sino False.

def sonCoprimos(n,m):
	if m>n:
		n,m=m,n
	i=1
	while i<=m:
		if n%i==0 and m%i==0:
			mcd=i
		i=i+1
	if mcd==1:
		return True
	else:
		return False

#Funcion que determina el primer numero del enesimo par de numeros primos gemelos.
#La variable m varia (en un loop) entre 2 y n-1, ya que la variable contador es menor a n, buscando numeros primos con la funcion esPrimo, fijandose por el m-esimo y el m-esimo + 2 numeros, mediante el uso de un and.
#Si se cumple esto, entonces la variable contador aumentara en 1. 
#La variable m aumentara hasta que la variable contador haya llegado hasta el numero que yo introduje (n), mostrandome con el return m-1 que numero es, el primer primo del enesimo par de primos.

def enesimoParDeGemelos(n):
	contador=0
	i = 2
	while contador < n:
		if esPrimo(i) and esPrimo(i+2):
			contador=contador+1
		i=i+1
	return i-1	

#Funcion que determina una laguna de primos de longitud n. Para ello defino las variables i y longlaguna, longlaguna es una variable que se calcula en base a la resta de 2 numeros primos consecutivos, con el objetivo de ver la longitud de la laguna, para ello uso la funcion enesimoPrimo, buscando los primos i e i+1-esimos. Entonces dentro del ciclo, mientras la variable longlaguna sea menor al n que me indica el largo de la laguna que yo quiero (osea mientras la diferencia entre los 2 numeros primos consecutivos sea menor a n), va a seguir corriendo el ciclo, aumentando el valor de i ( la funcion enesimoPrimo depende de la variable i), cuando salgo del ciclo porque longlaguna es mayor o igual a n, voy a pedir que me devuelva la funcion el numero siguiente al numero primo, que es donde empieza la laguna de primos.

def primeraLaguna(n):
	i=1
	longlaguna=0
	while longlaguna<n:
		longlaguna=enesimoPrimo(i+1)-enesimoPrimo(i)-1
		i=i+1
	return enesimoPrimo(i-1)+1

#########################################################################################################################
#########################################################################################################################
#######################################            	PROGRAMA		 ########################################
#######################################		 	PRINCIPAL                ########################################
#########################################################################################################################
#########################################################################################################################


#Se utiliza (segun el primer argumento ingresado en linea de comandos) cada una de las funciones
#definidas previamente, tomando como entrada el segundo (y tercer, en el caso de sonCoprimos) argumento
#ingresado en linea de comandos, previamente convertido a numero entero. Se imprime en pantalla el resultado.

n = int(sys.argv[2])

if sys.argv[1] == "esPrimo":
	if esPrimo(n):
		print "si"
	else:
		print "no"

if sys.argv[1] == "enesimoPrimo":
	print enesimoPrimo(n)

if sys.argv[1] == "sonCoprimos":
	m = int(sys.argv[3])
	if sonCoprimos(n,m):
		print "si"
	else:
		print "no"

if sys.argv[1] == "enesimoParDeGemelos":
	print enesimoParDeGemelos(n), "y", enesimoParDeGemelos(n) + 2

if sys.argv[1] == "primeraLaguna":
	i = 0
	primlag = primeraLaguna(n)
	print "[",
	while i<n:
		print primlag + i,",",
		i = i + 1
	print "\b\b]"
		
	
