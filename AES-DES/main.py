#!/usr/bin/python
# coding: utf8

<<<<<<< HEAD



def xor_matrices(A,B):
    
    if(len(A)!=len(B)):
        print("Erro en el programa")
        exit(0)
        
    for reng in range(len(A)):
        for col in range(len(A[reng])):
            print(hex(int(A[reng][col],16)^int(B[reng][col],16)).split('x')[-1]+" ",end='')
        print()
    
def s_box():

    a="03"
    a=int(a,16)
    tabla=bin(143)[2:]
    resultado=''
    for n in range(8):
        binario=bin(a&int(tabla,2)).split('b')[-1]
        for n in range(8-len(binario)):
            binario="0"+binario
        for n in range(len(binario)-1):
            if(n==0):
                x=int(binario[0],2)
            x=x^int(binario[n+1],2)
        tabla=tabla[-1]+tabla[:-1]
        #print(resultado)
        resultado+=str(x)
        print(resultado)
    resultado=resultado.replace('0','x').replace('1','0').replace('x','1')
    print(hex(int(resultado,2)^99)[2:])

    binario="45"
    binario=int(binario,16)
    binario=bin(binario)[2:]
    for n in range(8-len(binario)):
        binario="0"+binario
    #binario=binario.replace('0','x').replace('1','0').replace('x','1') 
    x=s=binario
    for y in range(4):
        #s=bin(int(s,2)>>7)
        
        s=s[1:]+s[0]
        #print (s)
        x=bin(int(x,2)^int(s,2))

    #print(hex(int(x,2)^99))
   
    entrada="01010011"
    resultado="00000000"
    for x in range(5):
        resultado=bin(int(resultado,2)^int(entrada,2))[2:]
        for n in range(8-len(resultado)): 
            resultado="0"+resultado
        entrada=entrada[1:]+entrada[0]
        #print(entrada)

    #print (resultado)

    print(hex(int(resultado,2)^99)[2:]) 
    



def  main():
    print ("Programa AES/DES")

    A=[["32","88","31","e0"],["43","5a","31","37"],["f6","30","98","07"],["a8","8d","a2","34"]]
    B=[["2b","28","ab","09"],["7e","ae","f7","cf"],["15","d2","15","4f"],["16","a6","88","36"]]
    #xor_matrices(A,B)


    s_box()

=======
def main():
	print "Programa AES/DES"
	print "Soy donovan"
>>>>>>> 486d7cfaa9b9ec4cfeb696473566b6c79edcef3a
main()

