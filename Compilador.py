# -*- coding: utf-8 -*-

def contar_lineas(programa):
    return len(programa.readlines())

def reservar_memoria(n_lineas):
    
    etiqueta=[[n_lineas]*2 for x in range(n_lineas)]                                        #Reserva memoria para un arreglo de n elementos n=lineas
    variables=[[n_lineas]*2 for x in range(n_lineas)]
    linea_programa=list(range(n_lineas))
    opcode=[[n_lineas]*2 for x in range(n_lineas)]
    direccion_actual=[[n_lineas]*2 for x in range(n_lineas)]
    op_dir_act=[[n_lineas]*2 for x in range(n_lineas)]
    directivas=[[n_lineas]*2 for x in range(n_lineas)]
    
    return etiqueta,variables,linea_programa,opcode,direccion_actual,op_dir_act,directivas


def encuentra_asterisco(linea):
    condicion=0
    if linea.count("*")>=1:                                         #Cuenta el n?mero de asteriscos en las lineas
        while condicion>=0:
            if linea[condicion]=="*":
                linea=linea[:condicion]
                condicion=-1
            else:
                condicion+=1
    return linea

def contar_elementos_linea(linea):                                  #Cuenta los elementos que tiene la linea
    return len(linea.split())

def encontrar_gato(direccion):
    condicion=0
    r=0
    if direccion[0]=='#':
        while condicion>=0:
            if direccion[condicion]=="#":
                direccion=direccion[condicion+1:]
                condicion=-1
                r=3
            else:
                condicion+=1
    return direccion,r
    


def buscar_opcode(arreglo, direccion, etiqueta,variables=0):
    mnemonicos=[["ABA",0,0,0,0,0,"1B",0],["ABX",0,0,0,0,0,"3A",0],["ABY",0,0,0,0,0,"183A",0],["ADCA","89","99","A9","18A9","B9",0,0],["ADCB","C9","D9","E9","18E9","F9",0,0]
            ,["ADDA","8B","9B","AB","18AB","BB",0,0],["ADDB","CB","DB","EB","18EB","FB",0,0],["ADDD","C3","D3","E3","18E3","F3",0,0],["ANDA","84","94","A4","18A4","B4",0,0],["ANDB","C4","D4","E4","18E4","F4",0,0],["ASI",0,0,"68","1868","78",0,0],["ASIA",0,0,0,0,0,"48",0],["ASIB",0,0,0,0,0,"58",0],["ASID",0,0,0,0,0,"5",0],["ASR",0,0,"67","1867","77",0,0],["ASRA",0,0,0,0,0,"47",0],["ASRB",0,0,0,0,0,"57",0],["BCLR",0,"15","1D","181D",0,0,0]
            ,["BITA","85","95","A5","18A5","B5",0,0],["BITB","C5","D5","E5","18E5","F5",0,0],["BRCLR",0,"13","IF","181F",0,0,0],["BRSET",0,"12","1E","181E",0,0,0],["BSET",0,"14","1C","181C",0,0,0],["CBA",0,0,0,0,0,"11",0],["CLC",0,0,0,0,0,"0C",0],["CLI",0,0,0,0,0,"0E",0],["CLR",0,0,"6F","186F","7F",0,0],["CLRA",0,0,0,0,0,"4F",0],["CLRB",0,0,0,0,0,"5F",0],["CLV",0,0,0,0,0,"0A",0],["CMPA","81","91","A1","18A1","B1",0,0],["CMPB","C1","D1","E1","18E1","F1",0,0],["COM",0,0,"63","1863","73",0,0]
            ,["COMA",0,0,0,0,0,"43",0],["COMB",0,0,0,0,0,"53",0],["CPD","1A83","1A93","1AA3","CDA3","1AB3",0,0],["CPX","8C","9C","AC","CDAC","BC",0,0],["CPY","188C","189C","1AAC","18AC","18BC",0,0],["DAA",0,0,0,0,0,"19",0],["DEC",0,0,"6A","186A","7A",0,0],["DECA",0,0,0,0,0,"4A",0],["DECB",0,0,0,0,0,"5A",0],["DES",0,0,0,0,0,"34",0],["DEX",0,0,0,0,0,"09",0],["DEY",0,0,0,0,0,"1809",0],["EORA","88","98","A8","18A8","B8",0,0],["EORB","C8","D8","E8","18E8","F8",0,0],["FDIV",0,0,0,0,0,"03",0],["IDIV",0,0,0,0,0,"02",0]
            ,["INC",0,0,"6C","186C","7C",0,0],["INCA",0,0,0,0,0,"4C",0],["INCB",0,0,0,0,0,"5C",0],["INS",0,0,0,0,0,"31",0],["INX",0,0,0,0,0,"08",0],["INY",0,0,0,0,0,"1808",0],["LDAA","86","96","A6","18A6","B6",0,0],["LDAB","C6","D6","E6","18E6","F6",0,0],["LDD","CC","DC","EC","18EC","FC",0,0],["LDS","8E","9E","AE","18AE","BE",0,0],["LDX","CE","DE","EE","CDEE","FE",0,0],["LDY","18CE","18DE","1AEE","18EE","18FE",0,0],["LSL",0,0,"68","1868","78",0,0]
            ,["LSLA",0,0,0,0,0,"48",0],["LSLB",0,0,0,0,0,"58",0],["LSLD",0,0,0,0,0,"05",0],["LSR",0,0,"64","1864","74",0,0],["LSRA",0,0,0,0,0,"44",0],["LSRB",0,0,0,0,0,"54",0],["LSRD",0,0,0,0,0,"04",0],["MUL",0,0,0,0,0,"3D",0],["NEG",0,0,"60","1860","70",0,0],["NEGA",0,0,0,0,0,"40",0],["NEGB",0,0,0,0,0,"50",0],["NOP",0,0,0,0,0,"01",0],["ORAA","8A","9A","AA","18AA","BA",0,0],["ORAB","CA","DA","EA","18EA","FA",0,0],["PSHA",0,0,0,0,0,"36",0],["PSHB",0,0,0,0,0,"37",0],["PSHX",0,0,0,0,0,"3C",0],["PSHY",0,0,0,0,0,"183C",0]
            ,["PULA",0,0,0,0,0,"32",0],["PULX",0,0,0,0,0,"38",0],["PULB",0,0,0,0,0,"1838",0],["ROL",0,0,"69","1869","79",0,0],["ROLA",0,0,0,0,0,"49",0],["ROLB",0,0,0,0,0,"59",0],["ROR",0,0,"66","1866","76",0,0],["RORA",0,0,0,0,0,"46",0],["RORB",0,0,0,0,0,"56",0],["RTI",0,0,0,0,0,"3B",0],["RTS",0,0,0,0,0,"39",0],["SBA",0,0,0,0,0,"10",0],["SBCA","82","92","A2","18A2","B2",0,0],["SBCB","C2","D2","E2","18E2","F2",0,0],["SEC",0,0,0,0,0,"OD",0],["SEI",0,0,0,0,0,"OF",0],["SEV",0,0,0,0,0,"OB",0],["STAA",0,"97","A7","18A7","B7",0,0],["STAB",0,"D7","E7","18E7","F7",0,0],["STD",0,"DD","ED","18ED","FD",0,0]
            ,["STOP",0,0,0,0,0,"CF",0],["STS",0,"9F","AF","18AF","BF",0,0],["STX",0,"D","EF","CDEF","FF",0,0],["STY",0,"18DF","1AEF","18EF","FF",0,0],["SUBA","80","90","A0","18A0","B0",0,0],["SUBB","C0","D0","E0","18E0","F0",0,0],["SUBD","83","93","A3","18A3","B3",0,0],["SWI",0,0,0,0,0,"3F",0],["TAB",0,0,0,0,0,"16",0],["TAP",0,0,0,0,0,"06",0],["TBA",0,0,0,0,0,"17",0],["TETS",0,0,0,0,0,"00",0],["TPA",0,0,0,0,0,"07",0],["TST",0,0,"6D","186D","7D",0,0],["TSTA",0,0,0,0,0,"4D",0],["TSTB",0,0,0,0,0,"5D",0],["TSX",0,0,0,0,0,"30",0],["TSY",0,0,0,0,0,"1830",0],["TXS",0,0,0,0,0,"35",0]
            ,["TYS",0,0,0,0,0,"1835",0],["WAI",0,0,0,0,0,"3E",0],["XGDX",0,0,0,0,0,"8F",0],["XGDY",0,0,0,0,0,"188F",0]]

    relativos=[["BCC",0,0,0,0,0,0,"24"],["BCS",0,0,0,0,0,0,"25"],["BEQ",0,0,0,0,0,0,"27"],["BGE",0,0,0,0,0,0,"2C"],["BGT",0,0,0,0,0,0,"2E"],["BHI",0,0,0,0,0,0,"22"]
               ,["BHS",0,0,0,0,0,0,"24"],["BLE",0,0,0,0,0,0,"2F"],["BLO",0,0,0,0,0,0,"25"],["BLS",0,0,0,0,0,0,"23"],["BLT",0,0,0,0,0,0,"2D"],["BMI",0,0,0,0,0,0,"2B"]
               ,["BNE",0,0,0,0,0,0,"26"],["BPL",0,0,0,0,0,0,"2A"],["BRA",0,0,0,0,0,0,"20"],["BRN",0,0,0,0,0,0,"21"],["BSR",0,0,0,0,0,0,"8D"],["BVC",0,0,0,0,0,0,"28"]
               ,["BVS",0,0,0,0,0,0,"29"]]
    
    direccion,tres=encontrar_gato(direccion)
                        
    for cont in list(range(len(variables))):
   
        if etiqueta==variables[cont][0] or direccion==variables[cont][0]:
            direccion=variables[cont][1]  
          
    if tres==3:
        
        direccion='#'+direccion
    if arreglo=="BSET":
        return "1C"+direccion[1]+direccion[2]+direccion[8]+direccion[9]
    if arreglo=="BRCLR":
        return "1F"+direccion[1]+direccion[2]+direccion[8]+direccion[9]+"XX"
    if arreglo=="FCB":
        print("\n\tDirectiva")
        return direccion[1]+direccion[2]+direccion[5]+direccion[6]
    
    if arreglo=="JSR" or arreglo=="JMP":
        if arreglo=="JSR":
            return "BDXXXX"
        if arreglo=="JMP":
            return "7EXXXX"
        
    for cont in list(range (len(relativos))):
    
        if arreglo==relativos[cont][0]:
            print("\n\tModo de Direccionamiento Relativo")
            return relativos[cont][7]+"XX"
            
        
    for cont in list(range (len(mnemonicos))):
    
        if arreglo==mnemonicos[cont][0]:
            
            #if direccion.count("$")==0 and len(direccion)>2:
             #   print("La direccion no esta en Hexadecimal")
              #  direccion="$"+str(format(direccion_actual[dir_act-1][0],'X'))
               # print(direccion)
            
            if direccion.count("$")>=1:
               
                if direccion[0]=='#':
                    print("\n\tModo de Direccionamiento Inmediato")
                    return mnemonicos[cont][1]+direccion[2:]
                
                if direccion.count("#")==0:
                
                    if len(direccion)<=3:
                        print("\n\tModo de Direccionamiento Directo")
                        return mnemonicos[cont][2]+direccion[1:]
                    
                    if len(direccion)>=4 and direccion.count(",")==0:
                        if direccion[1]=='0' and direccion[2]=='0':
                            if mnemonicos[cont][2]==0:
                                print("\n\tModo de Direccionamiento Extendido")
                                return mnemonicos[cont][5]+direccion[1:]
                            else:
                                print("\n\tModo de Direccionamiento Directo")
                                return mnemonicos[cont][2]+direccion[3:]                
                        else:
                            print("\n\tModo de Direccionamiento Extendido")
                            return mnemonicos[cont][5]+direccion[1:]
                    
                    if direccion.count(",")==1:
                     
                        if direccion.count("X")==1 or direccion.count("x")==1:
                            print("\n\tModo de Direcionamiento Indexado (X)")
                            if direccion[1]=='0' and direccion[2]=='0' and len(direccion)<=5:
                                return mnemonicos[cont][3]+direccion[1]+direccion[2]
                            else:
                                
                                if direccion[1]=='0' and direccion[2]=='0':
                                    return mnemonicos[cont][3]+direccion[3]+direccion[4]
                                else:
                                    print("hola")
                                    return mnemonicos[cont][3]+direccion[1:5]
                        
                        if direccion.count("Y")==1 or direccion.count("y")==1:
                            print("\n\tModo de Direcionamiento Indexado (Y)")
                            
                            if direccion[1]=='0' and direccion[2]=='0' and len(direccion)<=5:
                                return mnemonicos[cont][4]+direccion[1]+direccion[2]
                            else:
                                
                                if direccion[1]=='0' and direccion[2]=='0':
                                    return mnemonicos[cont][4]+direccion[3]+direccion[4]
                                else:
                                    return mnemonicos[cont][4]+direccion[1:5]
        
                                #return mnemonicos[cont][4]+" "+direccion[1:]
            if direccion=='0':
                print("\n\tModo de Direccionamiento Inherente")
                return mnemonicos[cont][6]
            
def un_elemento(arreglo,variables,x=0):
        if x>=1:
            op=buscar_opcode(arreglo[0].upper(),'0','0',variables)
            return arreglo[0].upper(),op
        else:
            return arreglo[0].upper()            
            
def dos_elementos(arreglo,variables,x=0):
        if x==1:
            op=buscar_opcode(arreglo[0].upper(),arreglo[1],'0',variables)
            return arreglo[0].upper(), arreglo[1],op                                  #El elemento 1 y 2 se regresan
        if x==2:
            op=buscar_opcode(arreglo[0].upper(),'0',arreglo[1],variables)
            return arreglo[0].upper(), arreglo[1],op
        if x==3:
            op=buscar_opcode(arreglo[1].upper(),'0',arreglo[1],variables)
            return arreglo[0].upper(), arreglo[1],op

def tres_elementos(arreglo,variables,x=0):
            
            if x==1:
                op=buscar_opcode(arreglo[0].upper(),arreglo[1],'0',variables)
                return arreglo[0].upper(), arreglo[1],arreglo[2],op               #El elemento 1, 2 y 3 se regresan
            if x==2:
                op=buscar_opcode(arreglo[1].upper(),arreglo[2],'0',variables)
                return arreglo[0], arreglo[1].upper(),arreglo[2],op               #El elemento 1, 2 y 3 se regresan

def suma_memoria(opcode):
        cuenta=0
        if opcode != 0 and opcode != None:
            for caracter in opcode:
                if caracter != ' ':
                    cuenta += 1
        return int(cuenta*.5)

    
    

    

programa=open("C:\\Users\\Sergio\\Desktop\\EXEMPLO.ASC","r")              #Abre el archivo

n_lineas=contar_lineas (programa)                                 #Cuenta las lineas que contiene el archivo

programa.seek(0)                                                   #Regresa el puntero al inicio del archivo
dir=0
eti=0
mne=0
var=0
op=0
dir_act=0
num_linea=0
direc=0
etiqueta,variables,linea_programa,opcode,direccion_actual,op_dir_act,directiva=reservar_memoria(n_lineas)
direccionActual = 0


for linea in programa.readlines():                                   #For que va a recorrer linea por linea del archivo
    
    linea_programa[num_linea]=linea
    linea=encuentra_asterisco(linea)
    arreglo=linea.split()
    directivas=linea.upper().split()
    
    if directivas.count("EQU")>=1:
        
            variables[var][0]=arreglo[0]
            variables[var][1]=arreglo[2]
            var+=1
            
            directiva[direc][0]=arreglo[2][1:]
            directiva[direc][1]=num_linea
            direc+=1
            
    elif directivas.count("ORG") >= 1:
        
            direccionActual = int(arreglo[1][1:],16)
            
            direccion_actual[dir_act][0]=int(arreglo[1][1:],16)
            direccion_actual[dir_act][1]=num_linea+1
            
            directiva[direc][0]=arreglo[1][1:]
            directiva[direc][1]=num_linea
            
            dir_act+=1
            direc+=1
            
    elif directivas.count("END") >=1:
        
        print("\n\tEncuentro de END y primera pasada terminada")
        break
    
    else:        
        if contar_elementos_linea(linea)==1:
        
            if linea[0]==" " or linea[0]=="\t" :
            
                mne,opcode[op][0]=un_elemento(arreglo,variables,1)                #El elemento 1 se guarda en el mnemonico
            
                print("\nLa direccion actual es:", format(direccion_actual[dir_act-1][0],'X'))
                print("El mnenomico es:",mne)
                print("El opcode es:",opcode[op][0])
                direccionActual += suma_memoria(opcode[op][0])
                
                direccion_actual[dir_act][0]=direccion_actual[dir_act-1][0]+suma_memoria(opcode[op][0])
                direccion_actual[dir_act][1]=num_linea+1
                
                opcode[op][1]=num_linea
                
                op+=1
                dir_act+=1
                
            else:
            
                etiqueta[eti][0]=un_elemento(arreglo,variables)                      #El elemento 1 se guarda en etiqueta
                etiqueta[eti][1]=format(direccion_actual[dir_act-1][0],'X')
                print("\n*Es una etiqueta")
                print("\nLa direccion actual es:", format(direccion_actual[dir_act-1][0],'X'))
                print("La etiqueta es:",etiqueta[eti])
                eti+=1
        
        elif contar_elementos_linea(linea)==2:
        
                if linea[0]==" " or linea[0]=="\t" :                          #Condici�n por si el elemento primero de la linea es espacio o tabulaci�n
            
                    if arreglo[1].count("#")>=1 or arreglo[1].count("$")>=1:
                
                        mne,dir,opcode[op][0]=dos_elementos(arreglo,variables,1)                           #El elemento 1 se guarda como mnemonico, elemento 2 se guarda como direcci�n
                
                        print ("\n*Es un mnemonico")
                        print("\nLa direccion actual es:", format(direccion_actual[dir_act-1][0],'X'))
                        print("El mnenomico es:",mne,"\nLa direccion es:", dir,"\nEl op es:",opcode[op][0])
                        direccionActual += suma_memoria(opcode[op][0])
                        
                        direccion_actual[dir_act][0]=direccion_actual[dir_act-1][0]+suma_memoria(opcode[op][0])
                        direccion_actual[dir_act][1]=num_linea+1
                                                
                        opcode[op][1]=num_linea
                        
                        op+=1
                        dir_act+=1
                    else:
                
                        mne,et,opcode[op][0]=dos_elementos(arreglo,variables,2)                             #El elemento 1 se guarda como mnemonico, elemento 2 se guarda como etiqueta

                        print ("\n*Es un mnemonico")
                        print("\nLa direccion actual es:", format(direccion_actual[dir_act-1][0],'X'))
                        print("El mnenomico es:",mne,"\nLa etiqueta es:",et,"\nEl op es:",opcode[op][0])
                        direccionActual += suma_memoria(opcode[op][0])
                        
                        direccion_actual[dir_act][0]=direccion_actual[dir_act-1][0]+suma_memoria(opcode[op][0])
                        direccion_actual[dir_act][1]=num_linea+1

                        opcode[op][1]=num_linea
 
                        op+=1
                        dir_act+=1
        
                else:
                    etiqueta[eti][0],mnemonico[mne][0],opcode[op][0]=dos_elementos(arreglo,variables,3)                             #El elemento 1 se guarda como etiqueta, elemento 2 se guarda como mnemonico
                    etiqueta[eti][1]=format(direccion_actual[dir_act-1][0],'X')
                    
                    print("\n*Es una etiqueta")
                    print("\nLa direccion actual es:", format(direccion_actual[dir_act-1][0],'X'))
                    print("La etiqueta es:",etiqueta[eti],"\nEl mnemonico es:",mnemonico[mne],"\nEl op es:",opcode[op][0])
                    direccionActual += suma_memoria(opcode[op][0])
                    
                    direccion_actual[dir_act][0]=direccion_actual[dir_act-1][0]+suma_memoria(opcode[op][0])
                    direccion_actual[dir_act][1]=num_linea+1
                    

                    
                    opcode[op][1]=num_linea
                    
                    op+=1
                    dir_act+=1    
                    eti+=1
            
        elif contar_elementos_linea(linea)==3:
                  
            if linea[0]==" " or linea[0]=="\t" :                                                        #Condici�n por si el elemento primero de la linea es espacio o tabulaci�n
                mne,dir,et,opcode[op][0]=tres_elementos(arreglo,variables,1)      #El elemento 1 se guarda en etiqueta, el 2 como mnemonico y el 3 como direccion

                print ("\n*Es un mnemonico")
                print("\nLa direccion actual es:", format(direccion_actual[dir_act-1][0],'X'))
                print("El mnenomico es:",mne,"\nLa direccion es:", dir,"\nLa etiqueta es:",et,"\nEl op es:",opcode[op][0])
                direccionActual += suma_memoria(opcode[op][0])
                
                direccion_actual[dir_act][0]=direccion_actual[dir_act-1][0]+suma_memoria(opcode[op][0])
                direccion_actual[dir_act][1]=num_linea+1
                                
                opcode[op][1]=num_linea
                                
                op+=1               
                dir_act+=1        
            
            else:
                etiqueta[eti][0],mne,dir,opcode[op][0]=tres_elementos(arreglo,variables,2)     #El elemento 1 se guarda en etiqueta, el 2 como mnemonico y el 3 como direccion
                etiqueta[eti][1]=format(direccion_actual[dir_act-1][0],'X')
                
                print("\n*Es una etiqueta")
                print("\nLa direccion actual es:", format(direccion_actual[dir_act-1][0],'X'))
                print("La etiqueta es:",etiqueta[eti],"\nEl mnemonico es:",mne,"\nLa direccion es:",dir,"\nEl op es:",opcode[op][0])
                direccionActual += suma_memoria(opcode[op][0])
                
                direccion_actual[dir_act][0]=direccion_actual[dir_act-1][0]+suma_memoria(opcode[op][0])
                direccion_actual[dir_act][1]=num_linea+1
                
                opcode[op][1]=num_linea
                
                op+=1                   
                dir_act+=1     
                eti+=1
  
    num_linea+=1            

etiqueta=etiqueta[:eti]
directiva=directiva[:direc]
direccion_actual=direccion_actual[:dir_act]
opcode=opcode[:op]
dir_y_op=0

print(etiqueta)

for lineaop in range(op):
    for lineadir in range(dir_act):
        if opcode[lineaop][1]+1==direccion_actual[lineadir][1]:
            
            op_dir_act[dir_y_op][0]=str(format(direccion_actual[lineadir-1][0],'X'))+"\t"+opcode[lineaop][0]
            op_dir_act[dir_y_op][1]=opcode[lineaop][1]
            dir_y_op+=1
            #format(direccion_actual[dir_act-1][0],'X')

archivo=open("C:\\Users\\Sergio\\Desktop\\EXEMPLO.lst","w")
   
direc=0
dir_y_op=0

for linea in range(n_lineas):
    x=0
    if linea_programa[linea].count("END") >=1:
        archivo.write(str(linea+1)+" A\t\t\t\t"+linea_programa[linea])
        break
    if len(directiva)>0:
        if directiva[direc][1]==linea:
            archivo.write(str(linea+1)+" A\t\t"+str(directiva[direc][0])+"\t"+linea_programa[linea])
            x=1
            if direc<len(directiva)-1:
                direc+=1
    if op_dir_act[dir_y_op][1]==linea:
        archivo.write(str(linea+1)+" A\t"+op_dir_act[dir_y_op][0]+"\t"+linea_programa[linea])
        x=1
        if dir_y_op<len(op_dir_act)-1:
            dir_y_op+=1
    if x==0:
        archivo.write(str(linea+1)+" A\t\t\t"+linea_programa[linea])
archivo.close()
programa.close()                                                      #Cerrar el archivo