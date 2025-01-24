#x, book = 12,15
#print (x,book)

#a= 3.1416
#print(int(a))
#print(str(a))
#hola= "te amo"
#print(hola.upper()) # para mayusculas 
#print (hola.lower()) # para poner minusculas 
#print (hola.swapcase()) # poner en mayusculas con espacio 
#print (hola.capitalize())# pone la primera en mayuscula 
#print (hola.replace ("te","no")) # remplaza el primer cararcter por el segundo caractere
#print(hola.count(""))# cuenta cuantas palabars hay en  la variable hola 
#print(hola.startswith("t"))# ver si la variable inicia con el caracter que esta entre parentesis 
#print(hola.endswith("o")) # ver si la variable finmaliza con el caracter que esta entreparentesis
#print (hola.find("a")) # encuentar la posiscion del caracter empesando desde cero 
#x = (1,1,1) # vector en python 
#aa=input("digita tu edad")

##--------------------------------------------- # hacer una matriz en python ------------------------------------------------##
# la separacion de filas esta dada por los parentesis con coma y cada columna es representada por la posicion de cada vector 

#a=[[100,10,5],
#[20,30,50],
#[70,80,90]]
#print(a)
#anchodematriz= len(a)
#for i in range (anchodematriz):
#    print(a[i]) # imprime la matris  posicion por posicion de pendiendo del acho de la matriz 

#print("este es tu valor",a[0][0])# selecciona el  primer valor de la m,atriz llamada a 

#import numpy as np

#bb= [[155,22,11,15],[111,120,123,1255],[100,141,147,1478]]
#cc=len(bb)
#bb[2][3]=17

#for i in range (cc): 
#    print (bb[i])
#-----------------------------------------------------------------------------listas--------------------------------------------------------#
#----------------------------------------- lista ----------------------#

#bolean
#si el datos es falso o verdadero 0 o 1 

#[10,20,30,40,50]
#["hola","chao","bb"]
#[10,"hhh",True,10.1]

#-----------------------------buplas--------------------------------------# 
#a=(10,5,6,7,8)
#()
#print(a[2])
#----------------------------------------diccionarios---------------------# 
#{
#    "nombre" "hard",
#    "apelido" "bruck",
#    "apodo" "zord"
#}
# --------------------------------------definir que tipo de calse es -----------------#

#print(type({
#    "nombre" "hard",
#    "apelido" "bruck",
#   "apodo" "zord"
#}
#))

#a=20 
#print (type(a))
#b= 12.85
#print (type(b))
#aa= input("escribe algo" )
#print (type(aa))
#--------------------------------------------------ciclo for---------------------------#

#for i in [0, 1, 2]:
    #for j in [0, 1]:
        #print(f"i vale {i} y j vale {j}")
#-------------------------------------------------------------------------------------- #        
# ---------------------------------------definir el rango por el programador -----------#

#for i in range (3):
#    print ("hola a todos ")
#    for j in range (5):
#        print (f"bye")
# ----------------------------------------vector con for --------------------------------#
#bb= [[155,22,11,15],[111,120,123,1255],[100,141,147,1478]]
#cc=len(bb)
#bb[0][3]=17
#print (cc)
#print(bb[0][3])

#for i in range (cc):  #el for recorre desde i = 0 hasta hasta i=cc-1 lo que signidfica que  i = 0 1 2  porque cc =3 
#   print (bb[i])   # en cada iteracion acede al numero correspondiente y lo imprime 

#---------------------------------------------------- aqui va a imprimir todo a execiopn de la primera fila -----------------------------------------------------------#

#bb= [[155,22,11,15],[111,120,123,1255],[100,141,147,1478]]
#cc=len(bb)
#bb[0][3]=17
#print (cc)
#print(bb[0][3])


#for i in range (1,cc):   # en este caso el for no va a iniciar desde laposicion cero sino i = 1 hasta la posicion 2 ya que el valor de la magnitud es de 3
   #print (bb[i]) 
# Usamos range(1, cc) para saltarnos la primera fila de la matriz, que tiene el índice 0.



# -------------------------------------------------------creacion de un vector en el cual el usario puede seleccionar el tamaño y los numeros que llevar -------------------------#
#import random  # nuemros ala azar aqui no se utilizo 
#n = int (input("digite el nuemro de n \f"))

#v= [None]*n
#for i in range (n):
#   v[i]=float(input("digite el valor del vector=  ")) 
#   print ("el valor digitado es  =",v[i],"\f ")
#print (v)


#----------------------------- vector  cuyas conmdiciones de tamaño son dadas pór el usuario y los valores son aleatorios ------------------------------------------#

#import math 
#import random as ra
#ss= int(input("escribe el tamaño del vector =   "))
#vv = [None]*ss


#for sss in range (0,ss): 
#    vv[sss]=ra.randint(0,100)
#    print(" el valor ala azar dado es \f", vv[sss],"\f")
#print(vv)

# ------------------------------------matriz cuyas condixiones de tamaño y nueros son dadas por el usuario -------------------------------------#
"""import math as mate

ic= int(input("digite  cuantas columnas va a tener su matriz "))
iff= int(input("digite  cuantas filas va a tener su matriz "))

vv=[]
for ff in range (iff):
    vv.append([])
    for cc in range (ic):
        vv[ff].append(0)
        print (" digita el valor para la posicion ",vv[ff])
        vv[ff][cc]= int(input("digite el nuemro correspondiente de la posicion =   "))

mg=len(vv)
for ff in range(0,mg):
    print(vv[ff])
"""
#----------------------------------------- matris cuyo usuario va a definir la magnitud y sus valores nuemricos van hacer al azar-------------------------------#
""""
import math as mathe
import random as ra
fila=int(input("digite el nuemro de filas que tendra tu matriz\t"))
columnas =int(input("digite el numero de columnas que tendra tu matriz \t"))

v=[]
for f in range (fila):
    v.append([])
    for c in range (columnas):
        v[f].append(0)
        v[f][c]=ra.randint(0,1000)

#para imprimir

magnitud = len(v)
for filas in range (columnas):
    print (v[f])
"""
#-----------------------------------------------------------------------------ciclo if--------------------------------------------------------------------------#
# 
