import sys
import random
import primes
import numpy as np
import textwrap


class BlumBlumShub(object):


    def generarPrimo(self, bits):
        """Genera el numero primo, necesario para utilizar Blum Blum Shub"""
        while True:
            p = primes.bigppr(bits)
            if p & 3 == 3:
                return p

    def generarN(self, bits):
        """
        Selecciona el valor de n utilizado en BBS
        """
    
        p = self.generarPrimo(bits//2)
        while 1:
            q = self.generarPrimo(bits//2)
            if p != q:
                return p * q    

    def __init__(self, bits):
        """
        Este constructor indica cuantos bits recibira BBS
        """        
        self.n = self.generarN(bits)
        length = self.bitLen(self.n)
        seed = random.getrandbits(length)
        self.semilla(seed)  

    def semilla(self, seed):
        self.state = seed % self.n
    
    def bitLen(self, x):
        " Get the bit lengh of a positive number" 
        assert x > 0
        q = 0 
        while x: 
            q += 1 
            x >>= 1 
        return q     

    def next(self, numBits):
        "Returns up to numBit random bits"
        
        result = 0
        for i in range(numBits):
            self.state = (self.state**2) % self.n
            result = (result << 1) | (self.state&1)
        
        return result    

if __name__ == "__main__":
    
    bbs = BlumBlumShub(128);    
    print("numero bits: 128")
    for i in range (1):
        #print(bbs.next(128))
        cadena = str(hex(bbs.next(128)))
        cadena = cadena[2:-1]
        print (cadena)
        llave = np.asarray(textwrap.wrap(cadena,2)).reshape(4,4)
        print (llave)

    print(llave)






