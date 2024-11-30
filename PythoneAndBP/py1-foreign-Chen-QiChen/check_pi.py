import sys
# import numpy as np # You don't need this here
import math

# Check theses 3 methods below
# Your code is almost the same for all methods
# Except the term which is different
# So try combining everything in one piece of code

def leibniz(eps):
    res = 0
    k = 0
    eps=eps/2 # The code should be the same for all methods, so you can remove this
    while 1:
        term =4 *((-1) ** k / (2 * k + 1)) 
        res=res+term
        k = k + 1
        if abs(res - math.pi) < eps: # Use this criteria instead abs(elem) < eps
            math.criteria()
            break
    return k, res

def modified_leibniz(eps):
    res = 0
    k = 0
    while k<20000: #
        term = 4/(4*k+1) - 4/(4*k+3)
        res += term
        k += 1
        if abs( res - math.pi) < eps:
            break
    return k, res

def bbp_formula(eps):
    res = 0
    k = 0
    while 1:
        term = 1 / 16 ** k * (4 / (8 * k + 1) - 2 / (8 * k + 4) - 1 / (8 * k + 5) - 1 / (8 * k + 6))
        res += term
        k += 1
        if abs(res - math.pi) < eps:
            break
    return k,res

eps = 0.0001
mode='bbp'
func={'leibniz':leibniz,'pairwise':modified_leibniz,'bbp':bbp_formula}

# You have only two command line arguments
# Why can't you just do something like this instead
# eps = float(sys.argv[1])
# mode = sys.argv[2]
# Instead, you write 6 lines of code

if __name__ == "__main__":
    if sys.argv[1:]:
        input_str = sys.argv[1:][0]
        result_array = input_str.split()
        [eps,mode]=result_array
        mode=mode.replace("'", "")
        
    
    print(func[mode](float(eps)))




