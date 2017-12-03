#!/usr/bin/python

import numpy as np
import math
from copy import deepcopy
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import *
import PIL.Image
import PIL.ImageTk


s_box=[ ["63","7c","77","7b","f2","6b","6f","c5","30","01","67","2b","fe","d7","ab","76"],
        ["ca","82","c9","7d","fa","59","47","f0","ad","d4","a2","af","9c","a4","72","c0"],
        ["b7","fd","93","26","36","3f","f7","cc","34","a5","e5","f1","71","d8","31","15"],
        ["04","c7","23","c3","18","96","05","9a","07","12","80","e2","eb","27","b2","75"],
        ["09","83","2c","1a","1b","6e","5a","a0","52","3b","d6","b3","29","e3","2f","84"],
        ["53","d1","00","ed","20","fc","b1","5b","6a","cb","be","39","4a","4c","58","cf"],
        ["d0","ef","aa","fb","43","4d","33","85","45","f9","02","7f","50","3c","9f","a8"],
        ["51","a3","40","8f","92","9d","38","f5","bc","b6","da","21","10","ff","f3","d2"],
        ["cd","0c","13","ec","5f","97","44","17","c4","a7","7e","3d","64","5d","19","73"],
        ["60","81","4f","dc","22","2a","90","88","46","ee","b8","14","de","5e","0b","db"],
        ["e0","32","3a","0a","49","06","24","5c","c2","d3","ac","62","91","95","e4","79"],
        ["e7","c8","37","6d","8d","d5","4e","a9","6c","56","f4","ea","65","7a","ae","08"],
        ["ba","78","25","2e","1c","a6","b4","c6","e8","dd","74","1f","4b","bd","8b","8a"],
        ["70","3e","b5","66","48","03","f6","0e","61","35","57","b9","86","c1","1d","9e"],
        ["e1","f8","98","11","69","d9","8e","94","9b","1e","87","e9","ce","55","28","df"],
        ["8c","a1","89","0d","bf","e6","42","68","41","99","2d","0f","b0","54","bb","16"]]

s_box_inv=[ ["52","09","6a","d5","30","36","a5","38","bf","40","a3","9e","81","f3","d7","fb"],
            ["7c","e3","39","82","9b","2f","ff","87","34","8e","43","44","c4","de","e9","cb"],
            ["54","7b","94","32","a6","c2","23","3d","ee","4c","95","0b","42","fa","c3","4e"],
            ["08","2e","a1","66","28","d9","24","b2","76","5b","a2","49","6d","8b","d1","25"],
            ["72","f8","f6","64","86","68","98","16","d4","a4","5c","cc","5d","65","b6","92"],
            ["6c","70","48","50","fd","ed","b9","da","5e","15","46","57","a7","8d","9d","84"],
            ["90","d8","ab","00","8c","bc","d3","0a","f7","e4","58","05","b8","b3","45","06"],
            ["d0","2c","1e","8f","ca","3f","0f","02","c1","af","bd","03","01","13","8a","6b"],
            ["3a","91","11","41","4f","67","dc","ea","97","f2","cf","ce","f0","b4","e6","73"],
            ["96","ac","74","22","e7","ad","35","85","e2","f9","37","e8","1c","75","df","6e"],
            ["47","f1","1a","71","1d","29","c5","89","6f","b7","62","0e","aa","18","be","1b"],
            ["fc","56","3e","4b","c6","d2","79","20","9a","db","c0","fe","78","cd","5a","f4"],
            ["1f","dd","a8","33","88","07","c7","31","b1","12","10","59","27","80","ec","5f"],
            ["60","51","7f","a9","19","b5","4a","0d","2d","e5","7a","9f","93","c9","9c","ef"],
            ["a0","e0","3b","4d","ae","2a","f5","b0","c8","eb","bb","3c","83","53","99","61"],
            ["17","2b","04","7e","ba","77","d6","26","e1","69","14","63","55","21","0c","7d"]]


r_con=[ ["01","02","04","08","10","20","40","80","1B","36"],
        ["00","00","00","00","00","00","00","00","00","00"],
        ["00","00","00","00","00","00","00","00","00","00"],
        ["00","00","00","00","00","00","00","00","00","00"] ]

e_table=[["01","03","05","0f","11","33","55","ff","1a","2e","72","96","a1","f8","13","35"],
         ["5f","e1","38","48","d8","73","95","a4","f7","02","06","0a","1e","22","66","aa"],
         ["e5","34","5c","e4","37","59","eb","26","6a","be","d9","70","90","ab","e6","31"],
         ["53","f5","04","0c","14","3c","44","cc","4f","d1","68","b8","d3","6e","b2","cd"],
         ["4c","d4","67","a9","e0","3b","4d","d7","62","a6","f1","08","18","28","78","88"],
         ["83","9e","b9","d0","6b","bd","dc","7f","81","98","b3","ce","49","db","76","9a"],
         ["b5","c4","57","f9","10","30","50","f0","0b","1d","27","69","bb","d6","61","a3"],
         ["fe","19","2b","7d","87","92","ad","ec","2f","71","93","ae","e9","20","60","a0"],
         ["fb","16","3a","4e","d2","6d","b7","c2","5d","e7","32","56","fa","15","3f","41"],
         ["c3","5e","e2","3d","47","c9","40","c0","5b","ed","2c","74","9c","bf","da","75"],
         ["9f","ba","d5","64","ac","ef","2a","7e","82","9d","bc","df","7a","8e","89","80"],
         ["9b","b6","c1","58","e8","23","65","af","ea","25","6f","b1","c8","43","c5","54"],
         ["fc","1f","21","63","a5","f4","07","09","1b","2d","77","99","b0","cb","46","ca"],
         ["45","cf","4a","de","79","8b","86","91","a8","e3","3e","42","c6","51","f3","0e"],
         ["12","36","5a","ee","29","7b","8d","8c","8f","8a","85","94","a7","f2","0d","17"],
         ["39","4b","dd","7c","84","97","a2","fd","1c","24","6c","b4","c7","52","f6","01"]]

l_table=[[" ","00","19","01","32","02","1a","c6","4b","c7","1b","68","33","ee","df","03"],
         ["64","04","e0","0e","34","8d","81","ef","4c","71","08","c8","f8","69","1c","c1"],
         ["7d","c2","1d","b5","f9","b9","27","6a","4d","e4","a6","72","9a","c9","09","78"],
         ["65","2f","8a","05","21","0f","e1","24","12","f0","82","45","35","93","da","8e"],
         ["96","8f","db","bd","36","d0","ce","94","13","5c","d2","f1","40","46","83","38"],
         ["66","dd","fd","30","bf","06","8b","62","b3","25","e2","98","22","88","91","10"],
         ["7e","6e","48","c3","a3","b6","1e","42","3a","6b","28","54","fa","85","3d","ba"],
         ["2b","79","0a","15","9b","9f","5e","ca","4e","d4","ac","e5","f3","73","a7","57"],
         ["af","58","a8","50","f4","ea","d6","74","4f","ae","e9","d5","e7","e6","ad","e8"],
         ["2c","d7","75","7a","eb","16","0b","f5","59","cb","5f","b0","9c","a9","51","a0"],
         ["7f","0c","f6","6f","17","c4","49","ec","d8","43","1f","2d","a4","76","7b","b7"],
         ["cc","bb","3e","5a","fb","60","b1","86","3b","52","a1","6c","aa","55","29","9d"],
         ["97","b2","87","90","61","be","dc","fc","bc","95","cf","cd","37","3f","5b","d1"],
         ["53","39","84","3c","41","a2","6d","47","14","2a","9e","5d","56","f2","d3","ab"],
         ["44","11","92","d9","23","20","2e","89","b4","7c","b8","26","77","99","e3","a5"],
         ["67","4a","ed","de","c5","31","fe","18","0d","63","8c","80","c0","f7","70","07"]]

GF=[["02","03","01","01"],
    ["01","02","03","01"],
    ["01","01","02","03"],
    ["03","01","01","02"]]

GF_inv=[["0e","0b","0d","09"],
        ["09","0e","0b","0d"],
        ["0d","09","0e","0b"],
        ["0b","0d","09","0e"]]

#Manejo de claves
def sub_keys(Key):  
    for w in range(10):
        for x in range(len(Key)):
            if(x<=len(Key)-2):
                Aux=hex(int(sub_byte(Key[x+1][len(Key[x])-1][0],Key[x+1][len(Key[x])-1][1],True),16)^int(Key[x][len(Key[x])-4],16)^int(r_con[x][w],16))[2:]
                if(len(Aux)==1):
                    Aux="0"+Aux
                Key[x].append(Aux)
            else: 
                Aux=hex(int(sub_byte(Key[0][len(Key[x])-1][0],Key[0][len(Key[x])-1][1],True),16)^int(Key[x][len(Key[x])-4],16)^int(r_con[x][w],16))[2:]
                if(len(Aux)==1):
                    Aux="0"+Aux
                Key[x].append(Aux)
            for y in range(3):
                Aux=hex(int(Key[x][len(Key[x])-1],16)^int(Key[x][len(Key[x])-4],16))[2:]
                if(len(Aux)==1):
                    Aux="0"+Aux
                Key[x].append(Aux)
    return Key

#Buscamos en matrices los valores ya sea en la s_box o en la s_box_inv

def sub_byte(X,Y,inv):
    if(inv):
        return s_box[int(X,16)][int(Y,16)] 
    else:
        return s_box_inv[int(X,16)][int(Y,16)] 

#Buscamos los valores en la tabla L
def sub_byte_l(X,Y):
    return l_table[int(X,16)][int(Y,16)] 

#Buscamos los valores en la tabla E
def sub_byte_e(X,Y):
    return e_table[int(X,16)][int(Y,16)] 

def shift_rows(X,inv):
    #Cambiamos los valores de la matriz por los de la s_box o la s_box_inv
    for reng in range(len(X)):
        for col in range(len(X[reng])):
            X[reng][col]=sub_byte(X[reng][col][0],X[reng][col][1],inv)
    #Rotamos la matriz, de izquierda a derecha o de derecha a izquierda 
    for x in range(len(X)):
        if(inv):
            X[x]=X[x][x:]+X[x][:x]
        else:
            X[x]=X[x][-x:]+X[x][:-x]
    return X

#Hacemos un Xor elemento por elemento de las matrices
def xor_matrices(Msj,Key):
    
    if(len(Msj)!=len(Key)):
        print("Error en el programa")
        exit(0)
        
    for reng in range(len(Msj)):
        for col in range(len(Msj[reng])):
            Aux=hex(int(Msj[reng][col],16)^int(Key[reng][col],16)).split('x')[-1] 
            if(len(Aux)==1):
                Aux="0"+Aux
            Msj[reng][col]=Aux 
    return Msj
  
#Regresamos la subllave que se encuentra en el arreglo Key
def select_sub_key(Key,X):
    Sub_Key=[]
    for y in range(4):
        Row_Sub_Key=[]
        for x in range(X*4-4,X*4):
            Row_Sub_Key.append(Key[y][x])
        Sub_Key.append(Row_Sub_Key)
    return Sub_Key

def mult_matrices(Msj,inv):
    Temp=deepcopy(Msj) 
    #Verificamos con que Matriz se va a multiplicar si la normal o la inversa
    if(inv):  
        GF_AUX=deepcopy(GF)
    else:
        GF_AUX=deepcopy(GF_inv)

    #Hacemos sustitución de elementos con la tabla L
    for reng in range(len(Msj)):
        for col in range(len(Msj)):
            GF_AUX[reng][col]=sub_byte_l(GF_AUX[reng][col][0],GF_AUX[reng][col][1])
            Msj[reng][col]=sub_byte_l(Msj[reng][col][0],Msj[reng][col][1])
    
    #Multiplicación de Matrices
    for reng in range(len(Msj)):
        for col in range(len(Msj[reng])):
            for reng2 in range(len(Msj[reng])):
                #Verificamos que el elemento sea un HEX
                if(Msj[reng2][reng]==" "):
                    aux="00"
                else:
                    aux=hex(int(GF_AUX[col][reng2],16)+int(Msj[reng2][reng],16))[2:]
                #Verificamos el tamaño del resultado, en el caso de que de menor a F se agregaun 0 y en el caso de que sea mayor a FF se resta FF
                if(len(aux)==1):
                    aux="0"+aux
                elif(len(aux)==3):
                    aux=hex(int(aux,16)-255)[2:]
                    if(len(aux)==1):
                        aux="0"+aux
                #Regresamos el resultado de la suma a su valor con la tabla E
                if(Msj[reng2][reng]!=" "):
                    aux=sub_byte_e(aux[0],aux[1])
                #En caso de que sea el primer elemento se guarda en una variable
                if(reng2==0):
                    temp=aux
                else:
                    temp=hex(int(temp,16)^int(aux,16))[2:]
            #En el caso de que el resultado de las XORS de menor que F se agrega un cero
            if(len(temp)==1):
                temp='0'+temp
            Temp[col][reng]=temp

    #Regresamos los valores de MSJ a su valor original
    for reng in range(len(Msj)):
        for col in range(len(Msj)):
            if(Msj[reng][col]==" "):
                Msj[reng][col]="00"
            else:
                Msj[reng][col]=sub_byte_e(Msj[reng][col][0],Msj[reng][col][1])

    return Temp

def cifrar(Msj,Key):
    for x in range(11):
        #Ronda 1
        if(x==0):
            Crypto=xor_matrices(Msj,select_sub_key(Key,x+1))
        #Ronda 2 - 10
        elif(0<x and x<10):
            Crypto=xor_matrices(mult_matrices(shift_rows(Crypto,True),True),select_sub_key(Key,x+1))
        #Ronda Final
        elif(x==10):
            Crypto=xor_matrices(shift_rows(Crypto,True),select_sub_key(Key,x+1))
    return Crypto


def descifrar(Crypto,Key):
    
    for x in range(11)[::-1]:
        #Ronda 1
        if(x==10):
            Msj=shift_rows(xor_matrices(Crypto,select_sub_key(Key,x+1)),False)
        #Ronda 2 - 10
        elif(0<x and x<10):
            Msj=shift_rows(mult_matrices(xor_matrices(Msj,select_sub_key(Key,x+1)),False),False)
        #Ronda Final
        elif(x==0):
            Msj=xor_matrices(Msj,select_sub_key(Key,x+1)) 
    return Msj

def pasar_matriz_cadena(Msj,Accion):
    temp=""
    for reng in range(len(Msj)):
        for col in range(len(Msj[reng])):
            if(Accion=="Cifrar"):
                temp=temp+Msj[reng][col]
            else:
                temp=temp+chr(int(Msj[reng][col],16))
    return temp

def seleccionador(Cadena,Key,Accion):
    Agregado=0
    Cadena_Ret=""
    Msj=[]
    Temp=[]
    Hex=""
    if(Accion=="Descifrar"):
        Agregado=int(Cadena[0],16)
        Cadena=Cadena[1:]
        for n in range(int(len(Cadena)/2)):
            Hex=Hex+chr(int(Cadena[(n*2)]+Cadena[(n*2)+1],16))
        Cadena=Hex
    
    for matrices in range(math.ceil(len(Cadena)/16)):
        for col in range(4):
            for reng in range(4):
                n=(matrices*16)+(col*4)+(reng)
                if(len(Cadena)>n):
                    temp=hex(ord(Cadena[n]))[2:]
                    if(len(temp)==0):
                        temp="0"+temp
                    Temp.append(temp)
                else:
                    Agregado=Agregado+1
                    Temp.append("58")
            Msj.append(Temp)
            Temp=[]
        if(Accion=="Cifrar"):
            Cadena_Ret=Cadena_Ret+pasar_matriz_cadena(cifrar(Msj,Key),"Cifrar")
        elif(Accion=="Descifrar"):
            Cadena_Ret=Cadena_Ret+pasar_matriz_cadena(descifrar(Msj,Key),"Descifrar")
        Msj=[]
    if(Accion=="Cifrar"):
        Cadena_Ret=hex(Agregado)[2:]+Cadena_Ret
    else:
        Cadena_Ret=Cadena_Ret[:-Agregado]

    return Cadena_Ret


class Application(Frame):
    
    def abrir(self,event):
        name = askopenfilename(initialdir="./",
                           filetypes =(("Todos los archivos","*.*"),("Archivo de Texto", "*.txt")),
                           title = "Escoge un archivo."
                           )
        try:
            archivo = open(name,'r',encoding='utf-8')
            self.file.set(name)
            lines = archivo.read()
            archivo.close()
        except (TypeError,FileNotFoundError):
            lines=""
            archivo=""
            self.file.set("")
        #Con esto obtenemos el contenido en la entrada
        print(self.contenido.get())
        self.cadena.set(lines)

    def cifrar(self,event):

        Key=[["2b","28","ab","09"],
            ["7e","ae","f7","cf"],
            ["15","d2","15","4f"],
            ["16","a6","88","3c"]]
        Key=sub_keys(Key)
        Crypto=seleccionador(self.cadena.get(),Key,"Cifrar")
        if(len(self.file.get())==0):
            showinfo('Cifrado', 'No ha cargado ningun archivo')
            self.file.set("")
            self.cadena.set("")
        else:
            archivo = open(self.file.get(),'w')
            archivo.write(Crypto)
            archivo.close()
            showinfo("Cifrado","Su archivo acaba de ser cifrado")
            self.file.set("")
            self.cadena.set("")
        
    def descifrar(self,event):
        
        Key=[["2b","28","ab","09"],
            ["7e","ae","f7","cf"],
            ["15","d2","15","4f"],
            ["16","a6","88","3c"]]
        Key=sub_keys(Key)
        Msj=seleccionador(self.cadena.get(),Key,"Descifrar")
        if(len(self.file.get())==0):
            showinfo("Descifrado","No ha cargado ningun archivo")
            self.file.set("")
            self.cadena.set("")
        else:
            archivo = open(self.file.get(),'w')
            archivo.write(Msj)
            archivo.close()
            showinfo("Descifrado","Su archivo acaba de ser descifrado")
            self.file.set("")
            self.cadena.set("")


    def createWidgets(self):
        #Variable para los niveles
        self.cadena=StringVar()
        self.file=StringVar()
        #Variable para imagen
        self.image=PIL.Image.open("./images/cifrado.jpg")
        self.photo=PIL.ImageTk.PhotoImage(self.image)
        self.imagen=Label(self, image=self.photo)
        self.imagen.grid(row=0,column=0,columnspan=2,rowspan=2)

        texto="\n\t\tCriptografía"
        #Creación de caja de texto
        self.out=Text(self,height=19,width=52)
        self.out.tag_configure('big', font=('Verdana', 20, 'bold'))
        self.out.tag_configure('low', font=('Verdana', 10))
        self.out.insert(END,texto,'big')

        texto="""\n\n Alumnos:
                \n\tAcosta Vega Sergio
                \n\tDíaz Gallardo Jesús Brandon
                \n\tLara Alamilla Donovan Adrián
                \n\tGrupo 2"""
        self.out.insert(END,texto,'low')
        self.out.grid(row=0,column=2,columnspan=4,rowspan=1)
        self.out.config(state="disabled")

        #Creación de texto

        self.texto=Text(self,height=1,width=5,relief="flat",bg="#D9D9D9")
        self.texto.grid(row=1,column=2)
        self.texto.insert(END,"Llave",'low')
        self.texto.config(state="disabled")

        #Creación de entrada de texto
        self.entrada=Entry(self,width=35,show="*")
        self.contenido=StringVar()
        self.entrada["textvariable"] = self.contenido
        self.entrada.grid(row=1,column=3,columnspan=3)

        #Creación de botón ENTER/SIGUIENTE
        self.ABRIR = Button(self)
        self.ABRIR["text"] = "Abrir",
        self.ABRIR["fg"]="green"
        self.ABRIR.bind("<Button-1>",self.abrir)
        self.ABRIR.grid(row=2,column=2)

        #Creacion de botón Cifrar
        self.CIFRAR = Button(self)
        self.CIFRAR["text"] = "Cifrar",
        self.CIFRAR["fg"]="Black"
        self.CIFRAR.bind("<Button-1>",self.cifrar)
        self.CIFRAR.grid(row=2,column=3)
        
        #Creacion de botón Descifrar
        self.DESCIFRAR = Button(self)
        self.DESCIFRAR["text"] = "Descifrar",
        self.DESCIFRAR["fg"]="Black"
        self.DESCIFRAR.bind("<Button-1>",self.descifrar)
        self.DESCIFRAR.grid(row=2,column=4)

        #Creación de botón SALIR
        self.QUIT = Button(self)
        self.QUIT["text"] = "Cerrar"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit
        self.QUIT.grid(row=2,column=5)


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

def  main():
    root = Tk()
    root.resizable(width=False, height=False)
    app = Application(master=root)
    app.master.title("Proyecto 2: Criptografía")
    app.mainloop()
    try:
        root.destroy()
    except TclError:
        pass

main()

