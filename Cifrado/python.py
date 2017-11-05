#!/usr/bin/python
# coding: utf8
import numpy as np
import PIL.Image
import PIL.ImageTk
from Tkinter import *

POLYBIOS=[["A","B","C","D","E"],["F","G","H",["I","J"],"K"],["L","M","N","O","P"],["Q","R","S","T","U"],["V","W","X","Y","Z"]]
POLYBIOS_EXT=["A","B","C","D","E"]

ALFABETO_ENG=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
ALFABETO_ES=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
ALFABETO_ES_MIN=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
DIGITOS=["0","1","2","3","4","5","6","7","8","9"]
SIMBOLOS=["$","#","@","^",'"',"~",":",";","\\","%"]

D1=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
D2=["N","R","H","J","C","W","T","Q","F","B","P","K","Z","O","D","U","X","M","V","A","L","Y","S","I","E","G"]
D3=["U","D","L","V","R","H","A","Z","S","O","W","C","K","N","G","B","Y","F","Q","I","E","X","P","T","J","M"]
D4=["X","O","F","M","D","N","R","E","H","S","T","B","L","J","V","I","K","G","U","Y","P","Q","A","W","Z","C"]
D5=["B","K","A","W","Y","G","M","J","Z","Q","I","E","T","S","H","R","N","L","D","C","V","U","X","F","P","O"]
D6=["J","E","C","T","X","P","I","B","M","Z","V","H","G","Q","A","U","O","Y","W","R","N","F","L","K","S","D"]
D7=["P","Y","G","L","M","J","S","O","V","F","D","C","T","R","I","W","K","X","E","Z","H","B","N","U","A","Q"]
D8=["D","M","N","I","L","A","R","U","K","Q","V","P","J","E","B","Y","T","H","X","F","O","G","S","Z","C","W"]
D9=["E","Q","B","S","Z","K","D","W","A","N","Y","R","F","U","X","G","V","C","P","J","T","L","O","H","M","I"]
D10=["S","F","X","H","P","N","E","C","G","T","O","L","Z","M","Q","A","W","U","K","V","I","D","Y","J","R","B"]

JEFFERSON=[D1,D2,D3,D4,D5,D6,D7,D8,D9,D10]

ALFABETOS=[ALFABETO_ENG,ALFABETO_ES,ALFABETO_ENG+DIGITOS,ALFABETO_ES+DIGITOS,ALFABETO_ES_MIN+SIMBOLOS]

VIGERENE=[]
PASE=False
mCif=""
#FRASE=""

def FUNC_POLYBIOS(frase):
    frase_cif=FUNC_POLYBIOS_CIF(frase)
    #print "Cifrado Polybios: ",frase_cif
    print "Descifrado Polybios: ",FUNC_POLYBIOS_DES(frase_cif)   

def FUNC_POLYBIOS_CIF(frase):
    frase_cif=""

    #Recorremos letra por letra de la frase dada
    for letra in frase:
        reng=0
        #Recorremos el alfabeto renglon por renglo
        for reng_s in POLYBIOS:
            try:
            #En el caso de que se encuentre la letra en el renglon se guardan las posiciones ren.index(letra) = columna
                if( letra=="I" or letra=="J"):
                    letra=["I","J"]
                frase_cif+=POLYBIOS_EXT[reng]+POLYBIOS_EXT[reng_s.index(letra)]
            except ValueError:
                pass
            reng+=1
    return frase_cif

def FUNC_POLYBIOS_DES(frase_cif):
    
    frase_des=""
    #Vamos a recorrer de 2 en dos la frase
    for n_letra in range(len(frase_cif)/2):
        #Buscamos en cada renglon las letras y en el caso de que la encontremos guardamos su posición
        for i in POLYBIOS:
            try:
                reng=i.index(frase_cif[n_letra*2])
            except ValueError:
                pass 
            try:
                col=i.index(frase_cif[(n_letra*2)+1])
            except ValueError:
                pass
        #En el caso de que no se pueda unir significa que se encontro [I,J] y agregamos simplemente la I
        try:
            frase_des+=POLYBIOS[reng][col]
        except TypeError:
            frase_des+="I"

    return frase_des

def FUNC_HILL():

    #llave=[[9,0,17],[21,4,11],[8,13,0]]
    llave=[[2,14,13],[21,4,17],[18,0,17]]
    frase=[[19,21],[0,4],[12,11]]
    #frase=[[7,1],[2,1],[19,16]]

    alfabeto=1
    #Probando funciones 
    frase_cif=FUNC_HILL_CIF(llave,frase,alfabeto)
    print "Cifrado HILL: ",frase_cif
    #frase_cif="HCTBBQ"
    print "Descifrado HILL: ",FUNC_HILL_DES(llave,frase_cif,alfabeto)
    

def FUNC_HILL_CIF(llave,frase,alfabeto):

    #Multiplicamos la matriz Llave con la matriz Mensaje y obtenemos el módulo de cada elemento
    frase_cif=np.matmul(llave,frase)%len(ALFABETOS[alfabeto])
    return NUMERO_A_LETRAS(frase_cif,alfabeto)

def FUNC_HILL_DES(llave,frase_cif,alfabeto):

    #Obtenemos el determinante de la matriz llave
    det=np.linalg.det(llave)%len(ALFABETOS[alfabeto])

    #Verificar que el determinante sea positivo
    det_1=(len(ALFABETOS[alfabeto])+1)/det
    
    #Cambiamos de letras numeros
    frase_cif=list(frase_cif)    
    n=0
    for x in frase_cif:    
        frase_cif[n]=ALFABETOS[alfabeto].index(x)
        n+=1
    frase_cif=np.reshape(frase_cif,(len(llave),len(frase_cif)/len(llave)),order='F')

    #Multiplicamos la matriz inversa por el determinante inverso, el resultado lo multiplicacmos por la frase cifrada y a ese resultado le sacamos el modulo n
    frase_des=np.rint(np.matmul((((np.linalg.inv(llave)*np.linalg.det(llave))*det_1)%len(ALFABETOS[alfabeto])).astype(float),frase_cif.astype(float))).astype(int)%len(ALFABETOS[alfabeto])

    return NUMERO_A_LETRAS(frase_des,alfabeto)

def FUNC_PLAYFAIR():
       
    llave=["H","O","L","A"]
    frase=["V","I","D","E","O"]  
    #llave=["T","O","L","E","R","A"]
    #frase=["J","U","E","V","E","S"] 
    #frase=["C","A","R","R","O","S"] 

    frase_cif=FUNC_PLAYFAIR_CIF(llave,frase)
    print "Cifrado PlayFair: ",frase_cif
    print "Descifrado PlayFair: ",FUNC_PLAYFAIR_DES(llave,frase_cif)
    
def FUNC_PLAYFAIR_CREAR_ALFABETO(llave):

    ALFABETO_PLAYFAIR=[]
    j=0
    #Agregamos la llave en los primeros elementos de la matriz
    for i in range(26+len(llave)):
        #Aqui se agregan todos los elementos de la llave en la matriz
        if (i<len(llave)):
            ALFABETO_PLAYFAIR.insert(i,llave[i])
        #Al finalizar empezamos a agregar las demás letras del alfabeto
        else:
            try:
                #Buscamos si el elemento siguiente del alfabeto se encuentra ya en el arreglo de PLAYFAIR
                ALFABETO_PLAYFAIR.index(ALFABETOS[0][j])
            except ValueError:
                #En el caso de que no se encuentre se va a agragar, creamos un caso de excepcion para la I y la J que ocupan el mismo espacio
                #Se prioriza la I
                if((llave.count("I")==1 or llave.count("J")==1) and (ALFABETOS[0][j]=="J" or ALFABETOS[0][j]=="I")):
                    pass 
                else:
                    #Agregamos el elemento en el alfabeto Playfair
                    if (ALFABETOS[0][j]!="J"):
                        ALFABETO_PLAYFAIR.insert(i,ALFABETOS[0][j])
                pass
            j+=1
    #Reordenamos el arreglo a una mariz de 5x4
    ALFABETO_PLAYFAIR=np.reshape(ALFABETO_PLAYFAIR,(5,5))
    return ALFABETO_PLAYFAIR

def FUNC_PLAYFAIR_CIF(llave,frase): 
    
    ALFABETO_PLAYFAIR=FUNC_PLAYFAIR_CREAR_ALFABETO(llave)

    #Regla 4        
    for x in range(len(frase)/2):
        if(frase[x*2]==frase[x*2+1]):
            frase.insert(x*2+1,"X")
    #Regla 5
    if(len(frase)%2!=0):
        frase.insert(len(frase),"X")
    
    frase_cif=""
    for x in range(len(frase)/2):
        #Sustituimos la J por I
        if (frase[x*2]=="J"):
            frase[x*2]="I"
        if (frase[x*2+1]=="J"):
            frase[x*2+1]="I"
        renglon=0
        #Buscamos los elementos en la matriz y obtenemos sus coordenadas
        for reng in ALFABETO_PLAYFAIR:
            reng=list(reng)
            if(reng.count(frase[x*2])==1):
                col_uno=reng.index(frase[x*2])
                reng_uno=renglon
            if(reng.count(frase[x*2+1])==1): 
                col_dos=reng.index(frase[x*2+1])
                reng_dos=renglon
            renglon+=1
        #Regla 1
        if(reng_uno==reng_dos): 
            col_dos+=1
            col_uno+=1
            if (col_uno == 5):
                col_uno=0
            if (col_dos == 5):
                col_dos=0
            frase_cif+=ALFABETO_PLAYFAIR[reng_uno][col_uno]+ALFABETO_PLAYFAIR[reng_dos][col_dos]
        #Regla 2
        elif(col_uno==col_dos): 
            reng_dos+=1
            reng_uno+=1
            if (reng_uno == 5):
                reng_uno=0
            if (reng_dos == 5):
                reng_dos=0            
            frase_cif+=ALFABETO_PLAYFAIR[reng_uno][col_uno]+ALFABETO_PLAYFAIR[reng_dos][col_dos]
        #Regla 3
        elif(reng_uno!=reng_dos and col_uno!=col_dos): 
            frase_cif+=ALFABETO_PLAYFAIR[reng_uno][col_dos]+ALFABETO_PLAYFAIR[reng_dos][col_uno]

    return frase_cif

def FUNC_PLAYFAIR_DES(llave,frase_cif):
    ALFABETO_PLAYFAIR=FUNC_PLAYFAIR_CREAR_ALFABETO(llave)
    
    frase=""
    for x in range(len(frase_cif)/2):
        renglon=0
        #Buscamos los elementos en la matriz y obtenemos sus coordenadas
        for reng in ALFABETO_PLAYFAIR:
            reng=list(reng)
            if(reng.count(frase_cif[x*2])==1):
                col_uno=reng.index(frase_cif[x*2])
                reng_uno=renglon
            if(reng.count(frase_cif[x*2+1])==1): 
                col_dos=reng.index(frase_cif[x*2+1])
                reng_dos=renglon
            renglon+=1

        #Regla 1
        if(reng_uno==reng_dos): 
            col_dos-=1
            col_uno-=1
            if (col_uno == -1):
                col_uno=4
            if (col_dos == -1):
                col_dos=4
            frase+=ALFABETO_PLAYFAIR[reng_uno][col_uno]+ALFABETO_PLAYFAIR[reng_dos][col_dos]
        #Regla 2
        elif(col_uno==col_dos): 
            reng_dos-=1
            reng_uno-=1
            if (reng_uno == -1):
                reng_uno=4
            if (reng_dos == -1):
                reng_dos=4        
            frase+=ALFABETO_PLAYFAIR[reng_uno][col_uno]+ALFABETO_PLAYFAIR[reng_dos][col_dos]
        #Regla 3
        elif(reng_uno!=reng_dos and col_uno!=col_dos): 
            frase+=ALFABETO_PLAYFAIR[reng_uno][col_dos]+ALFABETO_PLAYFAIR[reng_dos][col_uno]
    return frase

#Pasamos los números a letras conforme el Alfabeto

def NUMERO_A_LETRAS(numeros,alfabeto):
    size=1
    for dim in np.shape(numeros):
         size *= dim
    frase="" 
    for x in np.reshape(numeros,size, order='F'):
        frase+=ALFABETOS[alfabeto][x]
    return frase

#Función para rotar de derecha a izquiera o vicerversa n posiciones

def ROTATE(array,n,direccion): 
    if(direccion=="i"):
        return array[n:]+array[:n]
    if(direccion=="d"):
        return array[-n:]+array[:-n]

def FUNC_ALBERTI():
    llave=["A#",3,"1d"]
    frase="IGUALQUELANIEBLAANTEELSOLLAIGNORANCIASEDISIPAANTEELCONOCIMIENTO"
    frase=FUNC_ALBERTI_CIF(frase,llave)
    print "Cifrado ALBERTI:",frase 
    print "Descifrado ALBERTI:",FUNC_ALBERTI_DES(frase,llave)
    

def FUNC_ALBERTI_CIF(frase, llave):
    #Buscamos la letra Mayúscula que coincide
    i=ALFABETOS[3].index(llave[0][0])
    #Buscamos la letra Minúscula que coincide
    j=ALFABETOS[4].index(llave[0][1])
    #Obtenemos cada cuando se sustituye
    n_sustitucion=llave[1]
    #Obtenemos cuantos elementos se gira
    n_giro=llave[2][0]
    #Rotamos los alfabetos para que la letra que coincida sean los elementos 0 de los arreglos
    MAYUS_ROT=ROTATE(ALFABETOS[3],i,"i")
    MINUS_ROT=ROTATE(ALFABETOS[4],j,"i")
    frase_cif=""
    giro=0
    for letra in frase:
        #Condicion para rotar segun la regla
        if(giro==n_sustitucion):
            giro=0
            MINUS_ROT=ROTATE(MINUS_ROT,int(n_giro),llave[2][1])
        #Condición que interviene en caso de que se encuentre una Ñ
        if (letra=="\xc3" or letra=="\x91"):
            if(letra == "\x91"):
                continue
            frase_cif+=MINUS_ROT[MAYUS_ROT.index("Ñ")]
        else:
            #Buscamos la letra en el alfabeto exterior y obtenemos su posición para saberla en el alfbeto interior
            frase_cif+=MINUS_ROT[MAYUS_ROT.index(letra)] 
        giro+=1
    return frase_cif
 
def FUNC_ALBERTI_DES(frase_cif, llave):
    #Buscamos la letra Mayúscula que coincide
    i=ALFABETOS[3].index(llave[0][0])
    #Buscamos la letra Minúscula que coincide
    j=ALFABETOS[4].index(llave[0][1])
    n_sustitucion=llave[1]
    #Obtenemos cuantos elementos se gira
    n_giro=llave[2][0]
    #Rotamos los alfabetos para que la letra que coincida sean los elementos 0 de los arreglos
    MAYUS_ROT=ROTATE(ALFABETOS[3],i,"i")
    MINUS_ROT=ROTATE(ALFABETOS[4],j,"i")
    frase=""
    giro=0
    for letra in frase_cif:
        #Condicion para rotar segun la regla
        if(giro==n_sustitucion):
            giro=0
            MINUS_ROT=ROTATE(MINUS_ROT,int(n_giro),llave[2][1]) 
        #Condición que interviene en caso de que se encuentre una ñ
        if (letra=="\xc3" or letra=="\xb1"):
            if(letra == "\xb1"):
                continue
            frase+=MAYUS_ROT[MINUS_ROT.index("ñ")]
        else:
            #Buscamos la letra en el alfabeto interior y obtenemos su posición para saberla en el alfbeto exterior
            frase+=MAYUS_ROT[MINUS_ROT.index(letra)] 
        giro+=1  
    return frase

def FUNC_JEFFERSON():
    #frase="ME LO DIJERON Y LO OLVIDE LO VI Y LO ENTENDI LO HICE Y LO APRENDI"
    frase="MELODIJERONYLOOLVIDELOVIYLOENTENDILOHICEYLOAPRENDI"
    frase="TWOHOQTOPUUHOHMTWVUMSLWAETIOVWLQSAPKYVMMFRYMGJQQUF"
    print "Cifrado y Descifrado de Jefferson:\n"
    FUNC_JEFFERSON_CIF_DES(frase)

def FUNC_JEFFERSON_CIF_DES(frase):
    D=0
    criptos=[]
    for x in frase:
        if(D==10):
            D=0
        #Se van rotando todos los alfabetos para que la frase quede en elemento 0 de cada arreglo
        criptos.append(ROTATE(JEFFERSON[D],JEFFERSON[D].index(x),"i")) 
        D+=1
    for n in range(len(D1)):
        renglon=""
        for x in criptos:
            renglon+=x[n]
        print "\t",renglon
    return  2

def FUNC_VIGENERE():
    #frase="VIVALAVIDA"
    #llave="MURCIELAGO"
    #llave="INMOLARSE"
    frase="UNBELLOBOSQUEABANDONADO"
    llave="ASTEROIDE"
    #Creamos la tabla rotando en uno cada renglon con respecto al anterior
    for x in range(len(ALFABETOS[3])):
        VIGERENE.append(ROTATE(ALFABETOS[3],x,"i"))
    
    frase_cif=FUNC_VIGERENE_CIF(frase,llave)
    print "Cifrado Vigerene: ",frase_cif
    #frase_cif="rlriaxemedapmljscqxkvstwoigwehdgessw"
    print "Descifrado Vigerene: ",FUNC_VIGERENE_DES(frase_cif.upper(),llave)   
 
def FUNC_VIGERENE_CIF(frase,llave):
    i=0
    frase_cif=""
    for x in frase:
        #Reiniciamos la posición de la llave
        if(i==len(llave)):
            i=0 
        #Caso de escepción por Ñ
        if (x=="\xc3" or x=="\x91"): 
            if(x== "\x91"):
                continue
            frase_cif+=VIGERENE[VIGERENE[0].index(llave[i])][VIGERENE[0].index("Ñ")]
        else:    
            #Buscamos en el renglón 1 la posición del elemento de la llave y de la frase, y conforme sus resultados (coordenadas) agregamos la letra a la fras
            frase_cif+=VIGERENE[VIGERENE[0].index(llave[i])][VIGERENE[0].index(x)]
        i+=1
    return frase_cif

def FUNC_VIGERENE_DES(frase_cif,llave):
    i=0
    frase=""
    for x in frase_cif:
        if(i==len(llave)):
            i=0 
        if (x=="\xc3" or x=="\x91"):
            if(x== "\x91"):
                continue 
            frase+=VIGERENE[VIGERENE[0].index(llave[i])][VIGERENE[VIGERENE[0].index(llave[i])].index("Ñ")]
        else:    
            #Buscamos el renglón donde se encuentre la llave y dentro de ese mismo renglón buscamos el elemento del criptograma
            frase+=VIGERENE[0][VIGERENE[VIGERENE[0].index(llave[i])].index(x)]
        i+=1
    return frase

def FUNC_TRANS_GRUPOS():
    
    llave=[3,6,1,5,2,4]
    frase="HOLA COMO ESTAS YO MUY BIEN Y TU QUE TAL"
    mCif=FUNC_TRANS_GRUPOS_CIF(llave, frase)
    print mCif
    print FUNC_TRANS_GRUPOS_DES(llave, mCif.upper())

def FUNC_TRANS_GRUPOS_DES(llave, mCif):
    return FUNC_TRANS_GRUPOS_CIF(inverse_key(llave), mCif)

def FUNC_TRANS_GRUPOS_CIF(llave, mclaro):
    mclaro = "".join(mclaro.split(" ")).upper()
    mCif = ""
    for pad in range(0, len(mclaro)%len(llave)*-1%len(llave)):
        mclaro += "X" 
    for offset in range(0, len(mclaro), len(llave)):
        for element in [a-1 for a in llave]:
            mCif += mclaro[offset+element]
        mCif += " " 
    return mCif[:-1]

def inverse_key(llave):
    inverse = []
    for position in range(min(llave),max(llave)+1,1):
        inverse.append(llave.index(position)+1)
    return inverse

def FUNC_AFIN():
    a=5
    llave="AVION"
    mClaro="VIAJEALASESTRELLAS"
    alfabeto=0
    mCif=FUNC_AFIN_CIF(a, mClaro, llave, alfabeto)
    print mCif
    print FUNC_AFIN_DES(a, mCif, llave, alfabeto)
    

def mcd(n,m):
    m_aux = n%m
    if( m_aux == 0 ):
	return m
    elif( m_aux == 1 ):
	return 1
    else:
	return mcd(m,m_aux)

def invMult(a,n):
    if(mcd(a,n)!=1):
	print(str(a) + " NO TIENE INVERSO MULTIPLICATIVO EN " + str(n))
    else:
	for i in range(1,n) :
	    if( ( a*i-1 )%n == 0 ):
	        return i	

def FUNC_AFIN_CIF(a, mClaro, llave, alfabeto):
    mCifrado = ""
    boolean=True
    if(type(llave) is str):
        if(len(llave)>0):
            boolean=False
        
    if(type(llave) is int): 
        if(llave>0):
            boolean=False
    j=0
    #algoritmo AFIN desplazamiento puro o constantea a = 1 1<=b<=n
    if a == 1:               
        for i in range(len(mClaro)):         
	    abcIndex=ALFABETOS[alfabeto].index(mClaro[i])
            if(type(llave) is str):
                if (j==len(llave)):
                    j=0
	        keyIndex=ALFABETOS[alfabeto].index(llave[j])
                j+=1
            if(type(llave) is int):
                keyIndex=llave
	    cripto = (abcIndex + keyIndex)%len(ALFABETOS[alfabeto])
	    mCifrado += ALFABETOS[alfabeto][cripto]
        return mCifrado

	#algoritmo afin decimacion pura a > 1 y b = 0
    elif a > 1 and (boolean==True):
	for i in range(0,len(mClaro)):
	    abcIndex = ALFABETOS[alfabeto].index(mClaro[i])
	    cripto = (abcIndex * a)%len(ALFABETOS[alfabeto])
	    mCifrado += ALFABETOS[alfabeto][cripto] 
	return mCifrado
    elif a > 1 and (boolean==False):
	for i in range(0,len(mClaro)):
	    abcIndex = ALFABETOS[alfabeto].index(mClaro[i])
            if(type(llave) is str):
                if (j==len(llave)):
                    j=0
                keyIndex = ALFABETOS[alfabeto].index(llave[j])
                j+=1
            if(type(llave) is int):
                keyIndex=llave
	    cripto = ((abcIndex * a) + keyIndex)%len(ALFABETOS[alfabeto])
	    mCifrado += ALFABETOS[alfabeto][cripto] 
	return mCifrado


def FUNC_AFIN_DES(a,mCifrado,llave,alfabeto):
    aInv = invMult(a,len(ALFABETOS[alfabeto]))
    mDescifrado = ""
    boolean=True
    if(type(llave) is str):
        if(len(llave)>0):
            boolean=False
    if(type(llave) is int): 
        if(llave>0):
            boolean=False
    j=0
    #algoritmo AFIN desplazamiento puro o constantea a = 1 1<=b<=n
    if aInv == 1:
	for i in range(0,len(mCifrado)):
	    abcIndex = ALFABETOS[alfabeto].index(mCifrado[i])
	    #keyIndex = ALFABETOS[alfabeto].index(llave[i])
    
            if(type(llave) is str):
                if(j==len(llave)):
                    j=0 
                keyIndex = ALFABETOS[alfabeto].index(llave[j])
                j+=1
            if(type(llave) is int):
                keyIndex=llave

	    claro = (abcIndex - keyIndex)%len(ALFABETOS[alfabeto])
	    mDescifrado += ALFABETOS[alfabeto][claro]
	return mDescifrado

    #algoritmo afin decimacion pura a > 1 y b = 0
    elif aInv > 1 and (boolean==True):
	for i in range(0,len(mCifrado)):
	    abcIndex = ALFABETOS[alfabeto].index(mCifrado[i])
	    claro = (abcIndex * aInv)%len(ALFABETOS[alfabeto])
	    mDescifrado += ALFABETOS[alfabeto][claro]
	return mDescifrado
	
    elif a > 1 and (boolean==False):
	for i in range(0,len(mCifrado)):
	    abcIndex = ALFABETOS[alfabeto].index(mCifrado[i])
            if(type(llave) is str):
                if(j==len(llave)):
                    j=0
                keyIndex = ALFABETOS[alfabeto].index(llave[j])
                j+=1
            if(type(llave) is int):
                keyIndex=llave
            claro = ((abcIndex - keyIndex) * aInv)%len(ALFABETOS[alfabeto])
	    mDescifrado += ALFABETOS[alfabeto][claro]
	return mDescifrado

def FUNC_INV():
    frase="PORMA SLEJO SQUEY OMEEN CUENT REMIN ACION YONOO LVIDO"
    frase_cif=FUNC_INV_CIF(frase)
    print frase_cif
    print FUNC_INV_DES(frase_cif)

def FUNC_INV_CIF(frase):
    return frase[::-1]
def FUNC_INV_DES(frase_cif):
    return frase_cif[::-1]


class Application(Frame):
    
    def say_hi(self,event):
        
        #Obtenemos valor de la caja
        global PASE
        global mCif      
        global LLAVE
        global VIGERENE
        global FRASE
        entrada=self.contenido.get()
        #entrada=entrada.decode("utf-8")
        entrada=entrada.upper()
        #Creación de los niveles
        if(self.nivel.get()==0):
            #Nivel
            texto="\t\tNivel 1"
            #Al haber entrado a este nivel aumentamos la variable nivel
            self.nivel.set(1)
            #Cambiamos el texto del botón
            self.ENTER["text"] = "Enter",
            #Cambiamos el estado de la caja de texto para poder cambiar contenido
            self.out.config(state="normal")
            #Borramos contenido de la caja de textos
            self.out.delete(1.0,END)
            #Insertamos texto nuevo
            self.out.insert(INSERT,texto,"big")
            texto="""\n\n1. Es conocido como el padre de la criptografía.
                \n\n\ta) Julio Cesar
                \n\tb) Alberti Leon Battista
                \n\tc) Claude Shannon"""
            self.out.insert(END,texto,'low')
            #Volvemos a deshabilitar la caja de texto
            self.out.config(state="disabled")

        elif(self.nivel.get()==1 and (entrada!="ALBERTI LEON BATTISTA" and entrada!="B" and entrada!="B)" and PASE==False)):
            #En el caso de que la respuesta sea incorrecta la caja de entrada se pone roja
            self.entrada.config(background="red")

        elif(self.nivel.get()==1 and (entrada=="ALBERTI LEON BATTISTA" or entrada=="B" or entrada=="B)" or PASE==True)):
            if (PASE==False):
                entrada=""
            PASE=True
            texto="\t\tNivel 2"
            self.entrada.config(background="white") 
            self.out.config(state="normal")
            self.out.delete(1.0,END)
            self.out.insert(INSERT,texto,"big")
            texto="""\n\n2. Ingresa una cadena (SOLO LETRAS):"""
            entrada=QUITAR_ESPACIOS(entrada)
            FRASE=entrada
            #print entrada 
            if(len(entrada)>0):
                ACEPTO=True
                for x in entrada.upper():
                    try:
                        ALFABETOS[0].index(x)
                    except ValueError:
                        ACEPTO=False
                if(ACEPTO):
                    texto+="\n\n\tLa cadena ingresada fue:\n\n\t"""
                    texto+=AGREGAR_ESPACIOS(entrada)
                    texto+="\n\n    Obtener el criptograma por POLYBIOS"
                    mCif=FUNC_POLYBIOS_CIF(entrada)
                    #print mCif
                    self.nivel.set(2)
                else:
                    texto+="\n\n\t Cadena no válida, ingresa otra cadena"
            self.out.insert(END,texto,'low')
            self.out.config(state="disabled")
    
        elif(self.nivel.get()==2 and entrada!=mCif):
            #print mCif,"\t",entrada
            self.entrada.config(background="red")

        elif(self.nivel.get()==2 and entrada==mCif):
            PASE=False
            mCif=""
            texto="\t\tNivel 3"
            self.nivel.set(3)
            self.entrada.config(background="white") 
            self.out.config(state="normal")
            self.out.delete(1.0,END)
            self.out.insert(INSERT,texto,"big")
            texto="""\n\n3. Combinación de criptografía y criptoanálisis.
                \n\n\ta) Cifrado
                \n\tb) Esteganografía
                \n\tc) Criptologia"""
            self.out.insert(END,texto,'low')
            self.out.config(state="disabled")


        elif(self.nivel.get()==3 and (entrada!="CRIPTOLOGIA" and entrada!="C" and entrada!="C)" and PASE==False)):
            self.entrada.config(background="red")

        elif(self.nivel.get()==3 and (entrada=="CRIPTOLOGIA" or entrada=="C" or entrada=="C)" or PASE==True)):
            if (PASE==False):
                 entrada=""
            PASE=True
            texto="\t\tNivel 4"
            self.entrada.config(background="white")
            self.out.config(state="normal")
            self.out.delete(1.0,END)
            self.out.insert(INSERT,texto,"big")
            texto="""\n\n4. Ingresa una cadena (SIN CARACTERES ESPECIALES):"""
            entrada=QUITAR_ESPACIOS(entrada)
            FRASE+=entrada
            if(len(entrada)>0):
                ACEPTO=True
                for x in entrada.upper():
                    try:
                        ALFABETOS[3].index(x.decode("utf-8"))
                    except ValueError:
                        ACEPTO=False
                if(ACEPTO):
                    texto+="\n\n\tLa cadena a cifrar es:\n\n\t"""
                    texto+=AGREGAR_ESPACIOS(entrada+"INGENIERIA2018")
                    texto+="""\n\n    Obtener el criptograma por Afin con: 
                            \n\ta=16
              b=PERRO
              modulo=37"""
                    a=16
                    llave="PERRO"
                    alfabeto=3
                    mCif=FUNC_AFIN_CIF(a,entrada+"INGENIERIA2018", llave, alfabeto)
                    #print mCif
                    self.nivel.set(4)
                else:
                    texto+="\n\n\t Cadena no válida, ingresa otra cadena"
 
            self.out.insert(INSERT,texto,"low")
            self.out.config(state="disabled")


        elif(self.nivel.get()==4 and entrada!=mCif.decode("utf-8")):
            self.entrada.config(background="red")

        elif(self.nivel.get()==4 and entrada==mCif.decode("utf-8")):
            PASE=False
            mCif=""
            texto="\t\tNivel 5"
            self.nivel.set(5)
            self.entrada.config(background="white")
            self.out.config(state="normal")
            self.out.delete(1.0,END)
            self.out.insert(INSERT,texto,"big")
            texto="""\n\n5. Famoso emperador romano cuyo nombre lleva una técnica de cifrado.
                \n\n\ta) Julio Cesar
                \n\tb) Marco Aurelio
                \n\tc) Alejandro Magno"""
            self.out.insert(END,texto,'low')
            self.out.config(state="disabled")


        elif(self.nivel.get()==5 and entrada!="JULIO CESAR" and entrada!="A" and entrada !="A)" and PASE==False):
            self.entrada.config(background="red")

        elif(self.nivel.get()==5 and (entrada=="JULIO CESAR" or entrada=="A" or entrada =="A)" or PASE==True)):
            if(PASE==False):
                entrada=""
            PASE=True
            texto="\t\tNivel 6"
            self.entrada.config(background="white")
            self.out.config(state="normal")
            self.out.delete(1.0,END)
            self.out.insert(INSERT,texto,"big")
            texto="""\n\n6. Ingresa una cadena (LONGITUD=9):"""
            entrada=QUITAR_ESPACIOS(entrada)
            #print entrada
            if(len(entrada)>0): 
                if(len(entrada)==9): 
                    if(np.linalg.det(LETRA_NUMERO(entrada,1))>0):
                        ACEPTO=True
                        for x in entrada.upper():
                            try:
                                ALFABETOS[1].index(x)
                            except ValueError:
                                ACEPTO=False
                        if(ACEPTO):
                            texto+="\n\n\tLa cadena ingresada:\n\n\t"""
                            texto+=entrada
                            texto+="""\n\n    Obtener el criptograma por HILL con:
                                \n\tn=27
              K="""+entrada+"""
              Mclo=GATITO"""
                            frase=[[6,8],[0,20],[20,15]]
                            mCif=FUNC_HILL_CIF(LETRA_NUMERO(entrada,1),frase,1)
                            #print mCif
                            LLAVE=entrada
                            FRASE+=LLAVE
                            self.nivel.set(6)
                        else:
                            texto+="\n\n\t Cadena no válida, ingresa otra cadena"
                    else:
                        texto+="\n\n\t Determinante de la matriz negativo, ingresa otra cadena"
                else:
                    texto+="\n\n\t Cadena no válida, ingresa otra cadena"
            self.out.insert(END,texto,'low')
            self.out.config(state="disabled")
       
        elif(self.nivel.get()==6 and entrada!=mCif.decode("utf-8")):
            self.entrada.config(background="red")

        elif(self.nivel.get()==6 and entrada==mCif.decode("utf-8")):
            PASE=False
            mCif=""
            texto="\t\tNivel 7"
            self.nivel.set(7)
            self.entrada.config(background="white")
            self.out.config(state="normal")
            self.out.delete(1.0,END)
            self.out.insert(INSERT,texto,"big")
            texto="""\n\n7. Sistema criptográfico utilizado por los espartanos en el siglo V.
                \n\n\ta) Escitala
                \n\tb) Hill
                \n\tc) Polybios"""
            self.out.insert(END,texto,'low')
            self.out.config(state="disabled")
       
        elif(self.nivel.get()==7 and (entrada!="ESCITALA" and entrada!="A" and entrada!="A)" and PASE==False)):
            self.entrada.config(background="red")

        elif(self.nivel.get()==7 and (entrada=="ESCITALA" or entrada=="A" or entrada=="A)" or PASE==True)):
            texto="\t\tNivel 8"
            self.nivel.set(8)
            self.entrada.config(background="white")
            self.out.config(state="normal")
            self.out.delete(1.0,END)
            self.out.insert(INSERT,texto,"big")
            texto="\n\n8. Obtener el critpgrama por Playfair de:"
            texto+="\n\n\tMclo="+LLAVE
            texto+="\n\tK=PLATINO"
            mCif=FUNC_PLAYFAIR_CIF(list("PLATINO"),list(LLAVE))
            #print mCif  
            self.out.insert(END,texto,'low')
            self.out.config(state="disabled")

        elif(self.nivel.get()==8 and entrada!=mCif):
            self.entrada.config(background="red")

        elif(self.nivel.get()==8 and entrada==mCif):
            texto="\t\tNivel 9"
            self.nivel.set(9)
            self.entrada.config(background="white")
            self.out.config(state="normal")
            self.out.delete(1.0,END)
            self.out.insert(INSERT,texto,"big")
            texto="""\n\n9. Máquina utilizada por los Alemanes para cifrar sus mensajes en la Segunda Guerra Mundial.
                \n\n\ta) Escitala
                \n\tb) Enigma
                \n\tc) Vigerene"""
            self.out.insert(END,texto,'low')
            self.out.config(state="disabled")
 
        elif(self.nivel.get()==9 and (entrada!="ENIGMA" and entrada!="B" and entrada!="B)")):
            self.entrada.config(background="red")

        elif(self.nivel.get()==9 and (entrada=="ENIGMA" or entrada=="B" or entrada=="B)")):
            texto="\t\tNivel 10"
            self.nivel.set(10)
            self.entrada.config(background="white")
            self.out.config(state="normal")
            self.out.delete(1.0,END)
            self.out.insert(INSERT,texto,"big")
            texto="""\n\n10. Por medio del cilindro de Jefferson encuentre el mensaje.
                \n\n\tK=TWOHO QTOPU UHOHM TWVUM SLWAE 
            \t     TIOVW LQSAP KYVMM FRYMG JQQUF"""
            #print "MELODIJERONYLOOLVIDELOVIYLOENTENDILOHICEYLOAPRENDI"
            self.out.insert(END,texto,'low')
            self.out.config(state="disabled")
 
        elif(self.nivel.get()==10 and (QUITAR_ESPACIOS(entrada)!="MELODIJERONYLOOLVIDELOVIYLOENTENDILOHICEYLOAPRENDI")):
            self.entrada.config(background="red")

        elif(self.nivel.get()==10 and (QUITAR_ESPACIOS(entrada)=="MELODIJERONYLOOLVIDELOVIYLOENTENDILOHICEYLOAPRENDI")):
            texto="\t\tNivel 11"
            self.nivel.set(11)
            self.entrada.config(background="white")
            self.out.config(state="normal")
            self.out.delete(1.0,END)
            self.out.insert(INSERT,texto,"big")
            texto="""\n\n11. Matemático que publicó en 1948 la teoría matemática de la comunicación.
                \n\n\ta) René Descartes
                \n\tb) Isaac Newton
                \n\tc) Claude Shannon"""
            self.out.insert(END,texto,'low')
            self.out.config(state="disabled")
            PASE=False
        elif(self.nivel.get()==11 and (entrada!="CLAUDE SHANNON" and entrada!="C" and entrada!="C)" and PASE==False)):
            self.entrada.config(background="red")

        elif(self.nivel.get()==11 and (entrada!="CLAUDE SHANNON" or entrada!="C" or entrada!="C)" or PASE==True)):
            if (PASE==False):
                 entrada=""
            PASE=True 
            texto="\t\tNivel 12"
            self.entrada.config(background="white")
            self.out.config(state="normal")
            self.out.delete(1.0,END)
            self.out.insert(INSERT,texto,"big")
            texto="""\n\n12. Ingrese una frase."""
            entrada=QUITAR_ESPACIOS(entrada)
            if(len(entrada)>0):
                ACEPTO=True
                for x in entrada.upper():
                    try:
                        ALFABETOS[3].index(x)
                    except ValueError:
                        ACEPTO=False
                if(ACEPTO):
                    texto+="\n\n\tLa cadena ingresada fue:\n\n\t"""
                    texto+=entrada
                    texto+="\n\n    Obtener el criptograma por Disco de Alberti"
                    texto+="\n\n\tK=[J@,3,4i]"
                    llave=["J@",3,"4i"]
                    texto+="\n\tMclo="+AGREGAR_ESPACIOS("ADIOS"+entrada+LLAVE)
                    mCif=FUNC_ALBERTI_CIF("ADIOS"+entrada+LLAVE,llave)
                    LLAVE="ADIOS"+entrada+LLAVE
                    #print mCif.decode("utf-8")
                    self.nivel.set(12)
                else:
                    texto+="\n\n\t Cadena no válida, ingresa otra cadena"
            self.out.insert(END,texto,'low')
            self.out.config(state="disabled")

        elif(self.nivel.get()==12 and entrada!=mCif.decode('utf-8').upper()):
            self.entrada.config(background="red")

        elif(self.nivel.get()==12 and entrada==mCif.decode('utf-8').upper()):
            PASE=False
            mCif=""
            texto="\t\tNivel 13"
            self.nivel.set(13)
            self.entrada.config(background="white")
            self.out.config(state="normal")
            self.out.delete(1.0,END)
            self.out.insert(INSERT,texto,"big")
            texto="""\n\n13. Significado griego de kryptos.
                \n\n\ta) Reordenar
                \n\tb) Ocultar
                \n\tc) Disfrazar"""
            self.out.insert(END,texto,'low')
            self.out.config(state="disabled")

        elif(self.nivel.get()==13 and (entrada!="OCULTAR" and entrada!="B" and entrada!="B)")):
            self.entrada.config(background="red")

        elif(self.nivel.get()==13 and (entrada=="OCULTAR" or entrada=="B" or entrada=="B)")): #entrada in ["OCULTAR","B","B)"]
            texto="\t\tNivel 14"
            self.nivel.set(14)
            self.entrada.config(background="white")
            self.out.config(state="normal")
            self.out.delete(1.0,END)
            self.out.insert(INSERT,texto,"big") 
            for x in range(len(ALFABETOS[3])):
                VIGERENE.append(ROTATE(ALFABETOS[3],x,"i"))
            #LLAVE="JAQUELINA"
            LLAVE+="INGENIERIAENCOMPUTACION" 
            frase_cif=FUNC_VIGERENE_CIF(LLAVE,"ORO")
            #print LLAVE
            texto="""\n\n14. Descifrar por medio de Vigerene.
                \n\n\tCrypto="""+frase_cif+"""
               K=ORO"""
            self.out.insert(END,texto,'low')
            self.out.config(state="disabled")
        
        elif(self.nivel.get()==14 and QUITAR_ESPACIOS(entrada)!=QUITAR_ESPACIOS(LLAVE)):
            self.entrada.config(background="red")

        elif(self.nivel.get()==14 and QUITAR_ESPACIOS(entrada)==QUITAR_ESPACIOS(LLAVE)):
             
            texto="\t\tNivel 15"
            self.nivel.set(15)
            self.entrada.config(background="white")
            self.out.config(state="normal")
            self.out.delete(1.0,END)
            self.out.insert(INSERT,texto,"big")
            texto="""\n\n15. Formas en que se procesa la información.
                \n\n\ta) Serial y Bloques
                \n\tb) Bits y Bytes
                \n\tc) Renglones"""
            self.out.insert(END,texto,'low')
            self.out.config(state="disabled")

        elif(self.nivel.get()==15 and QUITAR_ESPACIOS(entrada) not in ["SERIALYBLOQUES","A","A)"]):
            self.entrada.config(background="red")

        elif(self.nivel.get()==15 and QUITAR_ESPACIOS(entrada) in ["SERIALYBLOQUES","A","A)"]):

            texto="\t\tNivel 16"
            self.nivel.set(16)
            self.entrada.config(background="white")
            self.out.config(state="normal")
            self.out.delete(1.0,END)
            self.out.insert(INSERT,texto,"big")
            
            frase_cif=FUNC_INV_CIF("SIPUEDESLEERESTOSOLOINGRESA2017YPASARASALSIGUIENTENIVEL")
            texto="\n\n16. "
            texto+=AGREGAR_ESPACIOS(frase_cif)
            self.out.insert(END,texto,'low')
            self.out.config(state="disabled")

        elif(self.nivel.get()==16 and entrada!="2017"):
            self.entrada.config(background="red")

        elif(self.nivel.get()==16 and entrada=="2017"): 
            texto="\t\tNivel 17"
            self.nivel.set(17)
            self.entrada.config(background="white")
            self.out.config(state="normal")
            self.out.delete(1.0,END)
            self.out.insert(INSERT,texto,"big")
            texto="""\n\n17. Diffie y Helman sentaron las bases de la criptografía….
                \n\n\ta) Por bloques
                \n\tb) Simetrica
                \n\tc) Asimetrica"""
            self.out.insert(END,texto,'low')
            self.out.config(state="disabled")
        
        elif(self.nivel.get()==17 and QUITAR_ESPACIOS(entrada) not in ["ASIMETRICA","C","C)"]):
            self.entrada.config(background="red")

        elif(self.nivel.get()==17 and QUITAR_ESPACIOS(entrada) in ["ASIMETRICA","C","C)"]):
             
            texto="\t\tNivel 18"
            self.nivel.set(18)
            self.entrada.config(background="white")
            self.out.config(state="normal")
            self.out.delete(1.0,END)
            self.out.insert(INSERT,texto,"big")
            texto="""\n\n18.Pregunta de regalo.
                \n\n\ta) No
                \n\tb) No
                \n\tc) Si"""
            self.out.insert(END,texto,'low')
            self.out.config(state="disabled")
        
        elif(self.nivel.get()==18 and QUITAR_ESPACIOS(entrada) not in ["SI","C","C)"]):
            self.entrada.config(background="red")

        elif(self.nivel.get()==18 and QUITAR_ESPACIOS(entrada) in ["SI","C","C)"]):
             
            texto="\t\tNivel 19"
            self.nivel.set(19)
            self.entrada.config(background="white")
            self.out.config(state="normal")
            self.out.delete(1.0,END)
            self.out.insert(INSERT,texto,"big")
            texto="""\n\n19. Arte de ocultar un mensaje en otro.
                \n\n\ta) Criptografia
                \n\tb) Esteganografia
                \n\tc) Criptología"""
            self.out.insert(END,texto,'low')
            self.out.config(state="disabled")
 
        elif(self.nivel.get()==19 and QUITAR_ESPACIOS(entrada) not in ["CRIPTOGRAFIA","B","B)"]):
            self.entrada.config(background="red")

        elif(self.nivel.get()==19 and QUITAR_ESPACIOS(entrada) in ["CRIPTOGRAFIA","B","B)"]):
            texto="\t\tNivel 20"
            self.nivel.set(20)
            self.entrada.config(background="white")
            self.out.config(state="normal")
            self.out.delete(1.0,END)
            self.out.insert(INSERT,texto,"big")
            llave=[3,2,5,1,4]
            mCif=FUNC_TRANS_GRUPOS_CIF(llave,FRASE)
            FRASE=QUITAR_ESPACIOS(FUNC_TRANS_GRUPOS_DES(llave, mCif.upper()))
            #print FRASE
    
            texto="""\n\n20. Descifra por transposición por bloques.
                \n\n\tK=[3,2,5,1,4]
                \n\tCrypto="""+mCif
            self.out.insert(END,texto,'low')
            self.out.config(state="disabled")

        elif(self.nivel.get()==20 and QUITAR_ESPACIOS(entrada) not in [FRASE]):
            self.entrada.config(background="red")

        elif(self.nivel.get()==20 and QUITAR_ESPACIOS(entrada) in [FRASE]):
            texto="\t\tNivel 21"
            self.nivel.set(21)
            self.entrada.config(background="white")
            self.out.config(state="normal")
            self.out.delete(1.0,END)
            self.out.insert(INSERT,texto,"big")
            texto="""\n\n21. Año en que se considera que la criptografia dejo de ser un arte.
                \n\n\ta) 1972
                \n\tb) 1984
                \n\tc) 1948"""
            self.out.insert(END,texto,'low')
            self.out.config(state="disabled")

        elif(self.nivel.get()==21 and entrada not in ["1948","C","C)"]):
            self.entrada.config(background="red")

        elif(self.nivel.get()==21 and entrada in ["1948","C","C)"]): 
            texto="\n\t¡FELICIDADES!"
            texto+="\n\n\tPasaste todos\n\t los niveles" 
            self.nivel.set(22)
            self.entrada.config(background="white")
            self.out.config(state="normal")
            self.out.delete(1.0,END)
            self.out.insert(INSERT,texto,"big") 
        
        self.entrada.delete(0,'end')

    def createWidgets(self):
        #Variable para los niveles
        self.nivel=IntVar()
        #self.nivel.set(19)
        #Variable para imagen
        self.image=PIL.Image.open("./images/cifrado.jpg")
        self.photo=PIL.ImageTk.PhotoImage(self.image)
        self.imagen=Label(self, image=self.photo)
        self.imagen.grid(row=0,column=0,columnspan=3,rowspan=2)
        
        texto="\t\tCriptografía"
        #Creación de caja de texto
        self.out=Text(self,height=20,width=50)
        #self.out=Text(self,height=21,width=50,foreground="#bce7f7", background="black" )
        #Variables de configuracón para texto
        self.out.tag_configure('big', font=('Verdana', 20, 'bold'))
        self.out.tag_configure('low', font=('Verdana', 10))
        self.out.insert(END,texto,'big')
    
        texto="""\n\nAlumnos: 
                \n\tAcosta Vega Sergio
                \n\tDíaz Gallardo Jesús Brandon
                \n\tLara Alamilla Donovan Adrián
                \n\tGrupo 2\n\n\n\n"""

        self.out.insert(END,texto,'low')
        self.out.grid(row=0,column=3,columnspan=3,rowspan=1)
        self.out.config(state="disabled")
            
        #Creación de caja de entrada
        self.entrada=Entry(self,width=44)
        self.contenido=StringVar()
        self.entrada["textvariable"] = self.contenido
        self.entrada.bind("<Key-Return>",self.say_hi) 
        self.entrada.grid(row=1,column=3,columnspan=3)

        #Creación de botón ENTER/SIGUIENTE
        self.ENTER = Button(self)
        self.ENTER["text"] = "Siguiente",
        self.ENTER["fg"]="green"  
        self.ENTER.bind("<Button-1>",self.say_hi) 
        self.ENTER.grid(row=2,column=4)

        #Creación de botón SALIR
        self.QUIT = Button(self)
        self.QUIT["text"] = "Salir"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit
        self.QUIT.grid(row=2,column=5)
        
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

def QUITAR_ESPACIOS(frase):
    new_frase=""
    for x in frase:
        if(x==" "):
            continue
        new_frase+=x
    return new_frase
def AGREGAR_ESPACIOS(frase):
    j=0
    texto=""
    for x in frase:
        if(j==5):
            texto+=" "
            j=0
        texto+=x
        j+=1
    return texto



def LETRA_NUMERO(frase,alfabeto):
    frase=list(frase)    
    n=0
    for x in frase:
        try: 
            frase[n]=ALFABETOS[alfabeto].index(x)
        except ValueError:
            return [[0,0,0],[0,0,0],[0,0,0]]
        n+=1
    frase=np.reshape(frase,(3,3),order='A')
    return frase



def main():
    root = Tk()
    root.resizable(width=False, height=False)
    app = Application(master=root)
    app.master.title("Proyecto 1: Criptografía")
    app.mainloop()
    try:
        root.destroy()
    except TclError:
        pass
    #FUNC_POLYBIOS(frase.upper())
    #FUNC_HILL()
    #FUNC_PLAYFAIR()
    #FUNC_ALBERTI()
    #FUNC_VIGENERE()
    #FUNC_JEFFERSON()
    #FUNC_TRANS_GRUPOS()
    #FUNC_AFIN() 
    #FUNC_INV()
main()
