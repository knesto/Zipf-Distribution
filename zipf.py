import math
import random

alpha=1
n=10
x = -1 
m_bFirst = True #// Static first time flag
c=0 #Normalization constant

def nextZipf():
    global alpha,n,x,m_bFirst,c
    
    zipf_value = 0
    # Compute normalization constant on first call only
    if (m_bFirst==True):
        i=1
        while i <=n:
            c = c + (1.0 / math.pow(float (i), alpha))
            i=i+1
    c = 1.0 / c;
    m_bFirst = False

    #Pull a uniform random number (0 < z < 1)
    i = 1
    while True:
        z = rand_val(0)
        if((z != 0) or (z !=1)):
            break
        i = i + 1
    
    #Map z to the value
    sum_prob = 0
    i=1
    while i <=n:
        sum_prob = sum_prob+c / math.pow(float (i), alpha)
        if sum_prob>= z:
            zipf_value = i
            break
        i=i+1
    return (int (zipf_value)-1)

"""//=========================================================================
//	= Multiplicative LCG for generating uniform(0.0, 1.0) random numbers    =
//	=   - x_n = 7^5*x_(n-1)mod(2^31 - 1)                                    =
//	=   - With x seeded to 1 the 10000th x value should be 1043618065       =
//	=   - From R. Jain, "The Art of Computer Systems Performance Analysis," =
//	=     John Wiley & Sons, 1991. (Page 443, Figure 26.2)                  =
//========================================================================="""

def rand_val(seed):
    global x
    a = 16807 #Multiplier
    m = 2147483647 #Modulus
    q = 127773 #m div a
    r = 2836 #m mod a
    
    #Set the seed if argument is non-zero and then return zero
    if (seed > 0):
        x = seed
        return (0.0)
    
    #RNG using integer arithmetic
    x_div_q = x / q #x divided by q
    x_mod_q = x % q #x modulo q
    x_new = (a * x_mod_q) - (r * x_div_q) #New x value

    if (x_new > 0):
        x = x_new
    else:
      x = x_new + m
    # Return a random value between 0.0 and 1.0
    return (float (x) / m)
    
def main():
    pin= [0] * 10 
    count=0
    nRand= random.random()
    rand_val(nRand)
    for i in range(1000):
        nZipf = int(nextZipf())    
        pin[nZipf]=(pin[nZipf]+1)
           
    for j in range(len(pin)):
        print(pin[j]," ")

if __name__=="__main__":
    main()
