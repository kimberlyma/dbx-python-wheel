import sys
from math import factorial
from decimal import Decimal, getcontext

# Chudnovsky algorithm for figuring out pi
getcontext().prec=1000

def calc_pi(n):
    t= Decimal(0)
    pi = Decimal(0)
    deno= Decimal(0)

    for k in range(n):
        t = ((-1)**k)*(factorial(6*k))*(13591409+545140134*k)
        deno = factorial(3*k)*(factorial(k)**3)*(640320**(3*k))
        pi += Decimal(t)/Decimal(deno)
    pi = pi * Decimal(12) / Decimal(640320 ** Decimal(1.5))
    pi = 1/pi
    
    print(round(pi,n))



    return(round(pi,n))

def entry(args=None):
    if not args:
        return  
    
    n = int(args[0])
    
    calc_pi(n)

if __name__ == "__main__":
    entry(sys.argv)