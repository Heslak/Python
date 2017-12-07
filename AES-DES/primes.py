from __future__ import division

import random

def bigppr(bits=256):
    """
    Generador aleatorio
    """
     
    candidate = random.getrandbits(bits) | 1 

    prob = 0
    while 1:
        prob=pptest(candidate)
        if prob>0:
            return candidate
        candidate += 2
        
def pptest(n):
    """Verificamos si es un numero   primo"""

    
    if n<=1: 
        return 0

    bases  = [random.randrange(2,50000) for x in range(90)]

    
    for b in bases:
        if n%b==0: 
            return 0
        
    tests,s  = float(0),0
    #tests,s  = 0,0

    m        = n-1


    while not m&1:  
        m >>= 1
        s += 1

    for b in bases:
        tests += 1
        isprob = algP(m,s,b,n)
        if not isprob: 
            break
            
    if isprob: 
        return (1-(1./(4**tests)))
    
    return 0

def algP(m,s,b,n):
    y = pow(b,m,n)    
    for j in range(s):
        if (y==1 and j==0) or (y==n-1):
            return 1
        y = pow(y,2,n)       
       
        return 0


